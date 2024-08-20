import React from 'react'
import Image from "next/image";
import Link from 'next/link';

import almuerzos from '@/public/images/almuerzos.jpg';
import desayunos from '@/public/images/desayunos.jpg';
import cenas from '@/public/images/cenas.jpg';
import refrigerios from '@/public/images/refrigerios.jpg';
import bebidas from '@/public/images/bebidas.jpg';
import arrospaisa from '@/public/images/arros_paisa.jpg';
import pastabolognesa from '@/public/images/pastabolognesa.jpg';
import canelones from '@/public/images/canelones.jpg';
import huevospericos from '@/public/images/huevospericos.jpg';
import calentado from '@/public/images/calentado.jpg';
import sandwichdeatun from '@/public/images/sandwichdeatun.jpg';
import micheladamangobiche from '@/public/images/micheladamangobiche.jpg';


type Props = {}

function Recetas({}: Props) {
  return (
    <div className="max-w-container py-0 md:py-8">
        <div className="flex flex-col justify-center items-center mx-auto max-w-7xl py-4 gap-x-4">
        <h2 className="text-3xl"><strong>Recetas recomendadas</strong></h2>
        <p>Donde cada bocado es una explosión de sabor.</p>
        <div className="grid gap-6 mt-6 mb-6  grid-cols-1 md:grid-cols-3 lg:grid-cols-5">

          {/* ///////////////////////////////// */}

          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={arrospaisa}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover "
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Arroz Paisa</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>

          {/* ////////////////////////////////////// */}


          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={canelones}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Canelones</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>

          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={pastabolognesa}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Pasta a la bolognesa</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>


          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={huevospericos}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Huevos pericos</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>

          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={calentado}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Calentado</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>

          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={sandwichdeatun}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Sandwich de atun</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>


          <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
            <div className="relative transition-transform duration-300 transform-gpu hover:scale-105 ">
              <Image
                src={micheladamangobiche}
                alt="Almuerzo"
                width={256}
                height={256}
                className=" object-cover"
                style={{"aspectRatio": "1/1",
                  
                }}
              />
              <div className="absolute w-full bottom-0 left-0   text-white p-2" 
              style={{
                "background" : "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
              }}>
                <p className="font-bold">Michelada mango biche</p>
                <p className="text-base">Daniel Salazar</p>
              </div>
            </div>
            
          </div>


        </div>
        </div>
        <hr />
    </div>
  )
}

export default Recetas