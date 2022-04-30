
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
    if (!form.checkValidity()) {

  event.preventDefault();
  event.stopPropagation()
  validateInputs(event)
}
},false)
}

/**
* GET INPUTS VALUE AND CHECK BLANK FIELDS
**/
function validateInputs(event){
  // get the values from inputs
  const nameValue = fname.value.trim()
  const lastNameValue = surname.value.trim()
  const prefixValue = prefix.value.trim()
  const phoneValue = phone.value.trim()
  const emailValue = email.value.trim()
  const dateValue = date.value.trim()
  const start_timeValue = document.querySelector("#start_time").value.toString();
  const party_sizeValue =party_size.value.trim()

  let time = document.querySelector("#start_time");

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
    // console.log(start_timeValue );
    if(start_timeValue === ""){
      start_time.className = "form-control error"
      document.querySelector(".timeError").innerText = "Please select a valid time slot"
    }
    else{
      setSuccessFor(start_time)
    }

    if(party_sizeValue === ""){
      setErrorForBlank(party_size, "Select party size");
    }else{
      checkPartySize(party_sizeValue)
    }

    if(prefixValue != ""){
        setSuccessFor(prefix)
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
      setSuccessFor(date)
    }else{
      setErrorForDate(date, "Month must be ahead")
    }
  }else{
    setErrorForDate(date, "Year must be ahead")
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
  const nameValue = fname.value.trim()
  const lastNameValue = surname.value.trim()
  // const prefixValue = prefix.value.trim()
  const phoneValue = phone.value.trim()
  const emailValue = email.value.trim()
  const dateValue = date.value.trim()
  const start_timeValue = document.querySelector("#start_time").value.trim();
  const party_sizeValue =party_size.value.trim()

  if(userData == "name" && nameValue.length <= 2){
    fname.className = "form-control error"
    document.querySelector(".nameError").innerText = "Must contain min 3 characters"
  }
  else if(userData == "l_name" && lastNameValue.length <= 2){
    surname.className = "form-control error"
    document.querySelector(".lastNameError").innerText = "Must contain min 3 characters"
  }
  else if(userData == "phone" && phoneValue.length <=7 || phoneValue.length >=11){
    phone.className = "form-control error"
    document.querySelector(".phoneError").innerText = "Must have from 8 to 9 numbers"
  }
  // else if(userData == "start_time"){
  //   start_time.className = "form-control error"
  //   document.querySelector(".timeError").innerText = "Please select a valid time slot"
  // }
  else{
    setSuccessFor(input)
  }
}

/**
 * ERROR MESSAGES FOR INCORRECT DATE
 */
function setErrorForDate(bookingDate, message){
  bookingDate.className = "form-control error"
  document.querySelector(".dateError").innerText = message;
}

/**
 * ERROR MESSAGES FOR INCORRECT PARTY SIZE
 */
function checkPartySize(party_sizeValue){
  const minos = "-";

  if(party_sizeValue >= 13){
    party_size.className = "form-control error"
    document.querySelector(".partyError").innerText = "For parties over 12px contact us";
  }
  else if(party_sizeValue.match(minos) || party_sizeValue === "0"){
    party_size.className = "form-control error"
    document.querySelector(".partyError").innerText = "Please select a valid party size";
  }
  else{
    setSuccessFor(party_size)
  }
  
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


