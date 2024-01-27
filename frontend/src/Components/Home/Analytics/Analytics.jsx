import './Analytics.css';
import Graph from "./Graph/Graph";
import React from "react";
import { Slider } from '@mui/material';
import { styled } from '@mui/material/styles';

export default function Analytics({ baseUrl }) {

  const iOSBoxShadow =
    '0 3px 1px rgba(0,0,0,0.1),0 4px 8px rgba(0,0,0,0.13),0 0 0 1px rgba(0,0,0,0.02)';

  const marks = [
    {
      value: 1,
    },
    {
      value: 2,
    },
    {
      value: 3,
    },
  ];

  const IOSSlider = styled(Slider)(({ theme }) => ({
    // color: theme.palette.mode === 'dark' ? '#3880ff' : '#3880ff',
    height: 2,
    padding: '15px 0',
    '& .MuiSlider-thumb': {
      height: 10,
      width: 5,
      backgroundColor: '#fff',
      boxShadow: iOSBoxShadow,
      '&:focus, &:hover, &.Mui-active': {
        boxShadow:
          '0 3px 1px rgba(0,0,0,0.1),0 4px 8px rgba(0,0,0,0.3),0 0 0 1px rgba(0,0,0,0.02)',
        // Reset on touch devices, it doesn't add specificity
        '@media (hover: none)': {
          boxShadow: iOSBoxShadow,
        },
      },
      borderRadius: '1px',
    },
    '& .MuiSlider-valueLabel': {
      fontSize: 12,
      fontWeight: 'normal',
      top: 50,
      backgroundColor: '#fff',
      color: theme.palette.text.primary,
      '&:before': {
        display: 'none',
      },
      '& *': {
        background: 'transparent',
        color: theme.palette.mode === 'dark' ? '#fff' : '#000',
      },
    },
    '& .MuiSlider-track': {
      border: 'none',
    },
    '& .MuiSlider-rail': {
      opacity: 0.5,
      backgroundColor: '#bfbfbf',
    },
    '& .MuiSlider-mark': {
      backgroundColor: '#bfbfbf',
      height: 8,
      width: 1,
      '&.MuiSlider-markActive': {
        opacity: 1,
        backgroundColor: 'currentColor',
      },
    },
  }));

  // var text = 'Daily';
  function setInputValue(value) {
    var text;
    if (value === 1) {
      text = 'Weekly';
      return 'Weekly';
    }
    else if (value === 2) {
      text = 'Monthly';
      return 'Monthly';
    }
    else if (value === 3) {
      text = 'Yearly';
      return 'Yearly';
    }
    setChartData((prev) => ({
      ...prev,
      valuee: value,
      textt: text,
    }));
  }

  const [chartData, setChartData] = React.useState({
    temperature1: [],
    temperature2: [],
    valuee: 1,
    textt: "Daily",
  });
  // console.log(localStorage.getItem("userProfile"))

  // fetching the chart data
  function fetchData(value) {
    var timeframe = setInputValue(value)
    fetch(`${baseUrl}/analysis`, {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        access_token: localStorage.getItem("userProfile"),
        timeframe: timeframe,
      }),
    })
      .then((response) => response.json())
      .then(responsee => {
        setChartData((prev) => ({
          ...prev,
          temperature1: responsee[0],
          temperature2: responsee[1],
          valuee: value,
          textt: timeframe,
        }));
      })

  }
  // Fetch data initially
  // fetchData("Daily");

  // Fetch data every second
  // const intervalId = setInterval(fetchData, 5000);

  // Cleaning interval when the component unmounts


  return (
    <div className='analytics-container'>
      <p className="analytics">Analytics</p>
      <div className="dashboard-status">
        <div className="device-status">
        </div>
      </div>
      <div className="analytics-container">
        <br />
        <Graph condition={"Temperature1"} chartData={chartData} timeframe={chartData.textt} />
        <Graph condition={"Temperature2"} chartData={chartData} timeframe={chartData.textt} />
        <p className="filter">Time Frame</p>
        <IOSSlider
          sx={{
            width: 200,
          }}
          className='slider'
          aria-label="ios slider"
          defaultValue={chartData.valuee}
          value={chartData.valuee}
          marks={marks}
          valueLabelDisplay="auto"
          valueLabelFormat={value => <div>{setInputValue(value)}</div>}
          step={1}
          min={1}
          max={3}
          onChange={(_, value) => setInputValue(value)}
          onChangeCommitted={(event, value) => fetchData(value)}
        />
      </div>
    </div>
  )
}