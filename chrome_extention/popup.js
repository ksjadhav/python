document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    // Load tasks from storage
    chrome.storage.local.get(['tasks'], function(result) {
        const tasks = result.tasks || [];
        tasks.forEach(task => addTaskToList(task));
    });

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const task = taskInput.value.trim();
        if (task) {
            addTaskToList(task);
            saveTask(task);
            taskInput.value = '';
        }
    });

    function addTaskToList(task) {
        const li = document.createElement('li');
        const truncatedTask = task.length > 20 ? task.substring(0, 20) + '...' : task;
        li.textContent = truncatedTask;
        li.title = task; // Show full task on hover
        const removeLink = document.createElement('a');
        removeLink.href = '#';
        removeLink.textContent = 'Remove';
        removeLink.addEventListener('click', function() {
            removeTask(task);
            taskList.removeChild(li);
        });
        li.appendChild(removeLink);
        taskList.appendChild(li);
    }

    function saveTask(task) {
        chrome.storage.local.get(['tasks'], function(result) {
            const tasks = result.tasks || [];
            tasks.push(task);
            chrome.storage.local.set({ tasks: tasks });
        });
    }

    function removeTask(task) {
        chrome.storage.local.get(['tasks'], function(result) {
            let tasks = result.tasks || [];
            tasks = tasks.filter(t => t !== task);
            chrome.storage.local.set({ tasks: tasks });
        });
    }
});