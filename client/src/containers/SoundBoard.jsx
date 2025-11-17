import React from "react";
import "./SoundBoard.css";
import { Card } from "../components/Card";

export function SoundBoard() {
  return (
    <div className="soundboard">
      Sounds buttons will be here.
      <Card iconName={"sound_heavy-rain"} soundName={"heavy_rain"} />
    </div>
  );
}
