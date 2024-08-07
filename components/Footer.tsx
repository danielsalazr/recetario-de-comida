import React from 'react'

type Props = {}

export default function Footer({}: Props) {
  return (
    <footer className="pt-0 md:py-20 border-t">
        <div className="mx-auto max-w-container max-w-7xl px-4 py-6 sm:px-6 xl:px-8">
          <strong className="text-xl">FoodColombia</strong>
        </div>
    </footer>
  )
}