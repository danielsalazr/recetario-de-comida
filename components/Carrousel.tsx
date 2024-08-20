// import React from 'react';
"use client";
import aplastado from '@/public/images/aplastado.jpeg';
import quesadilla_con_pan from '@/public/images/quesadilla_con_pan.jpg';
import Image from "next/image";
import { Carousel } from 'flowbite-react';

type Props = {}

export default function Carrousel({}: Props) {
  return (
    <div className="w-full h-96  max-w-container  px-4 py-6 sm:px-6 xl:px-8">
      <Carousel slideInterval={3000} pauseOnHover className="h-full max-w-container mx-auto max-w-7xl transition duration-1000 ease-in-out transform">
        <Image src={aplastado} alt="..."  />
        <Image src={quesadilla_con_pan} alt="..."  />
        {/* <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." /> */}
      </Carousel>
    </div>
  )
}