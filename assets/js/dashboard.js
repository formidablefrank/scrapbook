$(document).ready(function(){
    $('.ui.sidebar')
      .sidebar({
        context: $('.bottom.segment')
      })
      .sidebar('attach events', '#navBtn')
    ;
    $('.ui.accordion').accordion();
    $('#navBtn').on('click', function(e){
        e.preventDefault();
        if($('#content.thirteen.wide.column').length){
            $('#content').removeClass('thirteen wide column');
            $('#content').addClass('sixteen wide column');
        }
        else if($('#content.sixteen.wide.column').length){
            $('#content').removeClass('sixteen wide column');
            $('#content').addClass('thirteen wide column');
        }
        $('.ui.sidebar')
            .sidebar('setting', 'transition', 'push')
            .sidebar('toggle');
    });
    $('.message .close')
        .on('click', function() {
        $(this)
        .closest('.message')
        .transition('fade');
    });
});
