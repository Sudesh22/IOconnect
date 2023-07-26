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

  // fetching the chart data
  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${baseUrl}/dashboard`, {
          method: "post",
          headers: {
            "Content-Type": "application/json",
          },
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
        <Graph condition={"Temperature"} chartData={chartData} />
        <Graph condition={"Humidity"} chartData={chartData} />
        <Guage
          condition={"Temperature℃"}
          parameter={chartData.temperature[6]}
        />
        <Guage condition={"Humidity"} parameter={chartData.humidity[6]} />
      </div>
    </div>
  );
}
