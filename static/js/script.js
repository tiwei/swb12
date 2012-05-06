/* Author:

*/


$(document).ready(function() { 

$('.btn-large').hover(function() {
	$(this).removeClass('btn-danger').addClass('btn-warning'); 
}, function() { 
	$(this).removeClass('btn-warning').addClass('btn-danger'); 
});

$('.btn-large').click(function() {
	$(this).removeClass('btn-warning').addClass('btn-success'); 
});

$('.btn-large').mousedown(function() {
	$(this).removeClass('btn-warning').addClass('btn-success'); 
});

$('.btn-large').mouseout(function() {
	$(this).removeClass('btn-success').addClass('btn-warning'); 
});

$('input.star3').rating();
$('input.star1').rating();

$("#skills").tagCloud(tags);

});