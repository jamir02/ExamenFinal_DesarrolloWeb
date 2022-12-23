let variableContador = 0
function f1()
{
    if(variableContador === 10)
    {
        variableContador = 0
    }
    for(let i = 0; i < variableContador; i++)
    {
        console.log('Se ha ingresado a la iterativa')
    }
    console.log('Le ha hecho click al boton')
    variableContador = variableContador + 1
    console.log('La cuenta es : ')
    console.log(variableContador)
}

function f2()
{
    console.log('Se ha cambiado la seleccion')
}


function obtenerInfo(identificador)
{
    console.log(identificador)
    fetch(`http://127.0.0.1:8000/proyCurso/obtenerInfo?producto=${identificador}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let tituloProducto = document.getElementById('tituloProducto')
        let cuerpoTabla = document.getElementById('cuerpoTabla')
        let datosTabla = ['Nombre','Precio','Descripcion','Estado','Stock']
        cuerpoTabla.innerHTML = ''
        tituloProducto.innerHTML = data.dato[0]
        for(let i = 0; i < data.dato.length; i++)
        {
            cuerpoTabla.innerHTML += `
            <tr>
                <td>${datosTabla[i]}</td>
                <td>${data.dato[i]}</td>
            </tr>
            `
        }
    })
}


document.addEventListener('DOMContentLoaded',()=>{
    /*
    let anuncioInfo = document.getElementById('anuncio')
    anuncioInfo.innerHTML = `
    <h1 style='color:red;'> Anuncio de la pagina web  </h1>
    `
    */
    /*
    let elementosNombre = document.getElementById('2')
    console.log(elementosNombre.innerHTML)
    elementosNombre.innerHTML = 'Producto Anime'
    */

    /*
    for(let i = 0; i < elementosNombre.length; i++)
    {
        console.log(elementosNombre[i].innerHTML)
        elementosNombre[i].innerHTML = 'Producto Anime'
    }
    */
})


