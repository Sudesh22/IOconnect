import './NewPass.css';
import React from 'react';
import { sha256 } from 'js-sha256';

export default function NewPass({ onRouteChange, loadUser, baseUrl }) {

  const [newPass, setNewPass] = React.useState({
    new_pass : "",
    confirm_pass : "",
  });
  function handleChange(e) {
    const { name, value } = e.target;
    setNewPass((prev) => ({ ...prev, [name]: value }));
  }
  function toggleVisiblity() {
    var x = document.getElementById("new-pass");
    var y = document.getElementById("confirm-pass");
    if (x.type === "password" || y.type === "password") {
      x.type = "text";
      y.type = "text";
    } else {
      x.type = "password";
      y.type = "password";
    }
  }

  function onSubmitNewPass() {
    if ((newPass.new_pass!=="") & (newPass.confirm_pass!=="") &(newPass.new_pass===newPass.confirm_pass)){
    fetch(`${baseUrl}/newPass`, {
      method: "post",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({
        access_token : localStorage.getItem("userProfile"),
        password: sha256(newPass.confirm_pass),
      }),
    })
      .then((response) => response.json())
      .then((user) => {
        onRouteChange("home");
      });
      // console.log();
    }
  }

  return (
    <article
      style={{ backgroundColor: "#1c1b1b" }}
      className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5 center"
    >
      <main className="pa3 black-80 center">
        <div className="measure tc">
          <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
            <legend className="f2 fw6 ph0 mh0 white">Set a new password</legend>
              <div className="mt3">
              <label
                className="db fw5 lh-copy f5 white"
                htmlFor="email-address"
              >
              New Password
              </label>
              <input
                className="pa2 input-reset ba bg-transparent white hover-white w-100"
                type="password"
                name="new_pass"
                id="new-pass"
                onChange={handleChange}
              />
            </div>
            <div className="mv3">
              <label className="db fw5 lh-copy f5 white" htmlFor="password">
              Confirm Password
              </label>
              <input
                className="b pa2 input-reset ba bg-transparent white hover-white w-100"
                type="password"
                name="confirm_pass"
                id="confirm-pass"
                onChange={handleChange}
              />
            </div>
          </fieldset>
          <div>
          <label class="form-control">
            <input type="checkbox" name="checkbox" onClick={toggleVisiblity}/>            Show Password
          </label>
          </div>
          <div className="">
            <input
              className="b ph3 pv1 input-reset ba b--white bg-transparent grow pointer f5 dib white"
              type="submit"
              value="Change my password"
              onClick={onSubmitNewPass}
            />
          </div>
        </div>
      </main>
    </article>
  );
}