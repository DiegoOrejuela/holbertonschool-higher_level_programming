#!/usr/bin/node

exports.converter = function (base) {
  const b = base;

  function mybase (n) {
    return (n.toString(b));
  }
  return (mybase);
};
