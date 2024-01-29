'use strict';

document.addEventListener('DOMContentLoaded', function () {
    const taskList = document.querySelector('#taskList');
    const todoForm = document.querySelector('#todo');

    todoForm.addEventListener('submit', function (event) {
        // Prevent default behavior
        event.preventDefault();
        // Query the current form selectors
        const taskInput = this.querySelector('input[name="task"]');
        generateTodoList(taskInput);
    });

    function generateTodoList(taskInput) {
        // Create a li element to hold the text
        const taskElement = document.createElement('li');
        // Add the value and upvote count to to the new element
        taskElement.textContent = taskInput.value;
        // Create an element to hold the counter
        const voteCount = document.createElement('span');
        voteCount.classList.add('counter');
        voteCount.textContent = '0';
        taskElement.appendChild(voteCount);
        // Append the new element to the existing list
        taskList.appendChild(taskElement);
        // Reset the form
        taskInput.value = '';
        // Pass the LI to the function that binds the `click` event
        handleUpvote(taskElement);
    }

    function handleUpvote(element) {
        // Bind a click handler to the element
        element.addEventListener('click', function (e) {
            // get the counter value
            const counter = e.target.querySelector('.counter');
            // convert the string to a number
            const countValue = Number(counter.textContent);
            // increment by 1
            const newCount = countValue + 1;
            // Update the counter element
            counter.textContent = newCount;
        });
    }
});