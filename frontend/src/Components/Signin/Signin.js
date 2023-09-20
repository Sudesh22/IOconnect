import React from "react";
import {sha256} from 'js-sha256'
import CryptoJS from "crypto-js";

const secretPass = "XkhZG4fW2t2W";

export default function Signin({ onRouteChange, loadUser, baseUrl }) {
  const [signIn, setSignIn] = React.useState({
    isError: false,
    errorMessage: "",
    signInEmail: "",
    signInPassword: "",
  });
  function handleChange(e) {
    const { name, value } = e.target;
    setSignIn((prev) => ({ ...prev, [name]: value }));
  }
  function onSubmitSignIn() {
    fetch(`${baseUrl}/signin`, {
      method: "post",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({
        email: signIn.signInEmail,
        password: sha256(signIn.signInPassword),
      }),
    })
      .then((response) => response.json())
      .then((user) => {
        console.log(user)
        loadUser(user);
        onRouteChange("home");
      })
      .catch((err) => {
        setSignIn((prev) => ({
          ...prev,
          errorMessage: "Bad Credentials!",
          isError: true,
        }));
        console.log(err);
      });
  }
  return (
    <article
      style={{ backgroundColor: "#1c1b1b" }}
      className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5 center"
    >
      {/* <py-script>
        import asyncio
        import json
        from request import request  # import our request function.

        async def main():
            baseurl = "https://jsonplaceholder.typicode.com"

            # GET
            headers = {"Content-type"}
            response = await request(f"{baseUrl}/posts/2", method="GET", headers=headers)
            print(f"GET request= status:{response.status}, json:{await response.json()}")

            # POST
            body = json.dumps({"title"})
            new_post = await request(f"{baseUrl}/posts", body=body, method="POST", headers=headers)
            print(f"POST request= status:{new_post.status}, json:{await new_post.json()}")

            # PUT
            body = json.dumps({"id"})
            new_post = await request(f"{baseUrl}/posts/1", body=body, method="PUT", headers=headers)
            print(f"PUT request= status:{new_post.status}, json:{await new_post.json()}")

            # DELETE
            new_post = await request(f"{baseUrl}/posts/1", method="DELETE", headers=headers)
            print(f"DELETE request= status:{new_post.status}, json:{await new_post.json()}")

        asyncio.ensure_future(main())
    </py-script>  */}
      <main className="pa3 black-80 center">
        <div className="measure tc">
          <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
            <legend className="f1 fw6 ph0 mh0 white">Sign In</legend>
            <div>
              {signIn.isError ? (
                <p className="red">{signIn.errorMessage}</p>
              ) : (
                <p>{signIn.errorMessage}</p>
              )}
            </div>

            <div className="mt3">
              <label
                className="db fw5 lh-copy f5 white"
                htmlFor="email-address"
              >
                Email
              </label>
              <input
                className="pa2 input-reset ba bg-transparent white hover-white w-100"
                type="email"
                name="signInEmail"
                id="email-address"
                onChange={handleChange}
              />
            </div>
            <div className="mv3">
              <label className="db fw5 lh-copy f5 white" htmlFor="password">
                Password
              </label>
              <input
                className="b pa2 input-reset ba bg-transparent white hover-white w-100"
                type="password"
                name="signInPassword"
                id="password"
                onChange={handleChange}
              />
            </div>
          </fieldset>
          <div className="">
            <input
              className="b ph3 pv1 input-reset ba b--white bg-transparent grow pointer f6 dib white"
              type="submit"
              value="Sign in"
              onClick={onSubmitSignIn}
            />
          </div>
          <div className="lh-copy mt3">
            <p
              onClick={() => onRouteChange("register")}
              className="f6 link dim black db pointer white"
            >
              {"Register"}
            </p>
          </div>
        </div>
      </main>
    </article>
  );
}
