import './Verify.css';
import React, { useState } from 'react';
import OtpInput from 'react-otp-input';

export default function Verify({ onRouteChange, loadUser, baseUrl }) {
  const [otp, setOtp] = useState(new Array(6).fill(""));
  // function handleChange(e) {
  //   const { name, value } = e.target;
  //   setVerify((prev) => ({ ...prev, [name]: value }));
  // }
  function onSubmitVerify() {
    fetch(`${baseUrl}/verify`, {
      method: "post",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({
        "jhg":"jhgf"
      }),
    })
      .then((response) => response.json())
      .then((user) => {
        
          console.log(user)
          loadUser(user);
          onRouteChange("Dashboard");
        
      });
  }

  return (
    <article
      style={{ backgroundColor: "#1c1b1b" }}
      className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5 center"
    >
      <main className="pa3 black-80 center">
        <div className="measure tc">
          <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
            <legend className="f1 fw6 ph0 mh0 white">OTP Verification</legend>
              <div className="mt3">
                <label
                  className="db fw5 lh-copy f5 white"
                  htmlFor="verification-code"
                >
                  An otp has been sent to your registered email address
                </label>
                <p class="msg">Please enter OTP to verify</p>
                {/* <input
                  className="pa2 input-reset ba bg-transparent white hover-white w-100"
                  type="text"
                  name="otp"
                  id="verification-code"
                  onChange={handleChange}
                /> */}
                <div class="otp-input-fields">
                  <p></p>
                  <OtpInput
      value={otp}
      onChange={setOtp}
      numInputs={4}
      renderSeparator={<span>-</span>}
      renderInput={(props) => <input {...props} />}
    />
                </div>
              </div>
          </fieldset>
          <div className="">
            <input
              className="b ph3 pv1 input-reset ba b--white bg-transparent grow pointer f6 dib white"
              type="submit"
              value="Submit"
              onClick={onSubmitVerify}
            />
          </div>
        </div>
      </main>
    </article>
  );
}
