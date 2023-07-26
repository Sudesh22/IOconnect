import React from "react";
import "./Team.css";
import Card from "./Card";
import { data } from "./data.js";

export default function Team() {
  return (
    <div className="team-container">
      <p className="team">Team</p>
      <div className="team-member">
        {data.map((items, index) => {
          return <Card key={index} {...items} />;
        })}
      </div>
    </div>
  );
}
