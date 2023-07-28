import React from "react";

export default function Verify({ onRouteChange, loadUser, baseUrl }) {
  const [verify, setVerify] = React.useState({
    otp : ""
  });
  function handleChange(e) {
    const { name, value } = e.target;
    setVerify((prev) => ({ ...prev, [name]: value }));
  }
  function onSubmitVerify() {
    fetch(`${baseUrl}/verify`, {
      method: "post",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({
        otp: verify.otp,
      }),
    })
      .then((response) => response.json())
      .then((user) => {
        
          console.log(user)
          loadUser(user);
          onRouteChange("signin");
        
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
            <legend className="f1 fw6 ph0 mh0 white">Verification Code</legend>
              <div className="mt3">
                <label
                  className="db fw5 lh-copy f5 white"
                  htmlFor="verification-code"
                >
                  Enter the 6-digit code received on your Email address
                </label>
                <input
                  className="pa2 input-reset ba bg-transparent white hover-white w-100"
                  type="text"
                  name="otp"
                  id="verification-code"
                  onChange={handleChange}
                />
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
