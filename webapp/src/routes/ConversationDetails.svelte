<script>
  import { marked } from 'marked';
  export let selectedConversation;

  // 마크다운을 HTML로 변환하는 함수
  const renderMarkdown = (markdownText) => {
    return marked(markdownText);
  };
</script>

{#if selectedConversation}
  <div>
    <h2>대화 상세 내용</h2>
    <ul>
      {#each selectedConversation.messages as message}
        <li>
          <strong>{message.from}: </strong>
          <p>{@html renderMarkdown(message.content)}</p>
        </li>
      {/each}
    </ul>
  </div>
{:else}
  <p>대화를 선택해주세요.</p>
{/if}
  
  <style>
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