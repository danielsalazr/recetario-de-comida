import React from 'react'
import plato from '@/public/images/Carne-a-la-Criolla-Colombia.jpg';
import whatsapp from '@/public/images/whatsapp-48.png';
import Image from "next/image";
import { Inter } from "next/font/google";
import Header from "@/components/Header";


type Props = {}

export default function ContainerRecipe({}: Props) {
  return (
    <>
        <main className='flex flex-col items-center mt-3'>
            <form action=""> 
              <div className="flex justify-center mt-8">
                <input
                    type="text"
                    //value={query}
                    //onChange={handleInputChange}
                    placeholder="Search..."
                    className=" px-4 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-lime-500"
                />
                <button
                    //onClick={handleSearch}
                    className="px-4 py-2 bg-lime-500 text-white rounded-r-md hover:bg-lime-600 focus:outline-none focus:ring-2 focus:ring-lime-500"
                > Search</button>
              </div>
            </form>
            {/* <div> Resto de la app</div> */}
            
            {/* <div className=''
              style={{
                "background": 'linear-gradient(90deg, rgba(255,69,0,1) 10%, rgba(255,215,0,1) 49%, rgba(50,205,50,1) 65%, rgba(255,165,0,1) 86%)',
                'height': '100px',
                'width': '100%'
              
              }}
            ></div> */}

            {/* <div className=' '> */}
                <div className=' flex justify-center items-center w-full  px-4 py-6'>
                    <div className='grid md:grid-cols-2 grid-cols-1 px-4 w-full max-w-7xl'>
                        <div className='border border-black p-6 rounded-tl-lg '>
                          <strong className="text-2xl">Ingredientes</strong>
                          <hr className="mt-2 border-t-2  border-amber-500 mt-5" />
                            <ul className='list-outside list-disc mt-5 ms-8 leading-8 text-lg '>

                              <li>2x Huevos</li>
                              <li>1Lb de arroz</li>
                              <li>100gr de Harina</li>
                              <li>1tallo de cebolla larga</li>
                              <li>1 tomate chonto</li>
                              <li>100 gr de Sal</li>
                            </ul>

                            <a href="https://wa.me/send?text=Hola%2C%20Esteban%20Esta%20es%20la%20Receta"><button className='text-white mt-6 ms-4 border py-2 px-4 rounded-lg text-xl' style={{"background": '#2FC613'}}>Enviar receta  <Image
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
                                src={plato}
                                alt="Vercel Logo"
                                className="dark:invert rounded-tr-lg"
                                // width={32}
                                // height={32}
                                priority
                            />
                            </div>
                        <div className='border border-black col-span-1 md:col-span-2 rounded-b-lg p-6'>
                            <strong className='text-2xl p-3'>Receta</strong>
                            <hr className="mt-2 border-t-2  border-amber-500 mt-5" />
                            <p className='mt-3 px-10 py-6'>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et lacinia ipsum. Proin quis magna ac risus vulputate rhoncus. Duis ac mi ac justo scelerisque malesuada. Aenean vulputate ante quam, auctor maximus purus pulvinar quis. Donec ex mi, fermentum et mauris non, viverra iaculis massa. Integer in sem hendrerit, tempus nunc sit amet, efficitur sapien. Quisque commodo sem magna, vel ultricies nisl tincidunt ac. Suspendisse lacinia id sapien vel consequat.
                            </p>
                            <p className='mt-3 px-10 '>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et lacinia ipsum. Proin quis magna ac risus vulputate rhoncus. Duis ac mi ac justo scelerisque malesuada. Aenean vulputate ante quam, auctor maximus purus pulvinar quis. Donec ex mi, fermentum et mauris non, viverra iaculis massa. Integer in sem hendrerit, tempus nunc sit amet, efficitur sapien. Quisque commodo sem magna, vel ultricies nisl tincidunt ac. Suspendisse lacinia id sapien vel consequat.
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