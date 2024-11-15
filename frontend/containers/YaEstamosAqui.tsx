import React from 'react'
import comida_bienvenida from '@/public/images/comida_bienvenida.jpg';
import Image from "next/image";
import Link from 'next/link';


type Props = {}

export default function YaEstamosAqui({}: Props) {
  return (
    <section className="max-w-container md:py-8  ">
        <div className='grid grid-cols-1  justify-center mx-auto max-w-7xl py-10 gap-x-4  md:grid-cols-2 '>
            <div className="flex justify-center px-4" >
                <Image
                    src={comida_bienvenida}
                    alt=''
                    width={600}
                    height={600}
                    className='rounded-md'
                    // className='w-96 '
                    // style={{"width": '160%'}}
                />
            </div>

            <div className="flex-1 p-9 basis-full md:basis-8/12">
              <p className="text-4xl font-semibold leading-tight mt-12 mb-6 pt-24">
                <strong>¡Estamos aquí!</strong>
              </p>
            
              <p className="text-2xl mb-6">
                Inicia ya tu plan de recetas para toda la semana y únete totalmente gratis a nuestro canal para que nos sigas y des tus aportes.
              </p>
            
            <button className='text-1xl p-3  bg-lime-500 text-white rounded-md hover:bg-lime-600 focus:outline-none focus:ring-2 focus:ring-lime-500'>
                Unirse
            </button>
             
           </div>


        </div>
    </section>
  )
}