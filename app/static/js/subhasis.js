//NavBar

function toggleDropdown(container) {
    if (window.innerWidth <= 991) {
        container.classList.toggle('active');
        var bottomNavItems = document.querySelector('.bottomNavItems');
        bottomNavItems.classList.toggle('active');
    }
}

//NavBar
// For ScrollBar
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

let scrollDiv = document.getElementById("scrollDiv");
window.onscroll = function () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollDiv.style.display = "block";

    } else {
        scrollDiv.style.display = "none";
    }
};
//For Footer Tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

