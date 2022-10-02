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