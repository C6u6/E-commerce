/* Index */
var buttons = document.querySelectorAll("button.alert-button");
Array.from(buttons).forEach(
    button => {button.addEventListener('click', warn)}
);

function warn(){
    window.alert('As it is a demo, this button has not any real functionality yet. Try the "Tecnologies" button or the "Clothes" one.');
}