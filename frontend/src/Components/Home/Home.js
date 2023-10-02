import React from "react";
import "./Home.css";
import Sidebar from "./Sidebar/Sidebar";
import Dashboard from "./Dashboard/Dashboard";
import Team from "./Teams/Team";
import HomeContent from "./HomeContent/HomeContent";
import Notification from "./Notification/Notification";
import Settings from "./Settings/Settings";
import Analytics from "./Analytics/Analytics"

export default function Home({ onRouteChange, user, baseUrl }) {
  const [internalroute, setInternalRoute] = React.useState("Dashboard");

  function onInternalRouteChange(internalroute) {
    setInternalRoute(internalroute);
  }

  function mainContent() {
    if (internalroute === "Home") {
      return <HomeContent />;
    } else if (internalroute === "Dashboard") {
      return <Dashboard baseUrl={baseUrl} />;
    } else if (internalroute === "Team") {
      return <Team />;
    } else if (internalroute === "Settings") {
      return <Settings 
                onRouteChange={onRouteChange} 
                baseUrl={baseUrl}
              />;
    } else if (internalroute === "Notification") {
      return <Notification />;
    } else if (internalroute === "Analytics") {
      return <Analytics />;
    }
  }
  return (
    <div>
      <div className="flex">
        <div className="w-20">
          <Sidebar
            onRouteChange={onRouteChange}
            onInternalRouteChange={onInternalRouteChange}
          />
        </div>
        <div className="w-80 bg-custom pa4 pt2 ma3 br3">
          <main className="">{mainContent()}</main>
        </div>
      </div>
    </div>
  );
}
