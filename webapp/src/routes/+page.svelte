<script>
	import { onMount } from 'svelte';
	import UserList from './UserList.svelte';
	import ConversationList from './ConversationList.svelte';
	import ConversationDetails from './ConversationDetails.svelte';
  
	let users = [];
	let conversations = [];
	let selectedUser = null;
	let selectedConversation = null;

	const fetchUsers = async () => {
          const currentUrl = new URL(window.location.href);
          const protocol = currentUrl.protocol;
          const host = currentUrl.hostname;

	  const response = await fetch(`${protocol}//${host}:8081/users`);
	  users = await response.json();
	};
  
	const fetchConversations = async (userId) => {
          const currentUrl = new URL(window.location.href);
          const protocol = currentUrl.protocol;
          const host = currentUrl.hostname;

	  const response = await fetch(`${protocol}//${host}:8081/conversations?user_id=${userId}`);
	  conversations = await response.json();
	};
  
	onMount(() => {
	  

	  fetchUsers();
	});
  
	const handleUserSelect = (user) => {
	  selectedUser = user;

	  fetchConversations(user._id);
	};
  
	const handleConversationSelect = (conversation) => {
	  selectedConversation = conversation;
	};
</script>
  

<div class="flex h-screen">
    <div class="flex flex-col w-1/8 overflow-auto m-2 p-2 border rounded bg-gray-100">
      <UserList {users} onUserSelect={handleUserSelect} />
    </div>
    <div class="flex flex-col w-1/4 overflow-auto m-2 p-2 border rounded bg-gray-100">
      {#if selectedUser}
        <ConversationList {conversations} selectedUserId={selectedUser._id} onConversationSelect={handleConversationSelect} />
      {/if}
    </div>
    <div class="flex flex-col w-3/4 overflow-auto m-2 p-2 border rounded bg-white">
      {#if selectedConversation}
        <ConversationDetails {selectedConversation} />
      {/if}
    </div>
</div>
