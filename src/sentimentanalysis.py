
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def analysis(x):
    sia = SentimentIntensityAnalyzer()
    result = sia.polarity_scores(str(x).strip('[]'))
    if result["neg"]>result["pos"]:
        return "mostly unhappy: negative polarity", "negative:", result["neg"], "positive", result["pos"]
    elif  result["neg"]<result["pos"]:
        return "mostly happy: positive plolarity", result["neg"], result["pos"]
    else:
        return "neutral or too mixed", "neutral:", result["neu"], "compound:", result["compound"]
