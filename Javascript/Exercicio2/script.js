let titulo = document.getElementById('titulo')
let listaNOrdenada = document.querySelector('ul')
let link = document.querySelector('a')
let listaOrdernada = document.getElementById('lista-ordenada')

titulo.innerText = "Novo título"

listaNOrdenada.innerHTML = `
  <li>Inteligencia</li>
  <li>Confiança</li>
  <li>Rapidez</li>
`

link.innerText = "Acesse o site da Proz Educação"

listaOrdernada.innerHTML = `
    <li><a href="https://google.com/">Google</a></li>
    <li><a href="https://bing.com">Bing</a></li>
    <li><a href="https://yahoo.com">Yahoo</a></li>
`