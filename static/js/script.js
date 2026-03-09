// Fade-in animation when page loads

window.addEventListener("load", () => {

    const elements = document.querySelectorAll(".glass-card, .hero-title, .hero-sub");

    elements.forEach((el, index) => {

        el.style.opacity = 0;
        el.style.transform = "translateY(20px)";

        setTimeout(() => {
            el.style.transition = "all 0.8s ease";
            el.style.opacity = 1;
            el.style.transform = "translateY(0)";
        }, index * 200);

    });

});



// Button loading animation

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const button = document.querySelector(".analyze-btn");

    if(form){

        form.addEventListener("submit", () => {

            button.innerText = "Analyzing...";
            button.disabled = true;

        });

    }

});