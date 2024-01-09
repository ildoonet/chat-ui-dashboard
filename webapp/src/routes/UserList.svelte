<script>
  export let users = [];
  export let onUserSelect;
  let selectedUserId = null;
  let searchTerm = ''; // Variable to store the search term

  // Reactive statement for filtering users
  $: filteredUsers = searchTerm
    ? users.filter(user => user.email.toLowerCase().includes(searchTerm.toLowerCase()))
    : users;

  const selectUser = (user) => {
    selectedUserId = user._id; // Save the ID of the selected user
    if (onUserSelect) {
      onUserSelect(user);
    }
  };
</script>

<input type="text" placeholder="Search by email..." bind:value={searchTerm} />

<ul>
  <li on:click={() => selectUser({_id: ''})}>
    All Users
  </li>

  {#each filteredUsers as user}
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
    background-color: lightblue;
  }
</style>