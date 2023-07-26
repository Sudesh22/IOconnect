import "./Guage.css";
import GaugeChart from "react-gauge-chart";
// import Chart from "react-google-charts";

export default function Guage({ condition, parameter }) {
  // const gaugeData = [
  //   ["Label", "Value"],
  //   [condition, parameter],
  // ];
  const chartStyle = {
    height: 100,
    width: 200,
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
        id="gauge-chart5"
        style={chartStyle}
        nrOfLevels={420}
        arcsLength={[0.3, 0.5, 0.2]}
        colors={["#5BE12C", "#F5CD19", "#EA4228"]}
        percent={perc}
        arcPadding={0.02}
      />
    </div>
  );
}
