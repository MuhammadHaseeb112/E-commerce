// for topscrool button

const toTop = document.querySelector(".to-top");

window.addEventListener("scroll",() =>{
    if (window.pageYOffset > 120) {
        toTop.classList.add("active");
    }
    else{
        toTop.classList.remove("active");
    }
})

// for display image

function getImagePreview(event)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="100";
    newimg.height="100";
    imagediv.appendChild(newimg);
  }


  let thumbnails = document.getElementsByClassName('thumbnail')

  let activeImages = document.getElementsByClassName('active')

  for (var i=0; i < thumbnails.length; i++){

    thumbnails[i].addEventListener('mouseover', function(){
      console.log(activeImages)
      
      if (activeImages.length > 0){
        activeImages[0].classList.remove('active')
      }
      

      this.classList.add('active')
      document.getElementById('featured').src = this.src
    })
  }


  let buttonRight = document.getElementById('slideRight');
  let buttonLeft = document.getElementById('slideLeft');

  buttonLeft.addEventListener('click', function(){
    document.getElementById('slider').scrollLeft -= 180
  })

  buttonRight.addEventListener('click', function(){
    document.getElementById('slider').scrollLeft += 180
  })
