
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

      $(function(){
        var date_input=$('input[name="date"]'); //our date input has the name "date"
        var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
        date_input.datepicker({
            format: 'mm/dd/yyyy',
            container: container,
            todayHighlight: true,
            autoclose: true,
        })

        $('#timePicker').clockTimePicker({  
          duration: true,
          durationNegative: true,
         precision: 5,
         i18n: {
          cancelButton: 'Abbrechen'
          },
         onAdjust: function(newVal, oldVal) {
          //...
          }
        });
     });
  });


  