
const menuToggle = document.getElementById('check');
const navMenu = document.querySelector('ul');

// Handle the checkbox state change (triggered when clicking on the hamburger icon)
menuToggle.addEventListener('click', function() {
    if (menuToggle.checked) {
        // When checked, show the menu (transition left to 0)
        navMenu.style.left = '0'; // This will trigger the transition
        navMenu.style.transition=".5s ease all"
    } else {
        // When unchecked, hide the menu (move it off-screen)
        navMenu.style.left = '-100%'; // This will trigger the transition
    }
});
