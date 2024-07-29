import React from 'react';
import sopa from '@/public/images/soup.png';
import Image from "next/image";
import Link from 'next/link';

type Props = {}

export default function Header({}: Props) {
  return (
    <header className='Header'>
        <div className='Header__Container mx-auto max-w-container flex justify-between max-w-7xl px-4 py-6 sm:px-6 xl:px-8'>
            <div className='Header__logoAndToggle'>
                <a href="/" className="flex gap-x-4 items-center">
                    <Image
                        src={sopa}
                        alt="Vercel Logo"
                        className="dark:invert"
                        width={32}
                        height={32}
                        priority
                    />
                    <span className='text-2xl'>FoodColombia</span>

                </a>
            </div>
            <div className='Header__nav hidden md:flex'>
                <nav className='flex items-center'>
                    <ul className='flex gap-x-6 items-center'>
                    {/* <Link href="/about" legacyBehavior> <a >About</a> </Link> */}
                        <Link href="/recipes" legacyBehavior><li className='text-xl'><a href="">Recetas</a></li></Link>
                        <Link href="/recipes/ver-recetas" legacyBehavior><li className='text-xl'><a href="">Aportar</a></li></Link>
                        <Link href="/about" legacyBehavior><li className='text-xl'><a href="">Comunidad</a></li></Link>
                        <Link href="/about" legacyBehavior><li className='text-xl'><a href="">Login</a></li></Link>
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