$(document).ready(function () {
  $('INPUT#btn_translate').click(request);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      request();
    }
  });
});

function request () {
  const langCode = $('INPUT#language_code').val();
  $.getJSON('https://www.fourtonfish.com/hellosalut/', { lang: langCode }, function (json) {
    $('DIV#hello').text(json.hello);
  });
}
