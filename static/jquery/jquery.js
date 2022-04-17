
/* Ddocument onload */
jQuery(function(){
    /* modal animation*/
    setTimeout(
        function() {
          $(".bookings").slideDown(2000, "linear");
        }, 3000);
    
    /* headding mousehover */
    $(document).on("mouseover", function(){
      $(".headding h1").addClass("hover");
      });
  });


  