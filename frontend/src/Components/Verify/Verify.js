import './Verify.css';
import React from 'react';

export default function Verify({ onRouteChange, loadUser, baseUrl }) {
  // function handleChange(e) {
  //   const { name, value } = e.target;
  //   setVerify((prev) => ({ ...prev, [name]: value }));
  // }
  let inputCount = 0, finalInput = "";
  function enableInput(){
    const input = document.querySelectorAll(".input");
    const inputField = document.querySelector(".inputfield");
    const submitButton = document.getElementById("submit");
    //Initial references

    //Update input
    const updateInputConfig = (element, disabledStatus) => {
      element.disabled = disabledStatus;
      if (!disabledStatus) {
        element.focus();
      } else {
        element.blur();
      }
    };

    input.forEach((element) => {
      element.addEventListener("keyup", (e) => {
        e.target.value = e.target.value.replace(/[^0-9]/g, "");
        let { value } = e.target;

        if (value.length == 1) {
          updateInputConfig(e.target, true);
          if (inputCount <= 3 && e.key != "Backspace") {
            finalInput += value;
            if (inputCount < 3) {
              updateInputConfig(e.target.nextElementSibling, false);
            }
          }
          inputCount += 1;
        } else if (value.length == 0 && e.key == "Backspace") {
          finalInput = finalInput.substring(0, finalInput.length - 1);
          if (inputCount == 0) {
            updateInputConfig(e.target, false);
            return false;
          }
          updateInputConfig(e.target, true);
          e.target.previousElementSibling.value = "";
          updateInputConfig(e.target.previousElementSibling, false);
          inputCount -= 1;
        } else if (value.length > 1) {
          e.target.value = value.split("")[0];
        }
        submitButton.classList.add("hide");
      });
    });

    window.addEventListener("keyup", (e) => {
      if (inputCount > 3) {
        submitButton.classList.remove("hide");
        submitButton.classList.add("show");
        if (e.key == "Backspace") {
          finalInput = finalInput.substring(0, finalInput.length - 1);
          updateInputConfig(inputField.lastElementChild, false);
          inputField.lastElementChild.value = "";
          inputCount -= 1;
          submitButton.classList.add("hide");
        }
      }
    });

    const validateOTP = () => {
      alert("Success");
    };

    //Start
    const startInput = () => {
      inputCount = 0;
      finalInput = "";
      input.forEach((element) => {
        element.value = "";
      });
      updateInputConfig(inputField.firstElementChild, false);
    };

    window.onload = startInput();

  }

  function onSubmitVerify() {
    fetch(`${baseUrl}/getOtp`, {
      method: "post",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({
        access_token: localStorage.getItem("userProfile"),
        otp : finalInput,
      }),
    })
      .then((response) => response.json())
      .then((user) => {
          console.log(user)
          loadUser(user);
          if (user.Status === "Success"){
            onRouteChange("NewPass"); 
          }
          else{
            console.log("otp expired!!")
          }
            
      });
    console.log(finalInput);
  }

  return (
        <div className="measure tc">
          <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
              <div className="mt3">
                
                {/* <input
                  className="pa2 input-reset ba bg-transparent white hover-white w-100"
                  type="text"
                  name="otp"
                  id="verification-code"
                  onChange={handleChange}
                /> */}
                 <div class="container" onClick={enableInput}>
            <legend className="f2 fw6 ph0 mh0 white center">OTP Verification</legend>
            <label
                  className="db fw5 lh-copy f5 white"
                  htmlFor="verification-code"
                >
                  An otp has been sent to your registered email address
                </label>
                {/* <p class="msg">Please enter OTP to verify</p> */}
                <div class="inputfield">
                  <input id ="1" type="number" maxlength="1" class="input"/>
                  <input id ="2" type="number" maxlength="1" class="input"/>
                  <input id ="3" type="number" maxlength="1" class="input"/>
                  <input id ="4" type="number" maxlength="1" class="input"/>
                </div>
                <button  class="hide" id="submit" onClick={onSubmitVerify}>Submit</button>
              </div>
              </div>
          </fieldset>
          <div className="">
            {/* <input
              className="b ph3 pv1 input-reset ba b--white bg-transparent grow pointer f6 dib white"
              type="submit"
              value="Submit"
              onClick={onSubmitVerify}
            /> */}
          </div>
        </div>
      
  );
}
