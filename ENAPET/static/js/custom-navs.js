$(function(){
  var hash = window.location.hash;

  if(hash) {
    $('.nav-tabs a[href="' + hash + '"]').tab('show');
    $('html, body').animate({
      scrollTop: ($(".content-header").offset().top - 50)
    }, 1000);
  };

  $('.nav-tabs a').click(function (e) {
    window.location.hash = this.hash;
  });
});
