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
  if (condition === "Temperature") {
    className = "red";
  } else if (condition === "Humidity") {
    className = "green";
  }
  return className;
}

function getYAxisData(condition, chartData) {
  let data = "";
  if (condition === "Temperature") {
    data = chartData.temperature;
  } else if (condition === "Humidity") {
    data = chartData.humidity;
  }
  return data;
}

function splitDateTime(dateTime) {
  return dateTime.split(" ");
  //   dateTime.split(/(\s+)/)
}
function getXAxisData(chartData) {
  const timeOnlyArray = chartData.Time.map((time) => {
    const timeParts = splitDateTime(time);
    return timeParts[1]; // Extracting the time part
  });
  return timeOnlyArray;
}
const Graph = ({ condition, chartData }) => {
  const x_axis = getXAxisData(chartData);
  const y_axis = getYAxisData(condition, chartData);

  var data = {
    labels: x_axis,
    datasets: [
      {
        label: `${condition}`,
        data: y_axis,
        backgroundColor: [
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
          color: "#0d0d0d",
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
          color: "#0d0d0d",
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
