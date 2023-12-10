import "./Sidebar.css";
import React from "react";
import { SidebarData } from "./Sidebardata";

export default function Sidebar({ onRouteChange, onInternalRouteChange }) {

  function leave() {
    localStorage.removeItem("userProfile");
    onRouteChange("signin")
  }
 
  return (
    <div className="sidebar">
      <div className="title">
        <div className="logo">
          <img className="logoimg" src={`${process.env.PUBLIC_URL}/images/ioconnect.png`} alt="logo" />
        </div>
      </div>
      {SidebarData.map((item, index) => {
        return (
          <ul key={index}>
            {item.title === "Signout" ? (
              <li
                key={index}
                className={item.cName}
                onClick={leave}
              >
                
                <div>
                  {item.icon}
                  <span>{item.title}</span>
                </div>
              </li>
            ) : (
              <li
                key={index}
                className={item.cName}
                onClick={() => onInternalRouteChange(`${item.title}`)}
              >
                <div>
                  {item.icon}
                  <span>{item.title}</span>
                </div>
              </li>
            )}
          </ul>
        );
      })}
    </div>
  );
}
