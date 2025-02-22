'use client';

import { useState, useEffect } from 'react';
import SearchResult from './SearchResult';
import { querySolr, geminiReRank } from '../app/api/api';

export default function CarSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [lastQuery, setLastQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedBrand, setSelectedBrand] = useState('');
  const resultsPerPage = 10;

  useEffect(() => {
    const storedQuery = sessionStorage.getItem('query');
    const storedResults = sessionStorage.getItem('results');
    const storedLastQuery = sessionStorage.getItem('lastQuery');
    const storedCurrentPage = sessionStorage.getItem('currentPage');

    if (storedQuery && storedResults && storedLastQuery && storedCurrentPage) {
      setQuery(storedQuery);
      setResults(JSON.parse(storedResults));
      setLastQuery(storedLastQuery);
      setCurrentPage(parseInt(storedCurrentPage, 10));
    }
  }, []);

  const handleSearch = async (e) => {
    e.preventDefault();
  
    querySolr(query).then((data) => {
      geminiReRank(data.docs, query).then((response) => {  
        // Parse the Gemini output to extract the ordered list of car names
        const orderedCarNames = response["re_ranked_cars"].match(/'([^']+)'/g).map(name => name.replace(/'/g, ''));
  
        // Create a mapping from car names to Solr documents
        const carNameToDocMap = data.docs.reduce((map, doc) => {
          map[doc.Name] = doc;
          return map;
        }, {});
  
        // Re-order the Solr documents based on the Gemini output
        const reorderedDocs = orderedCarNames.map(name => carNameToDocMap[name]);
        
        setResults(reorderedDocs);
        setLastQuery(query);
        setCurrentPage(1); // Reset to first page on new search
        setSelectedBrand(''); // Reset the brand filter
  
        // Store the search results and query in sessionStorage
        sessionStorage.setItem('query', query);
        sessionStorage.setItem('results', JSON.stringify(reorderedDocs));
        sessionStorage.setItem('lastQuery', query);
        sessionStorage.setItem('currentPage', '1');
  
        console.log('Results:', reorderedDocs);
      });
    });
  };

  const truncateText = (text, maxLength) => {
    if (text.length <= maxLength) return text;
    const truncated = text.substr(0, maxLength);
    return truncated.substr(0, truncated.lastIndexOf('.') + 1) || truncated;
  };

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
    sessionStorage.setItem('currentPage', pageNumber.toString());
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll to the top of the page
  };

  const indexOfLastResult = currentPage * resultsPerPage;
  const indexOfFirstResult = indexOfLastResult - resultsPerPage;
  const currentResults = results.slice(indexOfFirstResult, indexOfLastResult);

  const uniqueBrands = [...new Set(results.map(result => result.Brand[0]))];

  const filteredResults = selectedBrand
    ? results.filter(result => result.Brand[0] === selectedBrand)
    : results;

  return (
    <div className="w-full max-w-2xl mx-auto p-4">
      <form onSubmit={handleSearch} className="flex flex-col items-center gap-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for cars..."
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-300"
        />
        <button 
          type="submit" 
          className="w-full px-4 py-2 text-white bg-black rounded-md hover:bg-white hover:text-black hover:border-2 hover:border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all duration-200"
        >
          Search
        </button>
      </form>
      {results.length > 0 && (
        <div>
          <h2 className="text-xl py-2 font-semibold mb-2">
            Search results for: <span className="font-normal">"{lastQuery}"</span>:
          </h2>

          <div className="mb-4">
            <label htmlFor="brandFilter" className="mr-2">Filter by brand:</label>
            <select
              id="brandFilter"
              value={selectedBrand}
              onChange={(e) => setSelectedBrand(e.target.value)}
              className="border border-gray-300 rounded-md px-2 py-1"
            >
              <option value="">All Brands</option>
              {uniqueBrands.map((brand, index) => (
                <option key={index} value={brand}>{brand}</option>
              ))}
            </select>
          </div>

          {filteredResults.slice(indexOfFirstResult, indexOfLastResult).map((result, index) => (
            <SearchResult
              key={index}
              name={result.Name}
              document_id={result.id}
              relevant_field={result.relevant_field}
              url={result.URL}
              description={truncateText(result["description"], 300)}
            />
          ))}

          <div className="flex justify-center mt-4">
            {Array.from({ length: Math.ceil(filteredResults.length / resultsPerPage) }, (_, index) => (
              <button
                key={index}
                onClick={() => handlePageChange(index + 1)}
                className={`px-4 py-2 mx-1 border rounded-md ${currentPage === index + 1 ? 'bg-black text-white' : 'bg-white text-black'}`}
              >
                {index + 1}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}