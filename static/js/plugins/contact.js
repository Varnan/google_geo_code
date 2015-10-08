/*------------------------------------------------------------------
Project:    Mosaic
Author:     Yevgeny S.
URL:        http://simpleqode.com/
            https://twitter.com/YevSim
Version:    1.3.0
Created:        20/01/2014
Last change:    25/02/2015
-------------------------------------------------------------------*/


/**s
 * Contact form
 */

$(document).ready(function(e) {
  $("#form_message").hide();

  $("#form_sendemail").validate({
    rules: {
        name: "required",
        phone: "required",
    },
    messages: {
        name: "Please enter your name",
        phone: "Please enter your contact no.",
    }
  });
  
  $('#form_sendemail').submit(function(e) {
    if($('#form_sendemail').valid()) 
    {
      $.ajax({
        url: 'http://api.shadowfax.in/contactus/',
        type: 'POST',
        data: $(this).serialize(),
        dataType: 'json',
        beforeSend: function (XMLHttpRequest) {
          //
          $('.contact__form').fadeTo("slow", 0.33);
          $('#form_sendemail .has-error').removeClass('has-error');
          $('#form_sendemail .help-block').html('');
        },
        success: function( json, textStatus ) {
          
//             $('#form_message').addClass('alert-success').html( json.success );
//             $("#form_message").show();
//             setTimeout(function(){
//                 $("#form_message").hide();
//                 $('#form_message').removeClass('alert-success').html('');
//             },2000);
         
        },
        complete: function( XMLHttpRequest, textStatus ) {
          $("#form_message").show();
          setTimeout(function(){
                $("#form_message").hide();
            },4000);
          document.getElementById('form_sendemail').reset();
          $('.contact__form').fadeTo("fast", 1);
        }
      });
    }
    return false;
  });
});
