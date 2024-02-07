let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  //dots[slideIndex-1].className += " active";
}

var aDiv = document.getElementById("animatedDiv");

function changeWidth() 
{
    var scrollVal = window.pageYOffset;
    var scrollSlow  = (scrollVal / 4);
    
    //Changing CSS Width
    aDiv.style.width = Math.min(Math.max(scrollSlow, 20), 100) + "%";
}

window.addEventListener('scroll', function() 
{
    //requestAnimationFrame(changeWidth);
}, false);

/* Form Page */ 
