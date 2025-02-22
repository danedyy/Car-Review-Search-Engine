'use client';

import { useSearchParams, useParams, useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import { getDocumentById, moreLikeThis } from '../../api/api';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export default function CarDetails() {
  const params = useParams();
  const searchParams = useSearchParams();
  const router = useRouter();
  const [carDetails, setCarDetails] = useState(null);
  const [relatedCars, setRelatedCars] = useState([]);

  const name = decodeURIComponent(params.name);
  const info = Object.fromEntries(searchParams.entries());
  const document_id = info.document_id;
  const relevant_field = info.relevant_field;

  useEffect(() => {
    console.log("The document id is: ", document_id);
    console.log("The relevant field is: ", relevant_field);

    getDocumentById(document_id).then((data) => {
      const car = data.docs.find(doc => doc.Name === name);
      setCarDetails(car);
      console.log('Car details:', car);
      moreLikeThis(car.id, relevant_field).then((data) => {
        setRelatedCars(data.docs.slice(0, 3)); // Get the first 3 related cars
      });
    }).catch((error) => {
      console.error('Error querying Solr:', error);
    });
  }, [name, document_id, relevant_field]);

  if (!carDetails) {
    return (
      <div className="flex justify-center items-center h-screen bg-gray-100">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-indigo-500"></div>
      </div>
    );
  }

  const features = [
    { title: 'Rating', content: carDetails.Rating },
    { title: 'Price Feature', content: carDetails.Price_Feature },
    { title: 'Design Feature', content: carDetails.Design_Feature },
    { title: 'Practicality Feature', content: carDetails.Practicality_Feature },
    { title: 'Under the Bonnet Feature', content: carDetails.Under_Bonnet_Feature },
    { title: 'Efficiency Feature', content: carDetails.Efficiency_Feature },
    { title: 'Driving Feature', content: carDetails.Driving_Feature },
    { title: 'Safety Feature', content: carDetails.Safety_Feature },
    { title: 'Ownership Feature', content: carDetails.Ownership_Feature },
  ];

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto bg-white shadow-xl rounded-lg overflow-hidden">
        <div className="bg-black px-6 py-4">
          <div className="flex items-center justify-between">
            <button onClick={() => router.back()} className="text-white hover:text-indigo-100 transition duration-150 ease-in-out">
              <ArrowLeft className="h-6 w-6" />
            </button>
            <h1 className="text-2xl font-bold text-white text-center flex-grow">{carDetails.Name}</h1>
            <div className="w-6"></div>
          </div>
        </div>
        <div className="px-6 py-8">
          <div className="mb-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-2">Source</h2>
            <Link href={carDetails.URL[0]} className="text-indigo-600 hover:text-indigo-800 transition duration-150 ease-in-out">
              {carDetails.URL[0]}
            </Link>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {features.map((feature, index) => (
              <div key={index} className="bg-gray-50 rounded-lg p-4 shadow">
                <h2 className="text-lg font-semibold text-gray-800 mb-2">{feature.title}</h2>
                <p className="text-gray-600">{feature.content}</p>
              </div>
            ))}
          </div>
          <div className="mt-12">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">Related Cars</h2>
            <ul className="space-y-2">
              {relatedCars.map((relatedCar) => (
                <li key={relatedCar.id} className="bg-indigo-50 rounded-lg p-3 transition duration-150 ease-in-out hover:bg-indigo-100">
                  <Link 
                    href={`/car/${encodeURIComponent(relatedCar.Name)}?${new URLSearchParams({ document_id: relatedCar.id, relevant_field }).toString()}`}
                    className="text-indigo-600 hover:text-indigo-800 font-medium"
                  >
                    {relatedCar.Name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

