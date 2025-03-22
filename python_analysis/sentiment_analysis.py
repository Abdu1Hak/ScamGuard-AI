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



"""
CODE EXPLANATION:

- Used transformers and a specific model to return the presence of 6 of the most common emotions prevelant in Scam Messages
- Using research and statistical Data, I assigned weights to each category:
    - Reasoning ->
        - Fear is the Primary Scam Emotion (invoke urgency and threats): 0.45
        - Surprise is the second highest, creating a sense of anxiety: 0.25
        - Anger is used mildly in threats/coercions: 0.15
        - Joy are rarely found in the too good to be true offers: 0.10
        - Sadness is almost never found in correlation with scams: -0.10
        - Love is the most overlapping factor in all message types: -0.15

- Now the max possible score is 0.95 (if only positive emotions are present) and the minimum is -0.25 (if negatives are only present)
- After retrieving the sum of all the scores present, it is normalized by dividing against the maximum existing possibility
- Finally in the case that a negative score is returned, we return 0 instead. 


- An emotional analysis isnt nearly accurate nor comprehensive indicator of a scam message, however it offers a few benefits:
    - Informs us the exact abundance of strong emotions
    - Useful decider when it comes to edge cases
    - Only contributes 10-15% to the Final Probability Score
"""