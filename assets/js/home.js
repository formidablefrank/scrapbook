$(document)
  .ready(function() {

    $('body').attr('id', 'home');
    var
      changeSides = function() {
        $('.ui.shape')
          .eq(0)
            .shape('flip over')
            .end()
          .eq(1)
            .shape('flip over')
            .end()
          .eq(2)
            .shape('flip back')
            .end()
          .eq(3)
            .shape('flip back')
            .end()
        ;
      },
      validationRules = {
        firstName: {
          identifier  : 'email',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter an e-mail'
            },
            {
              type   : 'email',
              prompt : 'Please enter a valid e-mail'
            }
          ]
        }
      }
    ;

    $('.ui.card').popup();

    $('.ui.dropdown')
      .dropdown({
        on: 'hover'
      })
    ;

    $('.ui.form')
      .form(validationRules, {
        on: 'blur'
      })
    ;

    $('.masthead .information')
      .transition('scale in', 1000)
    ;

    setInterval(changeSides, 3000);

    $('#homeBtn').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#home").offset().top
        }, 800);
    });
    $('#featuresBtn').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#features").offset().top - 100
        }, 800);
    });
    $('#recentBtn').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#recent").offset().top - 50
        }, 800);
    });
    $('#clientsBtn').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#clients").offset().top - 50
        }, 800);
    });

  })
;
