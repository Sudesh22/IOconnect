import React from 'react';

export default function Signin({ onRouteChange,loadUser }) {
    const [signIn, setSignIn] = React.useState({
        signInEmail: '',
        signInPassword: ''
    })
    // function encrypt(email, password) {
    //     var encrypted = CryptoJS.AES.encrypt(
    //         document.getElementById("email-address").value,
    //         document.getElementById("password").value
    //      );
    //      return encrypted
    //   }
    function handleChange(e) {
        const { name, value } = e.target;
        setSignIn(prev => ({ ...prev, [name]: value }))
    }
    function onSubmitSignIn(){
        fetch('/signin', {
            method: 'post',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({
                email: signIn.signInEmail,
                password: signIn.signInPassword
            })
        })
            .then(response => response.json())
            .then(user => {
                if (user[0][0]) {
                    loadUser(user[0]);
                    onRouteChange('home')
                }
            })
            .catch(err => console.log(err))
    }
    return (
        <article className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5">
            <main className="pa4 black-80 center">
                <div className="measure tc">
                    <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
                        <legend className="f1 fw6 ph0 mh0">Sign In</legend>
                        <div className="mt3">
                            <label className="db fw6 lh-copy f6" htmlFor="email-address">Email</label>
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js" integrity="sha256-/H4YS+7aYb9kJ5OKhFYPUjSJdrtV6AeyJOtTkw6X72o=" crossorigin="anonymous"></script>
                            <input
                                className="pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                type="email"
                                name="signInEmail"
                                id="email-address"
                                onChange={handleChange}
                            />
                        </div>
                        <div className="mv3">
                            <label className="db fw6 lh-copy f6" htmlFor="password">Password</label>
                            <input
                                className="b pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                type="password"
                                name="signInPassword"
                                id="password"
                                onChange={handleChange}
                            />
                        </div>
                    </fieldset>
                    <div className="">
                        <input
                            className="b ph3 pv2 input-reset ba b--black bg-transparent grow pointer f6 dib"
                            type="submit"
                            value="Sign in"
                        // onSubmit={this.onSubmitSignIn}
                        onClick={onSubmitSignIn} 
                        />
                    </div>
                    <div className="lh-copy mt3">
                        <p
                            onClick={() => onRouteChange('register')}
                            className="f6 link dim black db pointer"
                        >
                            {'Register'}
                        </p>
                    </div>
                </div>
            </main>
        </article>
    )
}