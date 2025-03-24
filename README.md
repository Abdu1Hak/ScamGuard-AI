ScamGuard-AI: AI-Powered Scam Detection System
Welcome to ScamGuard-AI!
This AI-based application provides an accurate way to determine the likelihood that a message is a scam. It does this by analyzing messages in three distinct ways to give you a well-rounded and precise result.

How It Works
Sentiment Analysis (20%)
The first step in the analysis process is Sentiment Analysis. We use a trained NLP model from Hugging Face to determine the top 2 emotions present in the message and their respective percentages.

Why does this matter?
Scam messages often rely on emotional manipulation, such as fear, urgency, and excitement, to trick people into acting impulsively. By understanding these emotions, we can better gauge whether the message might be a scam.

How we handle it:
Our model identifies six core emotions, which are weighted based on their relevance to scams. If the sentiment analysis results show low emotional manipulation but high AI analysis, we reduce its impact to just 5% of the overall risk score.

Word Search Analysis (10%)
Next, the system scans the message for common scam-related words using a public GitHub repository containing over 500 known scam keywords.

Why this works:
Scams often rely on certain keywords to convey urgency or pressure. By detecting these words, we can flag messages as potentially risky.

How we handle it:
The frequency of scam-related words in the message influences the scam likelihood. If no keywords are found but the AI analysis still flags the message as risky, we'll display suspicious keywords suggested by AI.

AI Analysis (70%)
The most significant part of the analysis is handled by Gemini 2.0 AI. This AI scans the text for fraudulent patterns, emotional manipulation, urgency, and impersonation.

Why it’s powerful:
Gemini 2.0 goes beyond simple word searches. It detects deeper scam indicators and provides a scam likelihood percentage with a short explanation of its findings.

How it works:
The AI's results contribute to 70% of the final scam likelihood score.

How the System Works Together
The three analyses—Sentiment Analysis, Word Search, and AI Analysis—combine to generate a scam likelihood score, which is then presented to the user. Here’s how the results are structured:

Scam Likelihood: A percentage indicating the likelihood that the message is a scam.

Suspicious Keywords: Keywords from the message that indicate potential fraud.

Threat Breakdown: A detailed explanation of why the message is flagged, based on all three analysis methods.

This system is carefully integrated using Flask to handle routing and API requests.

Personal Motivation and Purpose
Unlike a standard project, this application was created out of a personal experience—I received 4 scam messages in a single day. This motivated me to build a tool that could solve this problem while showcasing my skills in backend development, frontend design, and API integration.

Experience It Yourself!
You can test ScamGuard-AI live on Render:
🔗 Try ScamGuard-AI

If the link doesn’t work, here are screenshots of the UI for reference.

Tech Credits
Scam Keywords GitHub: The common scam keywords used in the word search are sourced from this GitHub repository.

We plan to expand and refine this list, especially in cases where no keywords are detected but the AI still flags the message as suspicious.

 
