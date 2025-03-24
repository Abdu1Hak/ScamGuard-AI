"SENTIMENT ANALYSIS"

from transformers import pipeline
# Pipeline a simple API dedicated object 

class SentimentAnalysis:

    def __init__(self):
        self.classifier  = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
        self.weights = {
            'fear': 0.45,
            'surprise': 0.25,
            'anger': 0.15,
            'joy': 0.10, 
            'sadness': -0.10,
            'love': -0.15
        }
        self.maximum_possible_score = 0.95

    def scam_score(self, text):
        predictions = self.classifier(text)[0]

        categorical_scores = {}
        for item in predictions:
            label = item['label']
            score = item['score']
            categorical_scores[label] = score # append the new label with scores
        
        scores = []

        for emotion, weight in categorical_scores.items():
            score = categorical_scores[emotion]*weight
            scores.append(score)
        
        sum_score = sum(scores)
        normalized_score = (sum_score/self.maximum_possible_score)*100
        scam_percent = max(0, normalized_score)

        return int(scam_percent), categorical_scores


