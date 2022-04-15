// $(function(){
//     if($(window).width < 700){
//         $('ul')[0].removeAttribute("class");
//         $('body').css("background-color", "blue")
//         // $('.btn').addClass('backup-btn').removeClass('btn');
//         // $('.mybtn').addClass('dropdown-toggle').attr("data-toggle", "dropdown");
//         // $('.myanchor').addClass('anchor');
//     }
// });

jQuery(function(){
    setTimeout(
        function() {
            $(".bookings").slideDown(2000, "linear");
        }, 3000);
    
  });