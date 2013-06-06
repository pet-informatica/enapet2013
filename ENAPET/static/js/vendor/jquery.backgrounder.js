/**
 * (c) 2013 Guilherme Cavalcnti
 *
 * Version: v1.1
 * Author: Guilherme Cavalcanti
 *
 * This plugin is based on the jquery-backgrounder plugin by Nico Di Rocco
 * See code from github here: https://github.com/nrocco/jquery-backgrounder
 **/

$.fn.backgrounder = function( images, options )
{
	//Default settings
	var settings = {
		transitionTime: 1600,						// Amount of time to fade in/out the images
		displayTime: 		5000,
		zIndex: 				-666,
    width: $(this).width(),
    height: $(this).height(),
	};

  var helper = {
    buildContainer: function(){
      var $container = $("<div/>").attr("id", "backgrounder");
      var css = {
        left: 0,
        top: 0,
        overflow: "hidden",
        zIndex:settings.zIndex,
        width: '100%'
      }

      return $container.css(css);
    },

    buildImage: function(src) {
      var css = {
        display:"none",
        position:"absolute",
        zIndex:settings.zIndex,
        width: '100%',
        height: settings.height
      }

      return $("<div>").css(css).addClass('image').addClass(src);
    }
  }

	// Combine options with default settings if it's needed
	if(options && typeof options == "object")
		settings = $.extend(settings, options);

	// Create $container and add to the body
	var $container = helper.buildContainer();
  var $this = $(this);

	$(this).prepend($container).css({overflow:"hidden"});

	// Load all the images and add to $container
	var $imgElement;
	for( var i = images.length; i--; )
	{
    var $imgElement = helper.buildImage(images[i]);
		$container.append($imgElement);
	}

	// Grab the first image in the $container and fade in
	$("div:first-child", $container).toggleClass("current").fadeIn(settings.transitionTime);

	// Slideshow enabled
	setInterval(function()
	{
		var $currImg = $(".current", $container);

		if( !$currImg.next().length )
			var startAtBeginning = true;

		if( startAtBeginning )
		{
			$container.find('div:first-child').addClass("current").css({display:'block'});
			$currImg.removeClass("current").fadeOut(settings.transitionTime);
		}
		else
		{
			$currImg.next().addClass("current").fadeIn(settings.transitionTime,function(){
				$currImg.removeClass("current").css({display:"none"});
			});
		}
	}, settings.displayTime);
}
