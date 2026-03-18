document.addEventListener("DOMContentLoaded", function(){

/* ---------- LOADER ---------- */

let progress = 0;

const loader = document.getElementById("loader");
const progressBar = document.getElementById("loaderProgress");
const progressText = document.getElementById("loaderText");
const mainContent = document.getElementById("mainContent");

/* Fake smooth loading animation */

function updateLoader(){

    progress += Math.random() * 8;

    if(progress > 100) progress = 100;

    progressBar.style.height = progress + "%";
    progressText.innerText = Math.floor(progress) + "%";

    if(progress < 100){
        setTimeout(updateLoader, 50);
    } else {

        /* Fade out loader */
        loader.style.transition = "opacity 0.8s ease";
        loader.style.opacity = "0";

        setTimeout(()=>{
            loader.style.display = "none";

            /* Fade in site */
            mainContent.style.transition = "opacity 1s ease";
            mainContent.style.opacity = "1";

        }, 800);
    }
}

updateLoader();


/* ---------- FORM LOADING ---------- */

const form = document.getElementById("newsForm");
const loading = document.getElementById("loading");
const button = document.getElementById("analyzeBtn");

if(form){
form.addEventListener("submit", function(){

loading.style.display = "block";

button.innerText = "Analyzing...";
button.disabled = true;

});
}


/* ---------- PARTICLE BACKGROUND ---------- */

const canvas = document.getElementById("bg-canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

for(let i=0;i<80;i++){
particles.push({
x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
size:Math.random()*3+1,
speedX:(Math.random()-0.5)*0.5,
speedY:(Math.random()-0.5)*0.5
});
}

function animate(){
ctx.clearRect(0,0,canvas.width,canvas.height);

ctx.fillStyle="#B2FFFF";

particles.forEach(p=>{
p.x += p.speedX;
p.y += p.speedY;

if(p.x<0||p.x>canvas.width) p.speedX*=-1;
if(p.y<0||p.y>canvas.height) p.speedY*=-1;

ctx.beginPath();
ctx.arc(p.x,p.y,p.size,0,Math.PI*2);
ctx.fill();
});

requestAnimationFrame(animate);
}

animate();

window.addEventListener("resize",()=>{
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
});

});