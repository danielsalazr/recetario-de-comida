import React, {useState} from 'react'
import plato from '@/public/images/Carne-a-la-Criolla-Colombia.jpg';
import whatsapp from '@/public/images/whatsapp-48.png';
import Image from "next/image";
import { Inter } from "next/font/google";
import Header from "@/components/Header";



type Props = {
  
}

export default function ContainerRecipe({ 
  information,
}: Props) {

  const texto = information.recipe.ingredients //.replace(',','%2C').replace(' ','%20').replace(/\n/g,"%0A").split("%0A").map((linea) => "%E2%80%A2 " + linea).join()
  .replace("\r", "")
  .replace(/\n/g, "%0A")
  .replace(" ", "%20")
  .replace(" ", "%20")
  .replace(",", "%2C")
  .split("%0A")
  // .map((linea) => "%E2%80%A2%20" + linea)
  .map((linea, index) => index+1 + "%20" + linea)
  .join("%0A");
  console.log(texto);

  // const receta =
  
  return (
    <>
      <main className='flex flex-col items-center mt-0'>

        {/* <div> Resto de la app</div> */}

        {/* <div className=''
              style={{
                "background": 'linear-gradient(90deg, rgba(255,69,0,1) 10%, rgba(255,215,0,1) 49%, rgba(50,205,50,1) 65%, rgba(255,165,0,1) 86%)',
                'height': '100px',
                'width': '100%'
              
              }}
            ></div> */}

        {/* <div className=' '> */}
        <div className=' flex justify-center items-center w-full  px-4 py-2'>
          <div className='grid md:grid-cols-2 grid-cols-1 px-4 w-full max-w-7xl'>
            <div className='border border-black p-4 rounded-tl-lg'>
              <strong className="text-2xl">Ingredientes</strong>
              <hr className="mt-2 border-t-2  border-red-400" />
              {/* <ul className='list-outside list-disc mt-3 ms-8 leading-7 text-lg'>

                <li>2x Huevos</li>
                <li>1Lb de arroz</li>
                <li>100gr de Harina</li>
                <li>1tallo de cebolla larga</li>
                <li>1 tomate chonto</li>
                <li>100 gr de Sal</li>
              </ul> */}
              
              <p>
              <ul className='list-outside list-decimal mt-3 ms-8 leading-7 text-lg'>
                { information?.recipe ?   (
                
                  information.recipe.ingredients.split('\n').map( (line) => (
                    <li>{line}</li>
                ))
                ) : 'none'}
                </ul>
              </p>
              <a href={`https://wa.me/send?text=Receta%3A%0A${texto}`} target="_blank"><button className='text-white mt-6 ms-4 border py-2 px-4 rounded-lg text-xl' style={{ "background": '#2FC613' }}>Enviar receta  <Image
                src={whatsapp}
                alt="Vercel Logo"
                className="inline rounded-tr-lg "

                width={20}
                height={20}
                priority
              />
              </button></a>

            </div>
            <div className='border border-black rounded-tr-lg '>
              <Image
                src={information?.images ? `http://127.0.0.1:8000/media/${information.images[0].image}` : ''}
                alt="Vercel Logo"
                className="dark:invert rounded-tr-lg"
                width={600}
                height={600}
                priority
              />
            </div>
            <div className='border border-black col-span-1 md:col-span-2 rounded-b-lg p-4'>
              <strong className='text-2xl p-3'>Receta</strong>
              <hr className="mt-2 border-t-2  border-amber-500 mt-5" />
              <p className='mt-3 px-10 py-3'>
                <ol className='list-outside list-decimal mt-3 ms-8 leading-7 text-lg' type="1">
                  { information?.recipe ?   (
                  
                    information.recipe.description.split('\n').map((linee) => (
                      <li>{linee}</li>
                    ))
                    ) : 'none'}
                </ol>
                
                {/* {information?.recipe ?   information.recipe.description : '' } */}
                
              </p>
              
            </div>
          </div>
          <div></div>

          
        </div>
        {/* </div> */}

      </main>
    </>
  )
}