import React from 'react'
import comida_bienvenida from '@/public/images/comida_bienvenida.jpg';
import Image from "next/image";
import Link from 'next/link';


type Props = {}

export default function YaEstamosAqui({}: Props) {
  return (
    <section className="max-w-container py-0 md:py-8 ">
        <div className='flex flex-row  flex-container justify-center mx-auto max-w-7xl py-4 gap-x-4'>
            <div className="flex-1 justify-center  p-4" >
                <Image
                    src={comida_bienvenida}
                    alt=''
                    // width={400}
                    // height={200}
                    // className='w-96 '
                    // style={{"width": '160%'}}
                />
            </div>

            <div className="flex-1 p-4 basis-full md:basis-8/12">
                {/* <h2>Ya estamos aqui</h2> */}
                <p className="text-4xl font-normal leading-6">
                    
                    <strong>¡Estamos aqui!</strong>
                    
                </p>

                
                

                <p className='text-2xl'>
                    <br />
                    <br />
                    <br />
                    Inicia ya tu plan de recetas para toda la semana y unete totalmente gratis a nuestro canal para nos sigas y des tus aportes.
                    <br />
                    <br />
                    <br />
                </p>

                <a 
                    href="" 
                    className='text-2xl' 
                    style={{"textDecoration" : "underline"}}
                ><em><strong className=''>Unirse</strong></em></a>
            </div>

        </div>
    </section>
  )
}