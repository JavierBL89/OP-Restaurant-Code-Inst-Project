
const sendEmail = $('.send-email');
const close = $('#close');
const modalContact = $('.modal-contact');

/***** SHOW CONTACT FORM POPUP ****/
sendEmail.on('click', function(ev){

    modalContact.fadeIn("slow");
    
});

/***** CLOSE CONTACT FORM POPUP ***/
close.on('click', function(ev){
    console.log('puta');
    modalContact.fadeOut("slow");

});



