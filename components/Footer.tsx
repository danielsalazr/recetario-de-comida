import React from 'react'
import 'boxicons/css/boxicons.min.css';

type Props = {}

export default function Footer({}: Props) {
  return (
    <footer className="pt-0 md:py-20 border-t bg-amber-500 opacity-75">
        <div className="mx-auto flex justify-around max-w-7xl px-4 py-6 sm:px-6 xl:px-8">
          <div>
              <strong className="text-xl">FoodColombia</strong>
              <p>¡Disfruta de lo mejor de la cocina colombiana!</p>
              <br />
              <br />
              Siguenos en redes sociales:
              <br />
              <br />
              <div className='flex gap-x-2'>
                  <a href="#"><i className='bx bxl-facebook-square text-3xl'></i></a>
                  <a href="#"><i className='bx bxl-instagram text-3xl'></i></a>
                  <a href="#"><i className='bx bxl-tiktok text-3xl'></i></a>
                  <a href="#"><i className='bx bxl-youtube text-3xl'></i></a>
                  <a href="#"><i className='bx bxl-pinterest-alt text-3xl'></i></a>
              </div>
          </div>
          <div className=''>
            <strong>Sobre Nosotros</strong>
            <br />
            quienes somos
            <br />
            contacto

          </div>
          
        </div>
        <div className='text-center'>
          copyrigth &#169; 2024
        </div>
    </footer>
  )
}