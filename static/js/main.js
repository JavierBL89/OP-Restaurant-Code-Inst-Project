new WOW().init()

const form = document.getElementById('booking_form')

let fname = document.getElementById("name");
let surname = document.getElementById("l_name");
let prefix = document.getElementById("prefix");
let phone = document.getElementById("phone");
let email = document.getElementById("email");
let date = document.getElementById("date");
let start_time = document.getElementById("start_time");
let party_size = document.getElementById("party_size");


/**
* INITIALIZE FORM VALIDATION
**/
function handleSubmit(event){

form.addEventListener('submit', event => {
  event.preventDefault();
  event.stopPropagation()
  validateInputs()
})
}

/**
* GET INPUTS VALUE AND CHECK BLANK FIELDS
**/
function validateInputs(){
  // get the values from inputs
  const nameValue = fname.value.trim()
  const lastNameValue = surname.value.trim()
  const prefixValue = prefix.value.trim()
  const phoneValue = phone.value.trim()
  const emailValue = email.value.trim()
  const dateValue = date.value.trim()
  const start_timeValue = start_time.value.trim()
  // const party_sizeValue =party_size.value.trim()

    if(nameValue === ""){
      setErrorForBlank(fname, "Field cannot be blank");
    }else{
      checkLength(fname)
    }
  
    if(lastNameValue === ""){
      setErrorForBlank(surname, "Field cannot be blank");
    }else{
      checkLength(surname)
    }

    if(phoneValue === ""){
      setErrorForBlank(phone, "Field cannot be blank");
    }else{
      checkLength(phone)
    }

    if(emailValue === ""){
      setErrorForBlank(email, "Field cannot be blank");
    }else{
      emailValidation(emailValue)
    }

    if(dateValue === ""){
      date.className = "form-control error"
    }else{
      dateValidation(dateValue)
    }

    if(start_timeValue === ""){
      date.className = "form-control error"
    }else{
      // timeValidation(dateValue)
    }

}

/**
 * 
 * VALIDATE DATE TO BOOK ON A DATE AHEAD
 */
function dateValidation(dateValue){
  console.log(dateValue)
  const month = parseInt(dateValue.slice(5,7));
  const day = parseInt(dateValue.slice(8,10));
  const year = parseInt(dateValue.slice(0,4));

  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth() + 1;
  const currentDay = currentDate.getDate();

  if(year >= currentYear){
    if(month >= currentMonth){
      if(day >= currentDay){
        console.log("PERFECT");
        setSuccessFor(date)
      }else{
        setErrorFor(date, "Day must be ahead")
      }
    }else{
      setErrorFor(date, "Month must be ahead")
    }
  }else{
    setErrorFor(date, "Year must be ahead")
  }
}

/**
 * 
 * EMAIL FORMAT VALIDATION 
 */
function emailValidation(emailValue){
  const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if(emailValue.match(validRegex)){
    setSuccessFor(email)
  }else{
    document.querySelector(".emailError").innerText = "Enter a valid email"
  }
}


/**
 * 
 * VALIDATE INPUTS LENGTH 
 */
function checkLength(input){

  const userData =  input.getAttribute("id");
  const userDataValue = input.value.trim();

  if(userData == "name" && userDataValue.length <= 2){
    document.querySelector(".nameError").innerText = "Must contain min 3 characters"
  }
  else if(userData == "l_name" && userDataValue.length <= 2){
    document.querySelector(".lastNameError").innerText = "Must contain min 3 characters"
  }
  else if(userData == "phone" && userDataValue.length <=7 || userDataValue.length >=11){
    document.querySelector(".phoneError").innerText = "Must from 8 to 9 numbers"
  }
  else{
    setSuccessFor(input)
  }

}

/**
 * ERROR WARNINGS AN MESSAGES
 */
function setErrorFor(anything, message){
  anything.className = "form-control error"
  document.querySelector(".dateError").innerText = message;
}

/**
 * ERROR WARNING AN MESSAGE FOR BLANK INPUTS
 */
function setErrorForBlank(input, message){
  input.className = "form-control error"
  input.setAttribute("placeholder", message)
}

/**
 * TURNS BORDER INPUT INTO GREEN IF DATA PASSES VALIDATION
 */
function setSuccessFor(input){
  input.className = "form-control success"
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
