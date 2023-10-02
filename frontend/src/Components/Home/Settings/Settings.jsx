import './Settings.css';
import React from "react";
import * as FaIcons from 'react-icons/fa';
import * as BaIcons from 'react-icons/bi'

export default function Settings({ onRouteChange, baseUrl }){

    // const [setting, setSetting] = React.useState({
    //     signUpName: "",
    //     signUpEmail: "",
    //     signUpPassword: "",
    // });
      function changePass(e) {
        fetch(`${baseUrl}/changePass`, {
            method: "post",
            headers: { "Content-type": "application/json" },
            body: JSON.stringify({
                access_token : localStorage.getItem("userProfile")
            }),
          })
            .then((response) => response.json())
            .then((user) => {
                onRouteChange("verify");
            });
      }

      function getDevices(e) {
        fetch(`${baseUrl}/getDevices`, {
            method: "post",
            headers: { "Content-type": "application/json" },
            body: JSON.stringify({
                access_token : localStorage.getItem("userProfile")
            }),
          })
            .then((response) => response.json())
            .then((user) => {
                onRouteChange("devices");
            });
      }

    return(
        <div className='setting-container'>
           <p>Settings</p> 
           <div className='holder'>
                <div className="option" onClick={changePass}>
                    <div className='title'>
                        <div className='icon'>
                            <FaIcons.FaUserLock />
                        <span > Change Password</span> 
                        </div>
                    </div>
                </div>
           </div>
            <div className='holder'>
                <div className="option" onClick={getDevices}>
                    <div className='title'>
                        <div className='icon'>
                            <BaIcons.BiShapeCircle />
                        <span > Deployed Devices</span> 
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}