$.getJSON('https://swapi.co/api/people/5/?format=json', function (json) {
  $('DIV#character').text(json.name);
});
