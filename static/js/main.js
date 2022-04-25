new WOW().init()

const form = document.getElementById('booking_form')

let fname = document.getElementById("name");
let surname = document.getElementById("lname");
let prefix = document.getElementById("prefix");
let phone = document.getElementById("phone");
let email = document.getElementById("email");
let date = document.getElementById("date");
let start_time = document.getElementById("timepicker");
let party_size = document.getElementById("party_size");

function handleSubmit(event){

// const formField = input.parentElement;

form.addEventListener('submit', event => {
  event.preventDefault();
  event.stopPropagation()

  validateInputs()

// if(fname[0].value == ""){
//   console.log("puta")
//   document.getElementsByClassName("name")[0].parentElement.css("border-color", "red")
//   // fname.addClass("non-valid")
// }

})
}

function validateInputs(){
  const name = fname.value.trim()
  const surname = surname.value.trim()
  const prefix = prefix.value.trim()
  const phone = phone.value.trim()
  const email = email.value.trim()
  const date = date.value.trim()
  const start_date = start_time.value.trim()
  const party_size =party_size.value.trim()

  if(name == ""){

    setErrorFor(input, "Field cannot be blank")
  }
  else{
    setSuccessFor(input)
  }


}

// function validation(event) {

//     'use strict'
  
//     // Fetch all the forms we want to apply custom Bootstrap validation styles to
//     var forms = document.querySelectorAll('.validation')
//     let name = document.querySelectorAll('.name')[0].value;

//     // Loop over them and prevent submission
//     Array.prototype.slice.call(forms)
//       .forEach(function (form) {
//         form.addEventListener('submit', function (event) {
//           // if (!form.checkValidity()) {
//           event.preventDefault()
//           event.stopPropagation()
//           if(form.getAttribute("name").innerText == ""){
//             return console.log("puta")
//           }
  
//           // }
        

  
//           // form.classList.add('was-validated')
//         }, false)
//       })
//   }

  // function formatValidation(event){
  
  //   var phone = document.querySelectorAll('.phone')[0].value;

  //   if(phone.length > 9){
  //     console.log(phone.length)
  //     $(".phone").addClass("non-valid")
  //   }

  // }
