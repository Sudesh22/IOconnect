import "./Guage.css";
import GaugeChart from "react-gauge-chart";
// import Chart from "react-google-charts";

export default function Guage({ condition, parameter }) {
  // const gaugeData = [
  //   ["Label", "Value"],
  //   [condition, parameter],
  // ];
  let unit = ''
  if (condition === "Temperature") {
    unit = '°C'        
  }
  else{
    unit = ''
  }

  const chartStyle = {
    height: 100,
    width: 250,
  };
  const perc = parameter / 100;
  return (
    <div className="graphs-container ">
      {/* <Chart
        // width={}
        height={150}
        chartType="Gauge"
        loader={<div>Loading guage</div>}
        data={gaugeData}
        options={{
          redFrom: 90,
          redTo: 100,
          yellowFrom: 75,
          yellowTo: 90,
          minorTicks: 5,
        }}
        rootProps={{ "data-testid": "1" }}
      /> */}

      

      <GaugeChart
              id="gauge-chart8"
              style={chartStyle}
              nrOfLevels={30}
              colors={['#5BE12C', '#F5CD19', '#EA4228']}
              arcWidth={0.3}
              percent={perc}
              formatTextValue={value => value + unit}
            />
    </div>
  );
}
