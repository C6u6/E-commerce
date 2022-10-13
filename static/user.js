// Make the submit button be appear
var checkButton = document.querySelector("#control-submit");
checkButton.addEventListener('click', appear);

function appear(){
    var state = checkButton.checked;
    var submitButton = document.querySelector("#change-data-submit");

    if (state){
        submitButton.disabled = false;
        return;
    }
    submitButton.disabled = true;
}
// Responsivite
var width = window.innerWidth;

if (width < 450){
    document.querySelector("#user-title").style.margin = "10px 5vw 0 5vw";
    Array.from(document.querySelectorAll(".warn")).forEach(
        el => {
            el.style.margin = "1px 3vw 1px 3vw";
        }
    );
    var labels = document.getElementsByTagName('label');
    var inputs = document.getElementsByTagName('input');
    for (var label of labels){
        label.style.margin = "1px 3vw 1px 3vw";
    }
    for (var input of inputs){
        input.style.margin = "1px 3vw 1px 3vw";
    }
    document.querySelector("#control-submit").style.margin = "1px 0 1px 3vw";
    document.querySelector("#special-label").style.margin = '0';
    document.querySelector("#change-data-submit").style.margin = "1px 3vw 1px 3vw";
}