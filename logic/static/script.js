let nav = document.querySelector("nav");
let displayMenu = document.querySelector("nav ul");
let menu = document.querySelector(".menu");
let closeMenu = document.querySelector(".closeMenu");

const mobileMenu = () => {
  displayMenu.classList.add("add");
  closeMenu.style.display = "block";
  menu.style.display = "none";
};

closeMenu.addEventListener("click", () => {
  displayMenu.classList.remove("add");
  closeMenu.style.display = "none";
  menu.style.display = "block";
});