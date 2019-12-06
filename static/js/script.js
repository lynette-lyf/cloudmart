/* global $ */
/* global TweenMax */
/* global Power2 */

// TOGGLE NAVBAR ANIMATION FOR MOBILE
const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');

  burger.addEventListener('click', () => {
    // Toggle Navbar
    nav.classList.toggle('nav-active');


    // Animate Links
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = '';
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index/7+0.3}s`;
      }
        
    });

    // Burger Animation
    burger.classList.toggle('toggle');




  });


}

navSlide();


// PARALLAX CURSOR ANIMATION

$(document).ready(function () {
  var timeout;
  $('#ParallaxCursor').mousemove(function(e){
    if(timeout) clearTimeout(timeout);
    setTimeout(callParallax.bind(null, e), 200);
    
  });

  function callParallax(e){
    parallaxIt(e, '.slide.one', -100);
    parallaxIt(e, '.slide.two', -50);
    parallaxIt(e, '.slide.three', -100);
    parallaxIt(e, 'img', -30);
}
  

  function parallaxIt(e, target, movement){
    var $this = $('#ParallaxCursor');
    var relX = e.pageX - $this.offset().left;
    var relY = e.pageY - $this.offset().top;
    
    TweenMax.to(target, 1, {
      x: (relX - $this.width()/2) / $this.width() * movement,
      y: (relY - $this.height()/2) / $this.height() * movement,
      ease: Power2.easeOut
    })
  }
});



