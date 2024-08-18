import React from 'react'
import plato from '@/public/images/Carne-a-la-Criolla-Colombia.jpg';
import whatsapp from '@/public/images/whatsapp-48.png';
import Image from "next/image";
import { Inter } from "next/font/google";
import Header from "@/components/Header";
import ContainerRecipe from '@/components/ContainerRecipe';

// import { Container } from 'postcss';




type Props = {}

export default function index({}: Props) {
  return (
    <>
        <Header />
        
        <ContainerRecipe />

    </>
  )
}