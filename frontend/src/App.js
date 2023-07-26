import "./App.css";
import React from "react";
import Signin from "./Components/Signin/Signin";
import Signup from "./Components/Signup/Signup";
import Particle from "./Components/Particles/Particles";
import Home from "./Components/Home/Home";

export default function App() {
  const baseUrl = "http://192.168.0.106:5000";

  const [state, setState] = React.useState({
    route: "signin",
    isSignedin: false,
    user: {
      id: "",
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
        id: data[0],
        name: data[1],
        email: data[2],
      },
    }));
  }
  return (
    <div className="app">
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
  );
}
