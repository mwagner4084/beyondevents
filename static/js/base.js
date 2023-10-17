function toggleMobileMenu(menu) {
  menu.classList.toggle('open');
}

$(document).ready(function(){
	$('#menu-icon').click(function(){
		$('.site-header').toggleClass('open');
	});
});
