const foldButtons = document.querySelectorAll(".fold-button");

for (const button of foldButtons) {
    const post = button.closest(".one-post");
    button.setAttribute("aria-expanded", "true");

    button.addEventListener("click", function () {
        const isFolded = post.classList.toggle("folded");
        button.textContent = isFolded ? "Развернуть" : "Свернуть";
        button.setAttribute("aria-expanded", String(!isFolded));
    });
}