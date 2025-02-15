// script.js
document.addEventListener('DOMContentLoaded', () => {
 const button = document.getElementById('clickButton');
 const output = document.getElementById('output');

 button.addEventListener('click', () => {
     output.textContent = 'Hello, you clicked the button!';
 });
});
