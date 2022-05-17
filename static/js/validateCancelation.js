

const form = document.getElementById("cancelation_form")
const email = document.getElementById("email")
const phone = document.getElementById("phone")
const date = document.getElementById("date");


/**
* INITIALIZE FORM VALIDATION
**/
function handleSubmitCancelation(event){

    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation()
      validateInputs(event)

    }

    },false)
    }


function validateInputs(event){
    console.log("putaa");

    const emailValue = document.getElementById("email").value.trim()
    const phoneValue = document.getElementById("phone").value.trim()
    const dateValue = date.value.trim()

    if(emailValue === ""){
        setErrorForBlank(email, "Field cannot be blank");
      }else{
        validateEmail(emailValue)
      }

      if(phoneValue === ""){
        setErrorForBlank(phone, "Field cannot be blank");
      }else{
        checkLength(phoneValue)
      }

      if(dateValue === ""){
        date.className = "cancelation-input error"
      }else{
        dateValidation(dateValue)
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
      document.querySelector(".cancelationEmailError").innerText = "Enter a valid email"
    }
  }



  function checkLength(input){

    const userData =  input.getAttribute("id");
    const phoneValue = phone.value.trim()
    const emailValue = email.value.trim()
    
     if(userData == "phone" && phoneValue.length <=7 || phoneValue.length >=9){
      phone.className = "form-control error"
      document.querySelector("cancelation-form .phoneError").innerText = "Must have from 8 to 9 numbers"
    }else{
        setSuccessFor(input)
      }

}


/**
 * 
 * VALIDATE DATE TO BOOK ON A DATE AHEAD
 */
function dateValidation(dateValue){
    const currentDate =  new Date().now()
    console.log(currentDate);
   
    if(dateValue > currentDate){
      console.log(date);
      console.log(currentDate);
    }else{
        console.log("puta");
    }
  }

/**
 * ERROR WARNING AN MESSAGE FOR BLANK INPUTS
 */
 function setErrorForBlank(input, message){
    input.className = "cancelation-input error"
    input.setAttribute("placeholder", message)
  }

  
  /**
 * TURNS BORDER INPUT INTO GREEN IF DATA PASSES VALIDATION
 */
function setSuccessFor(input){
    input.className = "cancelation-input success"
  }