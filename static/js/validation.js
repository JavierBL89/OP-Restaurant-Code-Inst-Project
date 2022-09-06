//jshint esversion:6

const form = document.getElementById('booking_form');

let fname = document.getElementById("id_name");
let surname = document.getElementById("id_last_name");
let prefix = document.getElementById("id_prefix");
let phone = document.getElementById("id_phone");
let email = document.getElementById("id_email");
let date = document.getElementById("date");
let start_time = document.getElementById("id_start_time");
let party_size = document.getElementById("id_party_size");
let booking_comments = document.getElementById("id_excerpt");
const opening_days = [2,3,4,5,6];


/**
* INITIALIZE FORM VALIDATION
**/
form.addEventListener('submit', event => {
      validateInputs();
      let count = $(".success");
      console.log(count.length);
      if(count.length >= 8){
        console.log('VALID');
        form.submit();
      }else{
        event.preventDefault();
        event.stopPropagation();
        console.log('NO VALID');     
      }
},false);

/**
* GET INPUTS VALUE AND CHECK BLANK FIELDS
**/
function validateInputs(){

  // get the values from inputs
  const nameValue = fname.value.trim();
  const lastNameValue = surname.value.trim();
  const prefixValue = prefix.value.trim();
  const phoneValue = phone.value.trim();
  const emailValue = email.value.trim();
  const dateValue = date.value.trim();
  const start_timeValue = document.querySelector("#id_start_time").value.toString();
  const party_sizeValue =party_size.value.trim();

  $(".form-control error").css("border-color", "black;")

    if(nameValue === ""){
      setErrorForBlank(fname, "Field cannot be blank");
    }else{
      checkLength(fname);
    }

    if(lastNameValue === ""){
      console.log('bitch');
      setErrorForBlank(surname, "Field cannot be blank");
    }else{
      checkAlphanumerics(surname);
      checkLength(surname);
    }

    if(phoneValue === ""){
      setErrorForBlank(phone, "Field cannot be blank");
    }else{
      checkLength(phone);
    }

    if(emailValue === ""){
      setErrorForBlank(email, "Field cannot be blank");
    }else{
      emailValidation(emailValue);
    }

    if(dateValue === ""){
      date.className = "form-control error";
    }else{
      dateValidation(dateValue);
    }

    if(prefixValue != ""){
        setSuccessFor(prefix);
    }

    if(start_timeValue > '0'){
      setSuccessFor(start_time);
    }else{
      start_time.className = "form-control error";
      document.querySelector(".timeError").innerText = "Please, select a valid time";
    }
    
    if(party_sizeValue === ""){
      setErrorForBlank(party_size, "Select party size");
    }else if(party_sizeValue < 1 || party_sizeValue >= 13){
      party_size.className = "form-control error";
      document.querySelector(".partySizeError").innerText = "Must enter a number over 0 or under 13";
    }else{
      checkAlphanumerics(party_size);
    }
}

/**
 * 
 * VALIDATE NAME AND SURNAME USERS FORTMAT
 */
function checkAlphanumerics(input){
  let letters = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/g;
  let numbers =  /^[0-9]*$/g;

  let input_id = input.getAttribute("id");
    if(input_id == "id_name"){
      let inputValue = fname.value;
      if(inputValue.match(letters)){
        setSuccessFor(fname);
      }else{
        fname.className = "form-control error";
        document.querySelector(".nameError").innerText = "Only alphabet characters allowed";
      }
    }
    if(input_id == "id_last_name"){
      let inputValue = surname.value;
      if(inputValue.match(letters)){
        setSuccessFor(surname);
      }else{
        surname.className = "form-control error";
        document.querySelector(".lastNameError").innerText = "Only alphabet characters allowed";
      }
    }
    if(input_id == "id_phone"){
      let inputValue = phone.value;
      if(inputValue.match(numbers)){
        setSuccessFor(phone);
      }else{
        phone.className = "form-control error";
        document.querySelector(".phoneError").innerText = "Only numbers allowed";
      }
    }
    if(input_id == "id_party_size"){
      let inputValue = party_size.value;
      if(inputValue.match(numbers)){
        setSuccessFor(party_size);
      }else{
        party_size.className = "form-control error";
        document.querySelector(".partySizeError").innerText = "Only numbers allowed";
      }
    }
}

/**
 * 
 * VALIDATE DATE TO BOOK ON A DATE AHEAD
 */
function dateValidation(dateValue){
  const dayOfWeek =  new Date(dateValue).getDay();
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
        if(opening_days.includes(dayOfWeek)){
          setSuccessFor(date);
        }else{
          setErrorForDate(date, "Opening days from Tuesday to Saturday included");
        }
      }else{
        setErrorForDate(date, "Day must be from today onwards");
      }  
    }else{
      setErrorForDate(date, "Month must be ahead");
    }
  }else{
    setErrorForDate(date, "Year must be ahead");
  }
}

/**
 * 
 * EMAIL FORMAT VALIDATION 
 */
function emailValidation(emailValue){
  const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if(emailValue.match(validRegex)){
    setSuccessFor(email);
  }else{
    document.querySelector(".emailError").innerText = "Enter a valid email";
  }
}

/**
 * 
 * VALIDATE INPUTS LENGTH 
 */
function checkLength(input){
  const input_id =  input.getAttribute("id");
  const nameValue = fname.value.trim();
  const lastNameValue = surname.value.trim();
  const phoneValue = phone.value.trim();

  if(input_id == "id_name" && nameValue.length <= 2){
    fname.className = "form-control error";
    document.querySelector(".nameError").innerText = "Must contain min 3 characters";
  }else{
    checkAlphanumerics(fname);
  }

  if(input_id == "id_last_name" && lastNameValue.length <= 2){
    surname.className = "form-control error";
    document.querySelector(".lastNameError").innerText = "Must contain min 3 characters";
  }
  else{
    checkAlphanumerics(surname);
  }

  if(input_id == "id_phone" && phoneValue.length <=7 || phoneValue.length >10){
    phone.className = "form-control error";
    document.querySelector(".phoneError").innerText = "Must have from 8 to 9 numbers";

  }else{
    checkAlphanumerics(phone);
  }
}

/**
 * ERROR MESSAGES FOR INCORRECT DATE
 */
function setErrorForDate(bookingDate, message){
  bookingDate.className = "form-control error";
  document.querySelector(".dateError").innerText = message;
}

/**
 * ERROR WARNING AN MESSAGE FOR BLANK INPUTS
 */
function setErrorForBlank(input, message){
  input.className = "form-control error";
  input.setAttribute("placeholder", message);
  return false
}

/**
 * TURNS BORDER INPUT INTO GREEN IF DATA PASSES VALIDATION
 */
function setSuccessFor(input){
  input.className = "form-control success";  
  return true
}
