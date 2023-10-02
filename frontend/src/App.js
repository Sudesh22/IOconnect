import "./App.css";
import React from "react";
import Signin from "./Components/Signin/Signin";
import Signup from "./Components/Signup/Signup";
import Particle from "./Components/Particles/Particles";
import Home from "./Components/Home/Home";
import Verify from "./Components/Verify/Verify";
import NewPass from "./Components/NewPass/NewPass";

export default function App() {
    const baseUrl = "http://192.168.0.106:8081";

  const [state, setState] = React.useState({
    route: "signin",
    isSignedin: false,
    user: {
      name: "",
      email: "",
    },
  });
  function onRouteChange(route) {
    setState((prev) => ({ ...prev, route: route }));
  }
  function loadUser(data) {
    setState((prev) => ({
      ...prev,
      user: {
        name: data[0],
        email: data[1],
      },
    }));
  }
  return (
    <div className="app">
      {state.route === "NewPass" ? (
          <NewPass
            onRouteChange={onRouteChange}
            user={state.user}
            loadUser={loadUser}
            baseUrl={baseUrl}
          />
        ) : (
          <div>
      {state.route === "verify" ? (
          <Verify
            onRouteChange={onRouteChange}
            user={state.user}
            loadUser={loadUser}
            baseUrl={baseUrl}
          />
        ) : (
      <div>
        {state.route === "home" ? (
          <Home
            onRouteChange={onRouteChange}
            user={state.user}
            baseUrl={baseUrl}
          />
        ) : (
          <div>
            <Particle />
            {state.route === "signin" ? (
              <Signin
                onRouteChange={onRouteChange}
                loadUser={loadUser}
                baseUrl={baseUrl}
              />
            ) : (
              <Signup
                onRouteChange={onRouteChange}
                loadUser={loadUser}
                baseUrl={baseUrl}
              />
            )}
          </div>
        )}
      </div>
      )}
      </div>
        )
    }
    </div>
  );
}
