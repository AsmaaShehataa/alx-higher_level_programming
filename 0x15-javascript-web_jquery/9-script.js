$('document').ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function() {
    $('DIV#hello').text(data.hello);
  });
});
