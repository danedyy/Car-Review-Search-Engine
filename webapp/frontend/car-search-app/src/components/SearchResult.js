'use client';

import Link from 'next/link';

export default function SearchResult({ name, document_id, url, description, relevant_field }) {
  
  const queryString = new URLSearchParams({ document_id, relevant_field }).toString();

  return (
    <div className="mb-4">
      <Link
        href={`/car/${encodeURIComponent(name)}?${queryString}`}
        className="text-blue-600 hover:underline text-lg cursor-pointer"
      >
        {name}
      </Link>
      <p className="text-green-700 text-sm">{url}</p>
      <p className="text-sm text-gray-600">{description}</p>
    </div>
  );
}
