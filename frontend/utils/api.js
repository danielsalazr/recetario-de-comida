// import { countReset } from "console";

// import Cookies from 'js-cookie';
// const token=Cookies.get('csrftoken')



export async function callApi(url, options = {}){

  const req1 = await fetch(url,
    {
      method:'GET',
      // credentials: 'include',
      // mode: 'cors',
      // headers: {
        // 'Content-Type': 'application/json',
      //   'Connection': 'keep-alive',
      //   'Cache-Control' : 'no-cache',
        // 'X-CSRFToken':csrfToken, 
        // 'Cookie': `sessionid=${SessionId};`, 
      // }, 
    }
  )
  
    
  if (!req1.ok) {

    return { error: true, statusText: req1.statusText };
    
  }
  const data2 = await req1.json();
  console.log(data2);

  return data2
}



// console.log(token);

export async function getTicketsInfo( csrfToken, SessionId, id){

    const req1 = await fetch(`http://localhost:8000/entradas/impresiontickets/${id}`,
      {
        method:'GET',
        credentials: 'include',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        //   'Connection': 'keep-alive',
        //   'Cache-Control' : 'no-cache',
          'X-CSRFToken':csrfToken, 
          'Cookie': `sessionid=${SessionId};`, 
        }, 
      }
    )
    if (!req1.ok) {

      return { error: true, statusText: req1.statusText };
      
    }
    const data2 = await req1.json();
    // console.log(data2);
  
    return data2
  }


export async function DeleteInfo(endpoint, id) {
  

  const sesion = localStorage.getItem('sesion');

  try {
    const req1 = await fetch(`http://localhost:8000/entradas/impresiontickets/?${endpoint}=${id}`, {
      method: 'DELETE',
      credentials: 'include',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': token,
        'Cookie': `sessionid=${sesion};`,
      },
    });

    if (!req1.ok) {

      return { error: true, statusText: req1.statusText };
    }

    return req1; 
  } catch (error) {
    console.error('Error en la llamada a la API:', error);
    return { error: true, message: error.message };
  }
}

export async function GenerarPDF(items) {
  if (!items) {
    throw new Error('Items no proporcionados');
  }

  const sesion = localStorage.getItem('sesion');
  console.log(token + '' + sesion)
  console.log(sesion)

  try {
    const req1 = await fetch(`http://localhost:8000/entradas/impresionTicketsPdf/`, {
      method: 'POST',
      credentials: 'include',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': token,
        'Cookie': `sessionid=${sesion};`,
      },
      body: JSON.stringify(items), 
    });

    if (!req1.ok) {

      return { error: true, statusText: req1.statusText };
    }
 
    const respuesta = await req1.json();
    const rutaPDF = respuesta.path;
    console.log(rutaPDF);
    const urlPDF = `http://localhost:8000${rutaPDF}`;
  
    return urlPDF;

  } catch (error) {
    console.error('Error en la llamada a la API:', error);
    return { error: true, message: error.message };
  }
}

export async function EntradasGeneradas(numeroOrden){
  const sesion = localStorage.getItem('sesion');
  const req1 = await fetch(`http://localhost:8000/entradas/EntradaMercancias/?po=${numeroOrden}`,
    {
      method:'GET',
      credentials: 'include',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      //   'Connection': 'keep-alive',
      //   'Cache-Control' : 'no-cache',
        'X-CSRFToken':token, 
        'Cookie': `sessionid=${sesion};`, 
      }, 
    }
  )
  if (!req1.ok) {

    return { error: "No se encontro entradas de esta orden", statusText: req1.statusText };
    
  }
  const res = await req1.json();
  console.log(res);
  // console.log(data2);

  return res
}



