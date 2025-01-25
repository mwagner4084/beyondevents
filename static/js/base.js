function toggleMenu() {
  let menu = document.getElementById("fullscreen-nav");
  menu.classList.toggle("active");
}

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("menu-icon").addEventListener("click", toggleMenu);
  document.querySelector(".close-btn").addEventListener("click", toggleMenu);
});


$(document).ready(function(){
  $('#menu-icon').click(function(){
      toggleMenu();
  });

  $('.close-btn').click(function(){
      toggleMenu();
  });
});


const cards = document.querySelectorAll(".card-gallery");  // Changed class from '.card' to '.card-gallery'

function isElementInViewport(el) {
  const rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

function isCardVisible() {
  for (const card of cards) {  // Added 'const' for better scoping
    isElementInViewport(card)
      ? card.classList.add("isVisible")
      : card.classList.remove("isVisible");
  }
}

document.addEventListener("DOMContentLoaded", isCardVisible);
window.addEventListener("scroll", isCardVisible);
window.addEventListener("resize", isCardVisible);
