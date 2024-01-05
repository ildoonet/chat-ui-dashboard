from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS를 위한 라이브러리 임포트
from flask_caching import Cache
from pymongo import MongoClient, DESCENDING
from bson import ObjectId
import argparse
from collections import OrderedDict


# 명령줄 인자 파싱
parser = argparse.ArgumentParser(description="MongoDB Flask Server")
parser.add_argument("mongo_uri", help="MongoDB URI")
parser.add_argument("--port", type=int, default=8081, help="Port number for the Flask server")
args = parser.parse_args()

# MongoDB 연결
client = MongoClient(args.mongo_uri)
db = client['chat-ui']

app = Flask(__name__)
CORS(app)  # 모든 엔드포인트에 대해 CORS 허용

# 캐시 설정
cache = Cache(app, config={
    'CACHE_TYPE': 'simple',  # 메모리 기반 캐시
    'CACHE_DEFAULT_TIMEOUT': 300  # 5분(300초) 캐시 유지
})

# ObjectId를 문자열로 변환하는 함수
def convert_objectid_to_str(item):
    if '_id' in item:
        item['_id'] = str(item['_id'])
    if 'userId' in item:
        item['userId'] = str(item['userId'])
    return item

@app.route('/users', methods=['GET'])
# @cache.cached(timeout=300)
def get_users():
    # users 컬렉션과 sessions 컬렉션을 조인하여 사용자 정보와 최신 세션 정보를 가져옴
    pipeline = [
        {
            '$lookup': {
                'from': 'sessions',  # 조인할 컬렉션
                'localField': '_id',  # users 컬렉션의 필드
                'foreignField': 'userId',  # sessions 컬렉션의 필드
                'as': 'session'  # 결과를 저장할 필드 이름
            }
        },
        { '$unwind': '$session' },  # 각 문서에 대해 session 배열을 풀어서 단일 문서로 만듦
        { '$sort': { 'session.updatedAt': DESCENDING } },  # session의 updatedAt을 기준으로 정렬
        { '$project': { 'session': 0 } }  # session 정보는 제외하고 결과 반환
    ]
    users = db.users.aggregate(pipeline)
    user_list = [convert_objectid_to_str(user) for user in users]

    new_user_list = []
    for x in user_list:
        if x not in new_user_list:
            new_user_list.append(x)

    return jsonify(new_user_list)

@app.route('/conversations', methods=['GET'])
def get_conversations():
    user_id = request.args.get('user_id')
    page = int(request.args.get('page', 1))
    per_page = 100
    skip = (page - 1) * per_page

    query = {}
    if user_id:
        query['userId'] = ObjectId(user_id)
    conversations = db.conversations.find(query).sort("updatedAt", DESCENDING).skip(skip).limit(per_page)

    conversation_list = []
    for conv in conversations:
        conv = convert_objectid_to_str(conv)
        user_info = db.users.find_one({"_id": conv['userId']})
        if user_info:
            conv['user'] = convert_objectid_to_str(user_info)
        conversation_list.append(conv)

    return jsonify(conversation_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port, debug=True)
