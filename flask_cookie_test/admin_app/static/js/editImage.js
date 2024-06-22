let listImageButtons = document.querySelectorAll('.change-image')

for(let count = 0; count < listImageButtons.length; count++ ){
    let imageButton = listImageButtons[count]
    imageButton.addEventListener(
        type = 'click',
        listener = (event) =>{
            console.log(imageButton.id)
            document.querySelector(".submit-changes").value = "image-" + imageButton.id
            document.querySelector(".modal-window").style = "display: flex;"
            // console.log(document.querySelector(".submit-changes").value)
        }
    )
}