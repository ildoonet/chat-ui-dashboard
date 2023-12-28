<script>
  export let users = [];
  export let onUserSelect;
  let selectedUserId = null;

  const selectUser = (user) => {
    selectedUserId = user._id; // 선택된 사용자의 ID를 저장
    if (onUserSelect) {
      onUserSelect(user);
    }
  };
</script>

<ul>
  <li on:click={() => selectUser({_id: ''})}>
    All Users
  </li>
  
  {#each users as user}
    <li 
      class:selected="{user._id === selectedUserId}" 
      on:click={() => selectUser(user)}>
      {user.email}
    </li>
  {/each}
</ul>

<style>
  li {
    cursor: pointer;
    padding: 5px;
  }
  li:hover {
    background-color: #f0f0f0;
  }
  .selected {
    background-color: lightblue; /* 선택된 항목에 대한 배경색 변경 */
  }
</style>

