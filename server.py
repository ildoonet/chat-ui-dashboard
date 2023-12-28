from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS를 위한 라이브러리 임포트
from flask_caching import Cache
from pymongo import MongoClient, DESCENDING
from bson import ObjectId
import argparse


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
@cache.cached(timeout=300)  # 5분 캐시
def get_users():
    users = db.users.find().sort("updatedAt", DESCENDING)
    user_list = [convert_objectid_to_str(user) for user in users]
    return jsonify(user_list)

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
