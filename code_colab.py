Install Required Libraries

# ✅ Install required libraries
!pip install -q textblob

Download Required NLTK Data

# ✅ Download required NLTK data
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


Import Required Modules

# ✅ Import modules
from textblob import TextBlob


Define Sentiment Analysis Function

# ✅ Function to analyze sentiment
def analyze_sentiment(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity

    # Return only Positive or Negative
    if polarity > 0:
        return "Positive 😊"
    else:
        return "Negative 😞"


Get User Input & Show Output

# ✅ Test: Ask user for sentence input
while True:
    sentence = input("\nEnter your sentence (or type 'exit' to stop): ")
    if sentence.lower() == 'exit':
        print("Goodbye!")
        break
    elif sentence.strip() == "":
        print("Please type something!")
        continue
    else:
        result = analyze_sentiment(sentence)
        print(f"Sentiment: {result}")


Required nltk downloads:


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
