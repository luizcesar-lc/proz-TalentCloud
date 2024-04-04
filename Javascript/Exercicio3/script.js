//------ Simples

let body = document.querySelector('body')
let titulo = document.createElement('h1')

titulo.innerHTML = "Loja de roupa"
titulo.id = "titulo"

body.appendChild(titulo)

//------ Complexo

let roupa = document.createElement('div')

roupa.innerHTML = `
<div>
  <h2>Camisa</h2>
  <img src="https://a-static.mlcdn.com.br/1500x1500/camisa-social-masculina-slim-manga-longa-azul-marinho-c15-u-s-born/estilomodas/5306844214/da029b690bb9d39e2c39937583403241.jpg" alt="Camisa">
  <p>Camisa Social azul escuro.</p>
  <p id="preco-camisa">R$ 79,99</p>
</div>
<div>
<h2>Calça</h2>
<img src="https://th.bing.com/th/id/R.b16b1057da91ddc0499daf1f2b591509?rik=Z9%2fAecCbV%2f%2f0gA&pid=ImgRaw&r=0" alt="Calça">
<p>Calça Social preta.</p>
<p id="preco-calca">R$ 129,99</p>
</div>
`;
body.appendChild(roupa)
