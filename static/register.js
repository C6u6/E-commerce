/* Register */
var checkButton = document.querySelector("#Check1");
checkButton.addEventListener('click', check);

function check(){
    // Value of the checkbox
    var value = checkButton.checked;
    // Submit button disabled
    var button = document.querySelector("#submit-button");

    if (value == true){
        button.disabled = false;
    }
    else{
        button.disabled = true;
    }
}