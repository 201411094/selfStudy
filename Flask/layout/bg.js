const body = document.querySelector("body");


function init(){
    const image = new Image();
    image.src = `images/background2.png`;
    image.classList.add("bgImage");
    body.prepend(image);
}

init();