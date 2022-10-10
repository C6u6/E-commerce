// After revealing the toggle element, to there
var mainButton = document.querySelector("#question");
mainButton.addEventListener('click', auxiliar);

function auxiliar(){
    // If the form with 'collapseExample' id is already displayed, do nothing
    if (document.querySelector("#collapseExample"))
    // This function calls another function after three seconds
    setTimeout(() => {
        document.querySelector('#Go-to').click();
    }, 400);
}

// Turn able the register button
var checkControl = document.querySelector("#Check1");
checkControl.addEventListener('click', reveal);

function reveal(){
    var check = checkControl.checked;
    var button = document.querySelector("#submit-button");

    if (check){
        button.disabled = false;
        return;
    }
    button.disabled = true;
}