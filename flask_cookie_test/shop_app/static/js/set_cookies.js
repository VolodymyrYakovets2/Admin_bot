const buttons = document.querySelectorAll(".buy");

for (let id = 0; id < buttons.length; id++){
    let button = buttons[id]
    button.addEventListener('click', function(){
        if (document.cookie != ""){
            let products = document.cookie.split("=")[1]
            document.cookie = `product = ${products} ${button.id}; Path = /`
        } else {
            document.cookie = `product = ${button.id}; Path = /`
        }
    })
}