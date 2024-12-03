import React, { useState, useEffect  } from 'react'
import plato from '@/public/images/Carne-a-la-Criolla-Colombia.jpg';
import whatsapp from '@/public/images/whatsapp-48.png';
import Image from "next/image";
import { Inter } from "next/font/google";
import Header from "@/components/Header";
import ContainerRecipe from '@/components/ContainerRecipe';
import Modal from '@/containers/Modal';
import {callApi} from '@/utils/api';

// import { Container } from 'postcss';




type Props = {}

export default function index({ }: Props) {

  const [openModal, setOpenModal] = useState(false);
  const [recipe, setRecipe] = useState({}) 


  const closeModal = () => setOpenModal(false);


  const obtenerDatos = async () => {
    try {
      const datos =  await callApi('http://127.0.0.1:8000/recetas/');
      setRecipe(datos)
      setOpenModal(!openModal)
    } catch (error) {
      console.error('Error:');
    }
  };

  // const getRecipe = async () =>{
  
  //   const info = await obtenerDatos()
  //   // console.log(info)
    
  //   // setOpenModal(!openModal)

  // }

  // useEffect(() => {
  //   // getRecipe();
  // }, []);

  return (
    <>
      <Header />
      <button onClick={obtenerDatos} >receta </button>


      <form action="">
        <div className="flex justify-center mt-8">
          <input
            type="text"
            //value={query}
            //onChange={handleInputChange}
            placeholder="Search..."
            className="px-4 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            //onClick={handleSearch}
            className="px-4 py-2 bg-blue-500 text-white rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          > Search</button>
        </div>
      </form>



      {/* <ContainerRecipe /> */}
      
      {openModal && <Modal
        isOpen={openModal}
        closeModal={closeModal}
        information={recipe}
      />}

    </>
  )
}