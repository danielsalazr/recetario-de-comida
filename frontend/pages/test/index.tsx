import React, { useState, useEffect  } from 'react';
import {callApi} from '@/utils/api';

function index() {

    const [datos, setDatos] = useState({});

    const obtenerDatos = async () => {
        // try {
          const respuestaa =  await fetch('http://127.0.0.1:8000/recetas/');
          const data = await respuestaa.json();
          setDatos(data);
          console.log(datos);
          // closeModal()
        // } catch (error) {
        //   console.error('Error:');
        // }
      };

      useEffect(() => {
        //   // getRecipe();
        console.log(datos)
        }, []);

  return (
    <div>
    <button onClick={obtenerDatos} >receta </button>
    {/* <p>{JSON.stringify(datos)}</p> */}
    </div>
  )
}

export default index
