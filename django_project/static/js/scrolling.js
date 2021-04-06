$(window).scroll(function(){
     var scroll = $(window).scrolltop();
     console.log(scroll)
     if(scroll >=300){
         $("#myNav").addClass("bg-dark");
     }
     else {
         $("#myNav").adClass("bg-dark");
     }
}); 