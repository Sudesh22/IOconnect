import React from "react";
import { FiAlertTriangle } from 'react-icons/fi';
import { CiUser } from "react-icons/ci";
import { MdOutlineCelebration } from "react-icons/md";
import { TbPlugConnected } from "react-icons/tb";
import './Notification.css';

export default function Notification({ baseUrl }) {
    const [notifData, setNotifData] = React.useState({
      //  title : [],
      //  desc : [],
      //  read : [],
      //  time : [],
      data: []
      });
      // console.log(localStorage.getItem("userProfile"))
    
      // fetching the chart data
      React.useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(`${baseUrl}/notif`, {
              method: "post",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                access_token : localStorage.getItem("userProfile"),
              }),
            });
            const responseData = await response.json();
            const data = responseData.reverse();
            console.log(data);  
            // const title = data.map((data) => data[1]);
            // const desc = data.map((data) => data[0]);
            // const read = data.map((data) => data[2]);
            // const time = data.map((data) => data[3]);
            
            setNotifData({
              // title : title,
              // desc : desc,
              // read : read,
              // time : time,
              data: data
            });
          } catch (error) {
            console.error("Error fetching data:", error);
          }
        };
        // Fetch data initially
        fetchData();
    
        // Fetch data every second
        const intervalId = setInterval(fetchData, 30000);
    
        // Cleaning interval when the component unmounts
        return () => {
          clearInterval(intervalId);
        };
      }, [baseUrl]); 

      const renderSwitch = (param)=> {
        console.log(param)
        switch(param) {
          case 'alert':
            return <FiAlertTriangle style={{ fontSize: '30px' }} />;
          case 'promotion':
            return <MdOutlineCelebration style={{ fontSize: '30px' }} />;
          case 'signIn':
            return <CiUser style={{ fontSize: '30px' }} />;
          case 'action':
            return <TbPlugConnected style={{ fontSize: '30px' }} />;
          default:
            return <FiAlertTriangle style={{ fontSize: '30px' }} />;
        }
      }

      const component = notifData.data.map(parameter => 
        <div>     
          <div className='nf-text'>
              <div className='nf-icon'>
                  <div >
                      {renderSwitch(parameter[4])}
                  </div>
              </div>
              <div className="nf-title">{parameter[1]}</div>
              <div className="nf-desc">{parameter[0]}</div>
              <div className="nf-date">{parameter[3]}</div>
          </div>
      </div>
    
      )
    
        var data = String(notifData.title) + String((notifData.read) ? '*' : '*'); 
    return (
        <div>
            <div className='notification-container'>
                <p>Notifications</p>
            </div>
            <div className='notif-contents'>
                {component}
            </div>
        </div>
    )
}