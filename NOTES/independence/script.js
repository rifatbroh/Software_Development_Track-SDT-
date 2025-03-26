
const day = document.getElementById("celebrateButton");
const flag = document.getElementById("flagContainer");
const celebrateText = document.getElementById("celebrateText");

day.addEventListener("click", function() {
    flag.classList.add("show");
    day.innerHTML = "Best of luck";

    setTimeout(function() {
        celebrateText.style.opacity = 1;
    }, 20);
});
