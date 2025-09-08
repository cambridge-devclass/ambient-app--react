import React from 'react';
import classnames from 'classnames';

// Material symbols
// https://fonts.google.com/icons?icon.size=24&icon.color=%231f1f1f&icon.style=Rounded&icon.set=Material+Symbols

export function Icon(props) {
  const { name, className, size, ...rest } = props;
  const cl = {
    'material-symbols-rounded': 1,
    [className]: !!className,
  };

  return (
    <span className={classnames(cl)} {...rest}>{name}</span>
  );
};

