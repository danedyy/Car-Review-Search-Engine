import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Path to the input CSV file
input_file = "cleaned_car_data.csv"

# Load the data from the CSV file
data = pd.read_csv(input_file)

# Combine the specified columns into a single string
columns_to_join = [
'Name','Brand'
]
combined_text = ' '.join(data[col].dropna().astype(str).str.cat(sep=' ') for col in columns_to_join)

# Split the string into words
words = re.findall(r'\b\w+\b', combined_text.lower())

# Define a list of stop words
stop_words = set([
'the', 'like', 'has', 'its', 'and', 'or', 'but', 'if', 'while', 'with', 
'a', 'an', 'of', 'to', 'in', 'on', 'for', 'by', 'at', 'from', 'as', 'is', 
'this', 'that', 'these', 'those', 'are', 'was', 'were', 'be', 'been', 
'being', 'have', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 
'should', 'can', 'could', 'may', 'might', 'must', 'am', 'is', 'are', 
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 
'did', 'will', 'would', 'shall', 'should', 'can', 'you', 'your', 'yours', 
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 
'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
'theirs', 'themselves', 'we', 'us', 'our', 'ours', 'ourselves', 'i', 
'me', 'my', 'mine', 'myself', 'what', 'which', 'who', 'whom', 'whose', 
'where', 'when', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 
'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 
'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'don', 
'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 
'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 
'there', 'wasn', 'weren', 'won', 'wouldn', 'here', 'also', 'features',
'lot', 'thing', 'things', 'good', 'bad', 'best', 'worst', 'more', 
'less', 'most', 'anymore', 'never', 'always', 'sometimes', 'maybe',
'really', 'actually', 'just', 'another', 'one', 'two', 'three', 'way', 
'way', 'much', 'such', 'even', 'too', 'seem', 'seemed', 'seems', 
'need', 'needed', 'want', 'wanted', 'think', 'thinks', 'thought', 
'come', 'comes', 'going', 'go', 'went', 'get', 'gets', 'better', 
'best', 'big', 'small', 'nice', 'pretty', 'cool', 'great', 'fine', 
'old', 'new', 'last', 'first', 'next', 'then', 'now', 'where', 
'when', 'why', 'how', 'any', 'each', 'many', 'few', 'some', 'all', 
'more', 'most', 'less', 'then', 'than', 'before', 'after', 'while',
'during', 'around', 'between', 'among', 'fewer', 'might', 'should',
'would', 'let', 'makes', 'make', 'like', 'such', 'go', 'goes', 
'gonna', 'need', 'want', 'could', 'might', 'should', 'would','xa0','0j'
])


# Filter out stop words and numbers
filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()