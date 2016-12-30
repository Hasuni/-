/*-----------------------------------------------------------------------------------*/
/*	REGISTRATION
/*-----------------------------------------------------------------------------------*/ 
function send(form_name){
	var check1= new RegExp("[0-9a-z_]+@[0-9a-z_^.]+\\.[a-z]{2,3}"); //логин(адрес почты)
	var check2= new RegExp("^[a-z0-9_]+[a-z0-9_]$"); //пароль
	if	((check1.test(login.value)==false)||(check2.test(password.value)==false)){
		if (check1.test(login.value)==false){
			document.getElementById("error2").style.display="inline-block";
		}
		if(check2.test(password.value)==false){
			document.getElementById("error").style.display="inline-block";
		}
	}
	else {document.forms[form_name].submit();
	location="index.html";}
}
/*-----------------------------------------------------------------------------------*/
/*	POSTS GRID
/*-----------------------------------------------------------------------------------*/ 
$(window).load(function(){
    var $container = $('.blog-grid');

    var gutter = 30;
    var min_width = 345;
    $container.imagesLoaded( function(){
        $container.masonry({
            itemSelector : '.post',
            gutterWidth: gutter,
            isAnimated: true,
              columnWidth: function( containerWidth ) {
                var box_width = (((containerWidth - gutter)/2) | 0) ;

                if (box_width < min_width) {
                    box_width = (((containerWidth - gutter)/2) | 0);
                }

                if (box_width < min_width) {
                    box_width = containerWidth;
                }

                $('.post').width(box_width);

                return box_width;
              }
        });
        $container.css( 'visibility', 'visible' ).parent().removeClass( 'loading' );
    });
});



    
/*-----------------------------------------------------------------------------------*/
/*	BUTTON HOVER
/*-----------------------------------------------------------------------------------*/

jQuery(document).ready(function($)  {
$("a.button, .forms fieldset .btn-submit, #commentform input#submit").css("opacity","1.0");
$("a.button, .forms fieldset .btn-submit, #commentform input#submit").hover(function () {
$(this).stop().animate({ opacity: 0.85 }, "fast");  },
function () {
$(this).stop().animate({ opacity: 1.0 }, "fast");  
}); 
});


/*-----------------------------------------------------------------------------------*/
/*	FLICKR
/*-----------------------------------------------------------------------------------*/
	
$(document).ready(function($){
	$('.flickr-feed').dcFlickr({
		limit: 9, 
        q: { 
            id: '51789731@N07',
			lang: 'en-us',
			format: 'json',
			jsoncallback: '?'
        },
		onLoad: function(){
			$('.frame a').prepend('<span class="more"></span>');
			$('.frame').mouseenter(function(e) {

            $(this).children('a').children('span').fadeIn(300);
        }).mouseleave(function(e) {

            $(this).children('a').children('span').fadeOut(200);
        });
		}
	});
});	


/*-----------------------------------------------------------------------------------*/
/*	MENU
/*-----------------------------------------------------------------------------------*/
ddsmoothmenu.init({
	mainmenuid: "menu",
	orientation: 'h',
	classname: 'menu',
	contentsource: "markup"
})