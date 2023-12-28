<script>
  export let conversations = [];
  export let selectedUserId; // 선택된 사용자의 ID
  export let onConversationSelect;
  let selectedConversationId = null;

  const selectConversation = (conversation) => {
    selectedConversationId = conversation._id;
    if (onConversationSelect) {
      onConversationSelect(conversation);
    }
  };
</script>

{#if selectedUserId}
  {#if conversations.length > 0}
    <ul>
      {#each conversations as conversation}
        <li 
          class:selected="{conversation._id === selectedConversationId}" 
          on:click={() => selectConversation(conversation)}>
          {conversation.title}
        </li>
      {/each}
    </ul>
  {:else}
    <p>대화가 없습니다.</p>
  {/if}
{:else}
  <!-- 사용자 선택이 되지 않은 경우 아무것도 표시하지 않음 -->
{/if}

<style>
  li {
    cursor: pointer;
    padding: 5px;
    white-space: nowrap; /* 텍스트를 한 줄로 유지 */
    overflow: hidden; /* 넘치는 내용 숨김 */
    text-overflow: ellipsis; /* 넘치는 텍스트를 말줄임표로 표시 */
  }
  li:hover {
    background-color: #f0f0f0;
  }
  .selected {
    background-color: lightgreen;
  }
</style>