<script>
  import { marked } from 'marked';
  export let selectedConversation;

  // 마크다운을 HTML로 변환하는 함수
  const renderMarkdown = (markdownText) => {
    // 개행 문자를 <br/>로 변환
    // const convertedText = markdownText.replace(/\n/g, '<br/>');
    const convertedText = markdownText;
    // 변환된 텍스트를 마크다운으로 렌더링
    return marked.parse(convertedText);
  };
</script>

{#if selectedConversation}
  <div>
    <h2>{selectedConversation.model}</h2>
    <p class="date">{selectedConversation.createdAt}</p>

    <ul>
      {#each selectedConversation.messages as message}
        <li>
          <strong>{message.from}: </strong>
          <article class="prose prose-slate">
            {@html renderMarkdown(message.content)}
          </article>
        </li>
      {/each}
    </ul>
  </div>
{:else}
  <p>대화를 선택해주세요.</p>
{/if}
  
  <style>
    .date {
      margin-bottom: 20px; /* 날짜와 메시지 목록 간의 간격 */
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      margin-bottom: 15px;
    }
    strong {
      display: block; /* 발신자를 별도 줄에 표시 */
    }
  </style>