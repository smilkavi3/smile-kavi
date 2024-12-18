// Get all buttons with the class 'qn'
const buttons = document.querySelectorAll('.qn');

// Loop through each button and add a click event listener using a for loop
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', () => {
        // Get the content div that corresponds to the clicked button
        const contentDiv = buttons[i].nextElementSibling;

        // Toggle the 'show' class to control visibility
        contentDiv.classList.toggle('visible');
        buttons[i].classList.toggle('expand');
    });
}