import React from 'react'
import Header from "@/components/Header";
import Image from 'next/image';
import imagen from '@/public/images/refrigerios.jpg'
import icono from '@/public/images/whatsapp.png'
import icono2 from '@/public/images/facebook.png'
import icono3 from '@/public/images/instagram.png'
import icono4 from '@/public/images/youtube.png'

type Props = {}

export default function about({}: Props) {
  return (
    <>
        <Header />
        <div className='bg-amber-100 mx-auto p-12'>
            <div className='w-11/12 flex mx-auto'>
            <Image
                src={imagen}
                alt="Almuerzo"
                width={350}
                height={350}
                className=" rounded-full"
                style={{"aspectRatio": "1/1",
                  
                }}
              />

            <div className='px-10'>
                <h1 className='text-2xl pb-5'><strong>Sobre el cocinero</strong></h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Est molestias recusandae expedita omnis aspernatur minus voluptates 
                    pariatur ea consequuntur ad, unde ut! Ducimus porro iste veniam ipsam architecto deleniti eius.</p>
                    <div className='flex gap-4 py-3'>
                    <button className='bg-lime-500 rounded-md p-1'>Mas sobre mi</button>
                    <button className='bg-lime-500 rounded-md p-1'>Mas sobre recetas deliciosas</button>
                    </div>
                    <section className='flex py-2 gap-4'>
                    <Image
                      src={icono}
                      alt="Almuerzo"
                      width={30}
                      height={30}
                      className=" rounded-full"
                      style={{"aspectRatio": "1/1",
                }}
              />
                  <Image
                      src={icono2}
                      alt="Almuerzo"
                      width={30}
                      height={30}
                      className=" rounded-full"
                      style={{"aspectRatio": "1/1",
                }}
              />
                  <Image
                      src={icono3}
                      alt="Almuerzo"
                      width={30}
                      height={30}
                      className=" rounded-full"
                      style={{"aspectRatio": "1/1",
                }}
              />
                  <Image
                      src={icono4}
                      alt="Almuerzo"
                      width={30}
                      height={30}
                      className=" rounded-full"
                      style={{"aspectRatio": "1/1",
                }}
              />
                    </section>     
                    <h1 className='text-2xl pb-5'><strong>El cocinero recomienda</strong></h1>     
                    <li className='flex gap-3'>
                    <ul className='bg-white p-1 rounded-md'>cocina_Josefina</ul>
                    <ul className='bg-white p-1 rounded-md'>sarita_enCasa</ul>
                    <ul className='bg-white p-1 rounded-md'>Las delicias de rocio</ul>
                    <ul className='bg-white p-1 rounded-md'>Asados del oeste</ul>
                    </li>      
           </div>

        </div>   
    </div>
    </>
  )
}