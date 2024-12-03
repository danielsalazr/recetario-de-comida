import React from 'react'
import { useState } from 'react';
import Image from 'next/image';
import ContainerRecipe from '@/components/ContainerRecipe';
import sopa from '@/public/images/soup.png';
// import foto from '@/public/Jo_script_black.webp'


interface ModalProps {
    Contenedor: React.ElementType;
    items?: any[];
    validacion?: boolean;
    isOpen: boolean;
    closeModal: () => void;

}

const Modal: React.FC<ModalProps> = ({ isOpen, closeModal, information}) => { //({ Contenedor, items, validacion, isOpen, closeModal }) => {
    
    console.log(information)


    return (
        <>
            {/* Overlay */}
            <div
                className="modal-overlay"
                aria-hidden="true"
            // onClick={closeModal}
            />
            <div className="modal-container">
                <div className="modal-box overflow-y-scroll">
                    <div className="modal-header">
                        <Image
                            // src={sopa}
                            alt="Logo"
                            width={100}
                            height={40}

                        />
                        <button
                            onClick={closeModal}
                            className="modal-close-btn"
                        >
                            <svg
                                className="h-6 w-6"
                                fill="none"
                                stroke="currentColor"
                                viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M6 18L18 6M6 6l12 12"
                                />
                            </svg>
                        </button>
                    </div>
                    <div className="modal-body">
                        {/* <Contenedor items={items} validacion={validacion} /> */}
                        <ContainerRecipe 
                            information={information}
                        />
                    </div>

                </div>
            </div>
        </>
    )
}


export default Modal