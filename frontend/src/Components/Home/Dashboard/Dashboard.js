import "./Dashboard.css";
import Graph from "./Graph/Graph";
import Guage from "./Graph/Gauge";
import React from "react";

export default function Dashboard({ baseUrl }) {
  const [chartData, setChartData] = React.useState({
    deviceStatus: [],
    humidity: [],
    temperature: [],
    Time: [],
  });
  // console.log(localStorage.getItem("userProfile"))

  // fetching the chart data
  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${baseUrl}/dashboard`, {
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
        const deviceStatus = data.map((data) => data[1]);
        const temperature = data.map((data) => data[2]);
        const humidity = data.map((data) => data[3]);
        const Time = data.map((data) => data[4]);
        


        setChartData({
          deviceStatus: deviceStatus,
          humidity: humidity,
          temperature: temperature,
          Time: Time,
        });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    // Fetch data initially
    fetchData();

    // Fetch data every second
    const intervalId = setInterval(fetchData, 5000);

    // Cleaning interval when the component unmounts
    return () => {
      clearInterval(intervalId);
    };
  }, [baseUrl]);

  return (
    <div>
      <p className="dashboard">Dashboard</p>
      <div className="dashboard-status">
        <div className="device-status">
          <p>Status : {chartData.deviceStatus[6]}</p>
        </div>
      </div>
      <div className="all-graph">
        <Guage
          condition={"Temperature"}
          parameter={chartData.temperature[6]}
        />
        <Guage condition={"Humidity"} parameter={chartData.humidity[6]} />
        <Graph condition={"Temperature"} chartData={chartData} />
        <Graph condition={"Humidity"} chartData={chartData} />
        <p className="text" >Average Temperature: {(parseInt(chartData.temperature[0])+parseInt(chartData.temperature[1])+parseInt(chartData.temperature[2])+parseInt(chartData.temperature[3])+parseInt(chartData.temperature[4])+parseInt(chartData.temperature[5])+parseInt(chartData.temperature[6]))/7}</p>
        <p className="text" >Average Humidity: {(parseInt(chartData.humidity[0])+parseInt(chartData.humidity[1])+parseInt(chartData.humidity[2])+parseInt(chartData.humidity[3])+parseInt(chartData.humidity[4])+parseInt(chartData.humidity[5])+parseInt(chartData.humidity[6]))/7}</p>
        <p className="text" >Last 5 Readings: </p>
        <p className="text" >Last 5 Readings: </p>
        <p className="text" >{chartData.temperature[0]}</p>
        <p className="text" >{chartData.humidity[0]}</p>
        <p className="text" >{chartData.temperature[1]}</p>
        <p className="text" >{chartData.humidity[1]}</p>
        <p className="text" >{chartData.temperature[2]}</p>
        <p className="text" >{chartData.humidity[2]}</p>
        <p className="text" >{chartData.temperature[3]}</p>
        <p className="text" >{chartData.humidity[3]}</p>
        <p className="text" >{chartData.temperature[4]}</p>
        <p className="text" >{chartData.humidity[4]}</p>
        

      </div>
    </div>
  );
}
