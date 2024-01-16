const code = document.getElementById('code')   
const brand = document.getElementById('brand')
const type = document.getElementById('type')
const category = document.getElementById('category')
const price = document.getElementById('price')
const cost = document.getElementById('cost')
const obs = document.getElementById('obs')

const inputList = [code, brand, type, category, price, cost, obs]

function sendForm() {
   const itenList = []

   let formItens = [{
      codigo: code.value,
      marca: brand.value,
      tipo: type.value,
      categoria: category.value,
      preco: price.value,
      custo: cost.value,
      observação: obs.value,
   }]   

   itenList.push(formItens)
}

function clearForm(){
   for (i of inputList){
      i.value = " "
   }
}