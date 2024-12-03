import React, {useEffect, useState} from 'react'
import {callApi} from '@/utils/api';
import Header from '@/components/Header';

import Select from 'react-select';
import AsyncSelect from 'react-select/async';
import 'select2/dist/css/select2.min.css';
import { Label } from 'flowbite-react';

export const getServerSideProps : GetServerSideProps<Props> = async () => {
  // try {
    const info = await callApi(`http://127.0.0.1:8000/recetas/recipesFormInfo/`);
    // const datos = await respuesta.json();
    console.log(info)
    return {
      props: {
        info,
        // id: params.id,
      },
    };
  // } catch (error) {
  //   console.error(error);
  //   return {
  //     notFound: true,
  //   };
  }



function Create({info}) {

    console.log(info)
    const [name, setName] = useState('');
    const [ingredients, setIngredients] = useState('');
    const [description, setDescription] = useState('');
    const [categories, setCategories] = useState([]);
    const [author, setAuthor] = useState('');
    const [img,setImg]= useState([]);
    const [selectedOption, setSelectedOption] = useState(null);

    const options = [
      { value: 'chocolate', label: 'Chocolate' },
      { value: 'strawberry', label: 'Strawberry' },
      { value: 'vanilla', label: 'Vanilla' }
    ]

    
    
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log()

      const recipeForm = document.querySelector('#recipeForm');
      const formData = new FormData(recipeForm);

      img.forEach( file => formData.append("imagen", file))
      

      const req = await fetch("http://127.0.0.1:8000/recetas/", {
        method: 'POST',
        body: formData
      });

      const data = await req.json();

      console.log(data);

    };



    function capturar(e) {
      console.log(e.target.files[0]);
      const imagen = e.target.files[0]
      const nombre = e.target.files[0].name;

      const data = {
        "datos": imagen,
        // "name": nombre
      }

      setImg((prevImg)=>[...prevImg, imagen]);
      console.log(img)
 
    }

    const handleChange = (selectedOption) => {
      setSelectedOption(selectedOption);
    };

    useEffect(()=>{
      console.log(img)
    },[img])

    
    useEffect(() => {
      if (info && info.categories) {
        const categoriesOptions = info.categories.map((category) => ({
          value: category.id,
          label: category.name,
        }));
        setCategories(categoriesOptions);
      }
    }, [info]);

    return (
      <>
      <Header></Header>
      <div className='flex justify-center items-center p-8'>

      <form
        onSubmit={handleSubmit}
        encType="multipart/form-data"
        className="w-10/12 mx-auto p-4 bg-white rounded-lg shadow-md"
        id="recipeForm"
      >
        <h2 className="text-lg font-bold mb-4">Crear Receta</h2>
  
        <div className="mb-4">
          <label
            htmlFor="name"
            className="block text-sm font-medium text-gray-700"
          >
            Nombre Receta
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="block w-full p-2 pl-10 text-sm text-gray-700 border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
            placeholder="Ingrese nombre de receta"
            required
          />
        </div>

        <div className='grid grid-cols-2 gap-4'>

        
        <div className="mb-4">
          <label
            htmlFor="ingredients"
            className="block text-sm font-medium text-gray-700"
          >
            Ingredientes
          </label>
          <textarea
            id="ingredients"
            value={ingredients}
            name="ingredients"
            onChange={(e) => setIngredients(e.target.value)}
            className="block w-full p-2 pl-10 text-sm text-gray-700 border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 h-96"
            placeholder="Ingrese ingredientes"
            rows="12"
            required
          />
        </div>
  
        <div className="mb-4">
          <label
            htmlFor="description"
            className="block text-sm font-medium text-gray-700"
          >
            Descripción
          </label>
          <textarea
            id="description"
            value={description}
            name="description"
            onChange={(e) => setDescription(e.target.value)}
            className="block w-full p-2 pl-10 text-sm text-gray-700 border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 h-96"
            placeholder="Ingrese descripción"
            rows="12"
            required
          />
        </div>

        </div>
  
        <div className="mb-4">
          <label
            htmlFor="categories"
            className="block text-sm font-medium text-gray-700"
          >
            Categorías
          </label>
          <select
            multiple
            id="categories"
            value={categories}
            name="categories"
            onChange={(e) =>
              setCategories(
                Array.from(e.target.selectedOptions, (option) => option.value)
              )
            }
            className="block w-full p-2 pl-10 text-sm text-gray-700 border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          >
            {info.categories.map( (option) => <option value={option.value}>{option.name}</option>)}
            {/* <option value="1">Categoría 1</option>
            <option value="2">Categoría 2</option> */}
            {/* ... */}
          </select>

        <Select
          value={selectedOption}
          onChange={handleChange}
          options={categories}
          isMulti
          required
        >
          
        </Select>
        </div>
        <div>
          <input type='file' name="leFile" onChange={(event)=>capturar(event)}/>
        </div>
        <div className='grid grid-cols-5 gap-4 mt-3'>
          {img ? (
            img.map((image, index) => (
              image instanceof File && (
                <img
                  key={index}
                  src={URL.createObjectURL(image)}
                  alt={`Imagen ${index + 1}`}
                  width={250}
                  height={250}
                  className='rounded-lg shadow-md'
                  
                />
              )
            ))
          ) : (
            <h1>No images</h1>
          )}
        </div>
       

      

  
        {/* <div className="mb-4">
          <label
            htmlFor="author"
            className="block text-sm font-medium text-gray-700"
          >
            Autor
          </label>
          <select
            id="author"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            className="block w-full p-2 pl-10 text-sm text-gray-700 border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
            required
          >
            <option value="1">Autor 1</option>
            <option value="2">Autor 2</option>
            
          </select>
        </div> */}
  
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Guardar Receta
        </button>
      </form>

      </div>

   
      
      </>
    );
}

export default Create
