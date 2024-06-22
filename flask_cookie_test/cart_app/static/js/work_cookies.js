const listButtonsMinus = document.querySelectorAll(".minus")

for (let count = 0; count < listButtonsMinus.length; count++){
    let button = listButtonsMinus[count]
    button.addEventListener(
        "click", 
        function(event){
            let listIdProducts = document.cookie.split("=")[1].split(" ")
            for (let index = 0; index < listIdProducts.length; index++){
                if (listIdProducts[index] == button.id.split("-")[1]){
                    listIdProducts.splice(index, 1)
                    break
                }
            }
            if (listIdProducts.length > 0 ){
                document.cookie = `product = ${listIdProducts.join(" ")}; path = /`
            }else{
                document.cookie = "" 
            }
            button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1
            if (button.nextElementSibling.textContent == 0){
                document.querySelector(`#product-${button.id.split("-")[1]}`).remove()
                let p = document.createElement("p")
                p.textContent = "Корзина порожня"
                document.body.appendChild(p)
            }
        }
    )
}