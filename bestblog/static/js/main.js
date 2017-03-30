//Smooth Scroll

function smoothScroll(ele){
    var presentY = window.pageYOffset;
    var eleTop = ele.offsetTop;
    var distance = presentY - eleTop;
    var speed = Math.round(distance / 100);

    if(speed > 20) speed = 20;

    var step = Math.round(distance / 40);
    var leap = presentY + eleTop;
    var timer = 0;

    for(var i = presentY; i > eleTop; i-=step){
        setTimeout("window.scrollTo(0, " + leap + ")", timer * speed);
        leap -= step;
        timer++;
        if(leap < eleTop){
            leap = eleTop;
            setTimeout("window.scrollTo(0, " + leap + ")", timer * speed);
        }
    }
}

var target = document.querySelector("html");
var topBtn = document.querySelector("#top-btn");

topBtn.addEventListener("click", function(){
    smoothScroll(target);
});

//toggle

function setMenu(ele){
    ele.addEventListener("click", function(){
        if(tmp === true){
            toggleMenus.style.display = "block";    
            tmp = false;
        }
        else{
            toggleMenus.style.display = "none";    
            tmp = true;
        }
    });
}

var toggleBtn = document.querySelector(".toggle-btn");
var toggleMenus = document.querySelector(".mobile-category ul");
var tmp = true;

setMenu(toggleBtn);
setMenu(toggleMenus);
