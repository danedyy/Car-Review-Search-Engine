import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Path to the input CSV file
input_file = "cleaned_car_data.csv"

# Load the data from the CSV file
data = pd.read_csv(input_file)

# Extract the 'Name' column from the data
names = data['Name']

# Join all the names into a single string
all_names = ' '.join(names)

# Split the string into words
words = re.findall(r'\b\w+\b', all_names.lower())

# Count the frequency of each word
word_freq = Counter(words)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Car Names')
plt.show()