#!/usr/bin/node

exports.converter = function (base) {
  function mybase (n) {
    return (n.toString(base));
  }
  return (mybase);
};
