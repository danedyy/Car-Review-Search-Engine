'use client';

import CarSearch from '../components/CarSearch';

export default function Home() {

  const handleTitleClick = () => {
    // Clear session storage and refresh the page
    sessionStorage.clear();
    window.location.reload();
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-white text-black">
      <h1 
        className="mb-4 text-4xl font-bold cursor-pointer"
        onClick={handleTitleClick}
      >
        Car Search Engine
      </h1>
      <CarSearch />
    </main>
  );
}