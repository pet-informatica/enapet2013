$(document).ready(function(){
  $('.event-call').backgrounder(
    ["image-1", "image-2", ],
    { transitionTime: 3000, displayTime: 8000 }
   );
  $("#social-networks li a").tooltip();
});
