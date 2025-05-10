from flask import Flask, render_template, url_for, request, redirect, session
import re 
from flashtext import KeywordProcessor
from python_analysis.sentiment_analysis import SentimentAnalysis
from python_analysis.match_words import return_matching_words, risk_score
from python_analysis.ai_analysis import ai_analysis


# How to create a flask app
app = Flask(__name__) 
app.secret_key = 'my_key'


@app.route("/", methods=['GET']) 
def main():
    session.pop('suspicious_text', None) # Clear Previous Data
    return render_template('base.html',suspicious_text = session.get('suspicious_text', ''))
        

@app.route("/analyze", methods=['POST'])
def analyze():
    if request.method == "POST": # Analyze is Pressed
        session['suspicious_text'] = request.form['suspicious_text'] # Store
        session.modified=True # Update
        return redirect(url_for("results"))
    else:
        return redirect(url_for('main'))


@app.route("/results")
def results():
    
    suspicious_text = session.get('suspicious_text')

    if not suspicious_text:
        print("No text found in session!")
        return redirect(url_for("main"))

    # Sentiment Probability + Breakdown (Return Two Strong Emotion Indicators)
    sentiment_object = SentimentAnalysis()
    sentiment_score, sentiment_breakdown = sentiment_object.scam_score(suspicious_text)
        
    # Returns Matching Words + Probability
    scam_matching_words = return_matching_words(suspicious_text)
    scam_score = risk_score(suspicious_text, scam_matching_words)
       
    # Return AI Score + Reasoning
    ai_score, ai_reasoning, ai_keywords = ai_analysis(suspicious_text)
    
    # Weights
    ai_weight = 0.70
    sentiment_weight = 0.20
    matching_weight = 0.10
    
    # We are leveraging AI in cases where sentiment + matching analysis shows inaccuracy
    if ai_score > 80 and (scam_score < 50 or sentiment_score < 50) : # Shows High AI detenctance 
        ai_weight = 0.85
        sentiment_weight = 0.05
        matching_weight = 0.10 
    
    # Leverage AI incase no keywords were returned from scam, although AI score is high
    if ai_score > 50 and (scam_matching_words == []):
        scam_matching_words = ai_keywords
        with open('common_spam_words_2020.txt', 'a') as file:
            for word in scam_matching_words:
                file.write(word + '\n')

    # Final Score
    final_score = int((ai_score*ai_weight) + (matching_weight*scam_score) + (sentiment_weight*sentiment_score))

    # Work On Display Items
    top_two_emotions = []
    for emotion, score in sentiment_breakdown.items():
        if len(top_two_emotions) < 2: #empty
            top_two_emotions.append((emotion, score))
        else: 
            if score > top_two_emotions[0][1]:
                top_two_emotions = [(emotion, score)] + [top_two_emotions[0]]
            elif score > top_two_emotions[1][1]:
                top_two_emotions[1] = (emotion, score)
    
    # Sort by ascending order 
    if top_two_emotions[0][1] < top_two_emotions[1][1]:
        top_two_emotions[0], top_two_emotions[1] =  top_two_emotions[1],top_two_emotions[0]
    
    
    # 3 Display Items for User
    sentiment_display = f"{top_two_emotions[0][0].capitalize()}: {top_two_emotions[0][1]*100:.1f}%, {top_two_emotions[1][0].capitalize()}: {top_two_emotions[1][1]*100:.1f}%"
    keyword_display = "Detected Common Scam Words Such as: " + ", ".join(scam_matching_words)
    safe_keywords = "No Keywords Detected"

    variables = {
        'score': final_score,
        'reasoning': ai_reasoning,
        'keywords': scam_matching_words,
        'suspicious_text': suspicious_text,
        'emotions':sentiment_display,
        'keywords_display':keyword_display,
        'safe_keyowords_display': safe_keywords
    }
    
    
    return render_template('complete.html', variables=variables)



if __name__ == '__main__':
    app.run() # Production Mode
