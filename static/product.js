// Aks for a file, whenever the user clicks on label (Select image)
var label = document.querySelector("#label-select");
label.addEventListener('click', () => {
    document.querySelector("#inp-img").click();
});

/* Simple function to display the uploaded images */
// All ids of the img tags
var ids = ["1-out", "2-out", "3-out", "4-out", "5-out"];

function previewImages() {
    var preview = document.querySelector('#galery');
    if (this.files) {
        [].forEach.call(this.files, readAndPreview);
}

function readAndPreview(file) {

    // Make sure `file.name` matches our extensions criteria
    if (!/\.(jpe?g|png|gif)$/i.test(file.name)) {
        return alert(file.name + " is not an image");
    } // else...
    
    var reader = new FileReader();
    
    reader.addEventListener("load", function() {
        var image = new Image();
        image.height = 100;
        image.title  = file.name;
        image.src    = this.result;
        preview.appendChild(image);
    });
    reader.readAsDataURL(file);
}
}  
document.querySelector('#inp-img').addEventListener("change", previewImages);