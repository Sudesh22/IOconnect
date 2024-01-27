import "./Graph.css";

// import React, { useState, useEffect } from 'react'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

function getClassName(condition) {
  let className = "";
  if (condition === "Temperature1") {
    className = "red";
  } else if (condition === "Temperature2") {
    className = "green";
  }
  return className;
}

function getYAxisData(condition, chartData) {
  let data = "";
  if (condition === "Temperature1") {
    data = chartData.temperature1;
  } else if (condition === "Temperature2") {
    data = chartData.temperature2;
  } else if (condition === "Humidity") {
    data = chartData.humidity;
  }
  return data;
}

// function splitDateTime(dateTime) {
//   return dateTime.split(" ");
//   //   dateTime.split(/(\s+)/)
// }
function getXAxisData(chartData,timeframe) {
  var timeOnlyArray;
  console.log(timeframe)
  if (timeframe==="Weekly"){

    timeOnlyArray = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  }
  if (timeframe === "Monthly"){
    timeOnlyArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
  }
  if (timeframe === "Yearly"){
    // timeOnlyArray = [1,2,3,4,5,6,7,8,9,10,11,12]
  }
  return timeOnlyArray;
}
const Graph = ({ condition, chartData, timeframe }) => {
  const x_axis = getXAxisData(chartData,timeframe);
  const y_axis = getYAxisData(condition, chartData);

  var data = {
    labels: x_axis,
    datasets: [
      {
        label: `${condition}`,
        data: y_axis,
        pointStyle: 'rectRot',
        pointBorderColor : 'white',
        pointBorderWidth : 0.9,
        pointRadius : 4,
        backgroundColor: [
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
        ],
        borderColor: [
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
          `${getClassName(condition)}`,
        ],
        borderWidth: 2,
      },
    ],
  };

  var options = {
    maintainAspectRatio: false,
    scales: {
      y: {
        grid: {
          color: "rgba(256,256,256,0.1)",
          borderColor: "rgba(256,256,256,0.7)",
        },
        ticks: {
          color: "rgba(256,256,256,0.8)",
          font: {
            size: 10,
          },
        },
      },
      x: {
        grid: {
          color: "rgba(256,256,256,0.1)",
          borderColor: "rgba(256,256,256,0.7)",
        },
        ticks: {
          color: "rgba(256,256,256,0.8)",
          font: {
            size: 8,
          },
        },
      },
    },
    plugins: {
      legend: {
        labels: {
          color: "white",
          font: {
            size: 15,
          },
        },
      },
    },
  };

  return (
    <div className="graph-container">
      <div
        className="bg-graph"
        style={{ padding: "10px", borderRadius: "10px" }}
      >
        <Line data={data} height={200} options={options} />
      </div>
    </div>
  );
};

export default Graph;
