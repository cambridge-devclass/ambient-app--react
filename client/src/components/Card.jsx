import { useState, useEffect, useRef } from "react";
import "./Card.css";
export function Card({ iconName, soundName }) {
  const [soundOn, setSoundOn] = useState(false);
  const iconSrc = require(`../assets/${iconName}.svg`);
  const soundSrc = `https://devclass-projects-public.s3.us-east-2.amazonaws.com/ambient-app--react/${soundName}.wav`;

  const audioRef = useRef(null);

  useEffect(() => {
    // Create audio instance once
    if (!audioRef.current) {
      audioRef.current = new Audio(soundSrc);
      audioRef.current.loop = true; // Enable looping for ambient sounds
    }

    const audio = audioRef.current;

    if (soundOn) {
      audio.play();
    } else {
      audio.pause();
      audio.currentTime = 0; // Reset to beginning when paused
    }

    // Cleanup function to pause and reset audio when component unmounts
    return () => {
      audio.pause();
      audio.currentTime = 0;
    };
  }, [soundOn, soundSrc]);

  return (
    <div
      onClick={(e) => setSoundOn(!soundOn)}
      className={`${soundOn ? "card_on" : "card_off"} card`}
    >
      <img
        src={iconSrc}
        className={`${soundOn ? "" : "icon_off"} icon`}
        alt={iconName}
      />
      <span className="cardText">Rain</span>
    </div>
  );
}
