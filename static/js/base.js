function toggleMobileMenu(menu) {
  menu.classList.toggle('open');
}

const hamburger = document.getElementById('hamburger-icon');
if (hamburger) {
  hamburger.addEventListener('click', () => {
    toggleMobileMenu(hamburger);
  });
}

$(document).ready(function(){
	$('#nav-icon').click(function(){
		$(this).toggleClass('open');
	});
});

$(document).ready(function(){
  $('#nav-icon').click(function(){
    toggleMobileMenu($('.mobile-menu'));
  });
});