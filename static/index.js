// For every clicked button that leads to no route, pops a message 
var buttons = document.querySelectorAll("button.alert-button");
Array.from(buttons).forEach(
    button => {button.addEventListener('click', warn)}
);
function warn(){
    window.alert('As it is a demo, this button has not any real functionality yet. Try the "Tecnologies" button or the "Clothes" one.');
}

// Responsivite
var width = window.innerWidth;
var height = window.innerHeight;

var standardWidth = (width * 0.08 * 2) + (200 * 3) 
if (width < standardWidth){
    // Display the buttons vertically
    var e = document.querySelectorAll(".ports");
    Array.from(e).forEach(
        element =>{
        element.style.display = "flex";
        element.style.flexDirection = "column";
        }
    )
    // Make minor of the top and bottom
    var divs = document.querySelectorAll(".main-div");
    Array.from(divs).forEach(
        element => {
            element.style.margin = "4vh 0";
        }
    )
}