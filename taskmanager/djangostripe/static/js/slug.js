document.addEventListener("click",f=>{
buttons = document.querySelectorAll('.size');

if(f.target.dataset.action=="size"){
buttons.forEach(function(btn) {
      btn.style="border:none;";
    });
document.querySelector(".inputsize").value=f.target.innerText
f.target.style="border:2px solid yellow"
}

})

function Plus(){
if(parseInt(document.querySelector(".num").innerText)<10){
count=document.querySelector(".num").innerText=parseInt(document.querySelector(".num").innerText)+1
document.querySelector(".inputcount").value=count
}
}
function Minus(){
if(parseInt(document.querySelector(".num").innerText)>1){
count=document.querySelector(".num").innerText=parseInt(document.querySelector(".num").innerText)-1
document.querySelector(".inputcount").value=count
}
}



document.querySelector(".inputsize").value=document.querySelector(".size").innerText
document.querySelector(".size").style="border:2px solid yellow"