import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const querySolr = async (userInput) => {
    try {
        console.log('Querying Solr:', userInput);
        const response = await axios.get(`${BASE_URL}/query_solr`, {
            params: { user_input: userInput }  
        });

        console.log(response.data);

        return response.data;
    } catch (error) {
        console.error('Error querying Solr:', error);
        throw error;
    }
};


export const getDocumentById = async (documentId) => {
    try {
        console.log('Getting document by ID:', documentId);
        const response = await axios.get(`${BASE_URL}/get_document_by_id`, {
            params: { document_id: documentId }
        });

        console.log(response.data);

        return response.data;
    } catch (error) {
        console.error('Error getting document by ID:', error);
        throw error;
    }
};


export const geminiReRank = async (documents, userInput) => {
    let prompt = `User query: ${userInput}\n\n`;

    documents.forEach(doc => {
        prompt += `Car: ${doc["Name"]}\n`;
        prompt += `Feature description: ${doc[doc["relevant_field"]]}\n\n`;
    });

    try {
        const response = await axios.get(`${BASE_URL}/gemini_re_rank`, {
            params: {query: prompt}
        });

        console.log(response.data);

        return response.data;
    } catch (error) {
        console.error('Error querying Solr:', error);
        throw error;
    }
};

export const moreLikeThis = async (documentId, fields) => {

    try {
        console.log('More like this:', documentId, fields);
        const response = await axios.get(`${BASE_URL}/more_like_this`, {
            params: { document_id: documentId, fields: fields }
        });

        console.log(response.data);

        return response.data;
    } catch (error) {
        console.error('Error querying Solr:', error);
        throw error;
    }
};

