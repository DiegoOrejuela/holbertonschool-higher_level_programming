#!/usr/bin/node

exports.add = function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  if (isNaN(num1) || isNaN(num2)) {
    return (NaN);
  } else {
    return (num1 + num2);
  }
};
