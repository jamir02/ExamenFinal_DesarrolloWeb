function crearSolicitud()
{
    let clienteSolicitud = document.getElementById('clienteSolicitud')
    let cuerpoTabla = document.getElementById('cuerpoTabla')
    clienteInfo = clienteSolicitud.value
    console.log(cuerpoTabla.rows)
    console.log(cuerpoTabla.rows.length)
    longitudTabla = cuerpoTabla.rows.length
    arregloProductos = []
    for(let i = 0; i < longitudTabla; i++)
    {
        productoDatos = cuerpoTabla.rows.item(i)
        let producto = [productoDatos.cells.item(0).innerHTML,productoDatos.cells.item(1).innerHTML,productoDatos.cells.item(2).innerHTML,productoDatos.cells.item(3).innerHTML,productoDatos.cells.item(4).innerHTML]
        arregloProductos.push(producto)
    }
    console.log(arregloProductos)

    url = '/proyCurso/agregarSolicitud'
    infoProductos = {
        'productosCapturados':arregloProductos,
        'cliente':clienteInfo
    }

    fetch(url,{
        method:"POST",
        headers: {
            "X-Request-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(infoProductos)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        window.location.assign('/proyCurso/dashboard')
    })
}

function getCookie(name)
{
    let cookieValue = null;
    if(document.cookie && document.cookie !== "")
    {
        const cookies = document.cookie.split(";")
        for(let i=0;i < cookies.length; i++)
        {
            const cookie = cookies[i].trim();
            if((cookie.substring(0,name.length + 1 )) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieValue;
}

function agregarProducto()
{
    let idProducto = document.getElementById('idProducto')
    let nombreProducto = document.getElementById('nombreProducto')
    let estadoProducto = document.getElementById('estadoProducto')
    let precioProducto = document.getElementById('precioProducto')
    let cantidadProducto = document.getElementById('cantidadProducto')

    let cuerpoTabla = document.getElementById('cuerpoTabla')

    cuerpoTabla.innerHTML += `
    <tr>
        <td>${idProducto.value}</td>
        <td>${nombreProducto.value}</td>
        <td>${cantidadProducto.value}</td>
        <td>${estadoProducto.value}</td>
        <td>${precioProducto.value}</td>
    </tr>
    `
}

addEventListener('DOMContentLoaded', ()=>{
    let infoProducto = document.getElementById('infoProducto')

    infoProducto.onchange = function()
    {
        identificador = infoProducto.value
        fetch(`http://127.0.0.1:8000/proyCurso/obtenerInfo?producto=${identificador}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let idProducto = document.getElementById('idProducto')
            let nombreProducto = document.getElementById('nombreProducto')
            let estadoProducto = document.getElementById('estadoProducto')
            let precioProducto = document.getElementById('precioProducto')

            idProducto.value = data.dato[0]
            nombreProducto.value = data.dato[1]
            estadoProducto.value = data.dato[4]
            precioProducto.value = data.dato[2]

        })
    }
})