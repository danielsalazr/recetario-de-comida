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
import ajiaco from '@/public/images/ajiaco.jpg';
import hayacas from '@/public/images/hayacas.jpg';
import caldodehuevo from '@/public/images/caldodehuevo.jpg';
import pataconesconperico from '@/public/images/pataconconpericos.jpg';
import pataconropavieja from '@/public/images/pataconropavieja.jpg';
import pataconmixto from '@/public/images/pataconmixto.jpg';
import mute from '@/public/images/mute.jpg';
import sobrebarriga from '@/public/images/sobrebarriga.jpg';
import lenguaensalsa from '@/public/images/lenguaensalsa.jpg';
import sardinasconarroz from '@/public/images/sardinasconarroz.jpg';
import champus from '@/public/images/champus.jpg';
import masato from '@/public/images/masato.jpg';
import tungodemaiz from '@/public/images/tungodemaiz.jpg';
import arepaeyuca from '@/public/images/arepaeyuca.jpg';
import cazuelademariscos from '@/public/images/cazuelademariscos.jpg';
import tapadodecorbinas from '@/public/images/tapadodecorbinas.jpg';
import ensaladadeconchas from '@/public/images/ensaladadeconchas.jpg';
import ensaladaverde from '@/public/images/ensaladaverde.jpg';
import frijoles from '@/public/images/frijoles.jpg';
import arepaconquesocuajada from '@/public/images/arepaconquesocuajada.jpg';
import pajarilla from '@/public/images/pajarilla.jpg';
import bistecdehigado from '@/public/images/bistecdehigado.jpg';
import chuletavalluna from '@/public/images/chuletavalluna.jpg';
import puntadeanca from '@/public/images/punta de anca.jpg';
import churrasco from '@/public/images/churrasco.jpg';
import aguapanela from '@/public/images/aguapanela.jpg';



type Props = {}

function Recetas({ }: Props) {

  const recetas = [

    {
      name: "Arroz Paisa",
      images: arrospaisa,
      author: "Daniel Salazar",
    },
    {
      name: "Canelones",
      images: canelones,
      author: "Daniel Salazar",
    },
    {
      name: "Pasta a la bolgnesa",
      images: pastabolognesa,
      author: "Daniel Salazar",
    },
    {
      name: "Huevos pericos",
      images: huevospericos,
      author: "Daniel Salazar",
    },
    {
      name: "Calentado",
      images: calentado,
      author: "Daniel Salazar",
    },
    {
      name: "Sandwich de atun",
      images: sandwichdeatun,
      author: "Daniel Salazar",
    },
    {
      name: "Michelada Mango biche",
      images: micheladamangobiche,
      author: "Daniel Salazar",
    },
    {
      name: "Ajiaco",
      images: ajiaco,
      author: "Daniel Salazar",
    },
    {
      name: "Hayacas",
      images: hayacas,
      author: "Daniel Salazar",
    },
    {
      name: "Caldo de huevo",
      images: caldodehuevo,
      author: "Daniel Salazar",
    },
    {
      name: "Patacon con huevos pericos",
      images: pataconesconperico,
      author: "Daniel Salazar",
    },
    {
      name: "Patacon ropa vieja",
      images: pataconropavieja,
      author: "Daniel Salazar",
    },
    {
      name: "Patacon Mixto",
      images: pataconmixto,
      author: "Daniel Salazar",
    },
    {
      name: "Mute",
      images: mute,
      author: "Daniel Salazar",
    },
    {
      name: "Sobre Barriga",
      images: sobrebarriga,
      author: "Daniel Salazar",
    },
    {
      name: "Lengua en salsa",
      images: lenguaensalsa,
      author: "Daniel Salazar",
    },
    {
      name: "Sardinas Con arroz",
      images: sardinasconarroz,
      author: "Daniel Salazar",
    },
    {
      name: "champus",
      images: champus,
      author: "Daniel Salazar",
    },
    {
      name: "masato",
      images: masato,
      author: "Daniel Salazar",
    },
    {
      name: "Tungo de maiz",
      images: tungodemaiz,
      author: "Daniel Salazar",
    },
    {
      name: "Arepa e yuca",
      images: arepaeyuca,
      author: "Daniel Salazar",
    },
    {
      name: "Cazuela de marizcos",
      images: cazuelademariscos,
      author: "Daniel Salazar",
    },
    {
      name: "Tapado de corbina",
      images: tapadodecorbinas,
      author: "Daniel Salazar",
    },
    {
      name: "Ensalada de Conchas",
      images: ensaladadeconchas,
      author: "ensaladadeconchas Salazar",
    },
    {
      name: "ensalada verde",
      images: ensaladaverde,
      author: "Daniel Salazar",
    },
    {
      name: "Frijoles",
      images: frijoles,
      author: "Daniel Salazar",
    },
    {
      name: "Arepa con queso cuajada",
      images: arepaconquesocuajada,
      author: "Daniel Salazar",
    },
    {
      name: "Pajarilla",
      images: pajarilla,
      author: "Daniel Salazar",
    },
    {
      name: "Bistec de higado",
      images: bistecdehigado,
      author: "Daniel Salazar",
    },
    {
      name: "Chuleta Valluna",
      images: chuletavalluna,
      author: "Daniel Salazar",
    },
    {
      name: "Punta de Anca",
      images: puntadeanca,
      author: "Daniel Salazar",
    },
    {
      name: "Churrasco",
      images: churrasco,
      author: "Daniel Salazar",
    },
    // {
    //   name: "Pollo con salsa champinones",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },
    // {
    //   name: "Pollo con salsa Chane",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },
    // {
    //   name: "Cordon Blue",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },
    // {
    //   name: "Arepa de Choclo",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },
    // {
    //   name: "Mazamorra con panela",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },
    {
      name: "Aguapanela",
      images: aguapanela,
      author: "Daniel Salazar",
    },
    // {
    //   name: "",
    //   images: arrospaisa,
    //   author: "Daniel Salazar",
    // },

  ]
  return (
    <div className="max-w-container py-0 md:py-8">
      <div className="flex flex-col justify-center items-center mx-auto max-w-7xl py-4 gap-x-4">
        <h2 className="text-3xl"><strong>Recetas recomendadas</strong></h2>
        <p>Donde cada bocado es una explosión de sabor.</p>
        <div className="grid gap-6 mt-6 mb-6  grid-cols-1 md:grid-cols-3 lg:grid-cols-5">


          {recetas.map(receta => (

            <div className="max-w-sm rounded overflow-hidden shadow-lg rounded-4">
              <div className="relative">
                <Image
                  src={receta.images}
                  alt="Almuerzo"
                  width={256}
                  height={256}
                  className=" object-cover"
                  style={{
                    "aspectRatio": "1/1",
                  }}
                />

                <div className="absolute w-full bottom-0 left-0   text-white p-2"
                  style={{
                    "background": "linear-gradient(0deg, rgba(0,0,0,0.4682247899159664) 20%, rgba(255,255,255,0.06206232492997199) 100%)"
                  }}>
                  <p className="font-bold">{receta.name}</p>
                  <p className="text-base">{receta.author}</p>
                </div>
              </div>
            </div>
          ))}






        </div >
      </div >
      <hr />
    </div >
  )
}

export default Recetas