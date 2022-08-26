
const sendEmail = $('#send-email');
const close = $('#close');
let puta = $('.overlay');

/***** SHOW CONTACT FORM POPUP ****/
sendEmail.on('click', function(ev){

    puta.fadeIn("slow");
    
});

/***** CLOSE CONTACT FORM POPUP ***/
close.on('click', function(ev){

    puta.fadeOut("slow");

});



