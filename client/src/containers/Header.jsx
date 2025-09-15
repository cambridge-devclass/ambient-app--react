import React from 'react';
import { Icon } from '../components/Icon';
import './Header.css';


export function Header() {
  return (
    <div className="header">
      <div className="header__logo">Ambient</div>
      <div className="header__buttons">
        <Icon name="person" className="header__button" />
      </div>
    </div>
  );
};
