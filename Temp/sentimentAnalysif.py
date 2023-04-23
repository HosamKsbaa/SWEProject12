from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
text = ""
# Open the file for reading
with open('englishText.txt', 'r') as file:
    # Read the contents of the file
    text = file.read()

# Print the contents of the file
print(text, " is analyzed as: ")

# Create a SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# Analyze text
scores = analyzer.polarity_scores(text)

# Print the sentiment scores
print(scores)
