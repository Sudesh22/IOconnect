import React from "react";
import { FiAlertTriangle } from 'react-icons/fi';
import './Notification.css';

export default function Notification({ baseUrl }) {
    const [notifData, setNotifData] = React.useState({
       title : [],
       desc : [],
       read : [],
       time : [],
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
            const title = data.map((data) => data[1]);
            const desc = data.map((data) => data[0]);
            const read = data.map((data) => data[2]);
            const time = data.map((data) => data[3]);
            
            setNotifData({
              title : title,
              desc : desc,
              read : read,
              time : time,
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
    
        var data = String(notifData.title) + String((notifData.read) ? '*' : '*'); 
    return (
        <div>
            <div className='notification-container'>
                <p>Notifications</p>
            </div>
            <div className='notif-contents'>
                <div>
                    <div className='nf-text'>
                        <div className='nf-icon'>
                            <div >
                                {<FiAlertTriangle style={{ fontSize: '30px' }} />}
                            </div>
                        </div>
                        <div className="nf-title">{data}</div>
                        <div className="nf-desc">{notifData.desc}</div>
                        <div className="nf-date">{notifData.time}</div>
                    </div>
                </div>
            </div>
        </div>
    )
}