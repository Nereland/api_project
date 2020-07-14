
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def analysis(x):
    sia = SentimentIntensityAnalyzer()
    result = sia.polarity_scores(str(x).strip('[]'))
    return result