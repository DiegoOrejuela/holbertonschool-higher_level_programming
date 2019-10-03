$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/', { lang: langCode }, function (json) {
      $('DIV#hello').text(json.hello);
    });
  });
});
