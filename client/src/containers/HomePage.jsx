import React from 'react';
import { Footer } from './Footer';
import { Header } from './Header';
import { SoundBoard } from './SoundBoard';
import { SavedSounds } from './SavedSounds';
import './HomePage.css';

export function HomePage() {
  return (
    <div className="homepage">
      <Header />
      <div className="homepage__content">
        <SavedSounds />
        <SoundBoard />
      </div>
      <Footer />
    </div>
  );
};
