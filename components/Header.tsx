import React from 'react';
import sopa from '@/public/images/ajiaco.png';
import Image from "next/image";
import Link from 'next/link';

type Props = {}

export default function Header({}: Props) {
  return (
    <header className='Header bg-amber-500 opacity-85 z-[-1] '>
        <div className='Header__Container mx-auto max-w-container flex justify-between max-w-7xl px-4 py-4 sm:px-6 xl:px-8 z-1'>
            <div className='Header__logoAndToggle'>
                <Link href="/" legacyBehavior>
                    <a href="" className="flex gap-x-4 items-center">
                        <Image
                            src={sopa}
                            alt="Vercel Logo"
                            className="dark:invert"
                            width={60}
                            height={60}
                            priority
                        />
                        <span className='text-2xl'><strong>Food</strong>Colombia</span>

                    </a>
                </Link>
            </div>
            <div className='Header__nav hidden md:flex'>
                <nav className='flex items-center'>
                    <ul className='flex gap-x-6 items-center '>
                    {/* <Link href="/about" legacyBehavior> <a >About</a> </Link> */}
                        <Link href="/recipes" legacyBehavior><li className='text-xl hover:text-white transition-colors'><a href="">Recetas</a></li></Link>
                        <Link href="/recipes/ver-recetas" legacyBehavior><li className='text-xl hover:text-white transition-colors'><a href="">Aportar</a></li></Link>
                        <Link href="/about" legacyBehavior><li className='text-xl hover:text-white transition-colors'><a href="">Comunidad</a></li></Link>
                        <Link href="/about" legacyBehavior><li className='text-xl hover:text-white transition-colors'><a href="">Login</a></li></Link>
                    </ul>
                </nav>
            </div>
            <div className='md:hidden flex items-center'>
            <button type="button" className="text-gray-500 hover:text-gray-700 focus:outline-none focus:text-gray-700">
                <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
            </button>
        </div>
        
        </div>
       
        <hr />
    </header>
  )
}