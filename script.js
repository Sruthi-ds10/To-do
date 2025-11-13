async function loadTasks() {
  const res = await fetch('/tasks');
  const tasks = await res.json();
  const list = document.getElementById('taskList');
  list.innerHTML = '';
  tasks.forEach(t => {
    list.innerHTML += `<li>${t.title} <button onclick="deleteTask(${t.id})">X</button></li>`;
  });
}

async function addTask() {
  const title = document.getElementById('taskInput').value;
  await fetch('/tasks', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({title})
  });
  document.getElementById('taskInput').value = '';
  loadTasks();
}

async function deleteTask(id) {
  await fetch('/tasks', {
    method: 'DELETE',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({id})
  });
  loadTasks();
}

loadTasks();
