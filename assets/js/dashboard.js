$(document).ready(function(){
    $('#navBtn').on('click', function(e){
        e.preventDefault();
        $('.ui.sidebar')
            .sidebar('setting', 'transition', 'scale down')
            .sidebar('toggle');
    });
    $('.ui.accordion').accordion();
});
