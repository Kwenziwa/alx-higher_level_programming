const request = require('request');

async function getCompletedTasksByUserId(apiUrl) {
  const response = await request.get(apiUrl);
  const todos = JSON.parse(response.body);

  const completedTasksByUserId = {};
  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (!completedTasksByUserId[userId]) {
        completedTasksByUserId[userId] = 0;
      }
      completedTasksByUserId[userId] += 1;
    }
  }

  return completedTasksByUserId;
}

async function printUsersWithCompletedTasks(completedTasksByUserId) {
  for (const userId in completedTasksByUserId) {
    const numCompletedTasks = completedTasksByUserId[userId];
    if (numCompletedTasks > 0) {
      console.log(`User ID: ${userId}, Number of completed tasks: ${numCompletedTasks}`);
    }
  }
}

if (require.main === module) {
  const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

  const completedTasksByUserId = await getCompletedTasksByUserId(apiUrl);

  await printUsersWithCompletedTasks(completedTasksByUserId);
}
