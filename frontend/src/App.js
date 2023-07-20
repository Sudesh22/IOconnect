import './App.css';
import React from 'react';
import Signin from './Components/Signin/Signin';
import Signup from './Components/Signup/Signup';
import Particle from './Components/Particles/Particles';
import Home from './Components/Home/Home';

export default function App() {
  const [state, setState] = React.useState({
    route: 'signin',
    isSignedin: false,
    user: {
      id: '',
      name: '',
      email: '',
      joined: ''
    }
  })
  function onRouteChange(route) {
    setState(prev => ({ ...prev, route: route }))
  }
  function loadUser(data) {
    setState(prev => (
      {
        ...prev,
        user:
        {
          id: data[0],
          name: data[1],
          email: data[2],
          joined: data.joined
        }
      }))
  }
  return (
    <div>
      <Particle />
      {state.route === 'home' ?
        <Home onRouteChange={onRouteChange} user={state.user}/>
        :
        <div className='landUpPage'>
          <div className='titles'>
            <h1>Industry</h1>
            <p>Your life is under Our Security......</p>
          </div>
          <div className='container'>
            {state.route === 'signin' ?
              <Signin onRouteChange={onRouteChange} loadUser={loadUser} />
              :
              <Signup onRouteChange={onRouteChange} loadUser={loadUser} />}
          </div>
        </div>
      }
    </div>

  );
}