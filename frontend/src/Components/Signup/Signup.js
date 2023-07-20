import React from 'react';
import {sha256} from 'js-sha256'

export default function Signup({ onRouteChange, loadUser }) {
    const [signUp, setSignUp] = React.useState({
        signUpName: '',
        signUpEmail: '',
        signUpPassword: ''
    })
    function handleChange(e) {
        const { name, value } = e.target;
        setSignUp(prev => ({ ...prev, [name]: value }))
    }
    function onSubmitSignUp(){
        fetch('/signup', {
            method: 'post',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({
                name: sha256(signUp.signUpName),
                email: sha256(signUp.signUpEmail),
                password: sha256(signUp.signUpPassword),
            })
        })
            .then(response => response.json())
            .then(user => {
                    onRouteChange('signin')
            })
    }
    
    return (
        <article className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5">
            <main className="pa4 black-80 center">
                <div className="measure tc">
                    <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
                        <legend className="f1 fw6 ph0 mh0">Register</legend>
                        <div className="mt3">
                            <label className="db fw6 lh-copy f6" htmlFor="email-address">Name</label>
                            <input
                                className="pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                type="email"
                                name="signUpName"
                                id="email-address"
                                onChange={handleChange}
                            />
                        </div>
                        <div className="mt3">
                            <label className="db fw6 lh-copy f6" htmlFor="email-address">Email</label>
                            <input
                                className="pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                type="email"
                                name="signUpEmail"
                                id="email-address"
                                onChange={handleChange}
                            />
                        </div>
                        <div className="mv3">
                            <label className="db fw6 lh-copy f6" htmlFor="password">Password</label>
                            <input
                                className="b pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                type="password"
                                name="signUpPassword"
                                id="password"
                                onChange={handleChange}
                            />
                        </div>
                    </fieldset>
                    <div className="">
                        <input
                            className="b ph3 pv2 input-reset ba b--black bg-transparent grow pointer f6 dib"
                            type="submit"
                            value="Register"
                            onClick={onSubmitSignUp}
                        />
                    </div>
                    <div className="lh-copy mt3">
                        <p
                            onClick={() => onRouteChange('signin')}
                            className="f6 link dim black db pointer"
                        >
                            {'Sign in'}
                        </p>
                    </div>
                </div>
            </main>
        </article>
    )
}