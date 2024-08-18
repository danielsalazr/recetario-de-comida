import React from 'react'
import Image from "next/image";
import Link from 'next/link';

import almuerzos from '@/public/images/almuerzos.jpg';
import desayunos from '@/public/images/desayunos.jpg';
import cenas from '@/public/images/cenas.jpg';
import refrigerios from '@/public/images/refrigerios.jpg';
import bebidas from '@/public/images/bebidas.jpg';


type Props = {}

function Recetas({}: Props) {
  return (
    <div className="max-w-container py-0 md:py-8">
        <div className="flex flex-col  flex-container justify-center items-center mx-auto max-w-7xl py-4 gap-x-4">
            <h2 className="text-3xl"><strong>¿Que te gustaria cocinar?</strong></h2>
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

            <div className='flex gap-8 mt-10'>
                <div className="py-4 ">
                    <Link href='/' className="text-center" style={{
                          "borderRadius": "50%",
                          // "aspectRatio": "1/1"
                        }}>
                      <Image
                        src={desayunos}
                        alt="Vercel Logo"
                        className=""
                        width={180}
                        height={180}
                        priority
                        style={{
                          "borderRadius": "50%",
                          "aspectRatio": "1/1"
                        }}
                      />

                      <p className="text-2xl m-3"><strong>Desayunos</strong></p>
                    </Link>
                </div>

                <div className="py-4 ">
                    <Link href='/' className="text-center" style={{
                          "borderRadius": "50%",
                          // "aspectRatio": "1/1"
                        }}>
                      <Image
                        src={almuerzos}
                        alt="Vercel Logo"
                        className=""
                        width={180}
                        height={180}
                        priority
                        style={{
                          "borderRadius": "50%",
                          "aspectRatio": "1/1"
                        }}
                      />

                      <p className="text-2xl m-3"><strong>Almuerzos</strong></p>
                    </Link>
                </div>

                <div className="py-4 ">
                    <Link href='/' className="text-center" style={{
                          "borderRadius": "50%",
                          // "aspectRatio": "1/1"
                        }}>
                      <Image
                        src={cenas}
                        alt="Vercel Logo"
                        className=""
                        width={180}
                        height={180}
                        priority
                        style={{
                          "borderRadius": "50%",
                          "aspectRatio": "1/1"
                        }}
                      />

                      <p className="text-2xl m-3"><strong>Cenas</strong></p>
                    </Link>
                </div>

                <div className="py-4 ">
                    <Link href='/' className="text-center" style={{
                          "borderRadius": "50%",
                          // "aspectRatio": "1/1"
                        }}>
                      <Image
                        src={refrigerios}
                        alt="Vercel Logo"
                        className=""
                        width={180}
                        height={180}
                        priority
                        style={{
                          "borderRadius": "50%",
                          "aspectRatio": "1/1"
                        }}
                      />

                      <p className="text-2xl m-3"><strong>Refrigerios</strong></p>
                    </Link>
                </div>
                <div className="py-4 ">
                    <Link href='/' className="text-center" style={{
                          "borderRadius": "50%",
                          // "aspectRatio": "1/1"
                        }}>
                      <Image
                        src={bebidas}
                        alt="Vercel Logo"
                        className=""
                        width={180}
                        height={180}
                        priority
                        style={{
                          "borderRadius": "50%",
                          "aspectRatio": "1/1"
                        }}
                      />

                      <p className="text-2xl m-3"><strong>Bebidas</strong></p>
                    </Link>
                </div>
            </div>

            
            
        </div>
        <hr />
    </div>
  )
}

export default Recetas