# ScamGuard-AI: AI-Powered Scam Detection System

**Welcome to ScamGuard-AI!**  
This AI-based application provides an accurate way to determine the likelihood that a message is a scam. It does this by analyzing messages in three distinct ways to give you a well-rounded response. Unlike a standard project, this application was created out of a **personal experience**—I received **5 scam messages** in a single day, Ridiculous! This motivated me to craft a solution using what I'm equally passionate about and skilled in: code. 

---
**Tech**
- Backend: Python, Flask
- Frontend: HTML/CSS, Vanilla JS
- API & Libraries: Huggingface pipeline/transformers, Gemini 2.0 Flash API, Render

## 🛠️ Tech Stack

<div align="center">

### **Backend**
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)

### **Frontend** 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?logo=javascript&logoColor=black)

### **APIs & AI**
![HuggingFace](https://img.shields.io/badge/HuggingFace-Pipelines-FFD21E?logo=huggingface&logoColor=black)
![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-API-4285F4?logo=google-cloud&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube_API-v3-FF0000?logo=youtube&logoColor=white)

### **ML/NLP**
![Transformers](https://img.shields.io/badge/🤗_Transformers-4.30%2B-FFD21E?logo=huggingface&logoColor=black)

### **Infrastructure**
![Render](https://img.shields.io/badge/Render-Cloud_Deploy-46E3B7?logo=render&logoColor=white)

### **Data**
![Pandas](https://img.shields.io/badge/Pandas-2.1%2B-150458?logo=pandas&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-API-34A853?logo=google-sheets&logoColor=white)

</div>

---

### **How It Works**

1. **Sentiment Analysis (20%)**  
   The first step in the analysis process is **Sentiment Analysis**. I used a trained **NLP model** from Hugging Face to determine the **top 2 emotions** present in the message with their respective percentages.  
   - **Why does this matter?**  
     Scam messages rely heavily on **emotional manipulation**, such as fear, urgency, and excitement, to trick people into acting impulsively. By identifying these emotions, we can better gauge whether the message might be a scam.  
   - **How ScamGuard handles it:**  
     The model identifies six core emotions, which are weighted based on their relevance to scams. If the sentiment analysis results show low emotional manipulation but high AI analysis, we adjust its impact to just **5%** of the overall likelihood score.  

2. **Word Search Analysis (10%)**  
   The system scans the message for common scam-related words using a **public GitHub repository** containing over **500 known scam keywords**.  
   - **Why this works:**  
     Scams rely on suspicious keywords to convey urgency or pressure. By detecting these words, we can flag messages as risky.  
   - **How ScamGuard handles it:**  
     The frequency of scam-related words in the message influences the **scam likelihood**. The response also supports a scaling mechanism to avoid disproportionality in weighing these keywords. If no keywords are found but the AI analysis response is high, the **suspicious keywords** suggested by AI are then displayed

3. **AI Analysis (70%)**  
   The most significant part of the analysis is handled by **Gemini 2.0 AI**. This AI scans the text for **fraudulent patterns**, **emotional manipulation**, **urgency**, and **impersonation of trusted entities**.  
   - **Why it’s powerful:**  
     Gemini 2.0 goes beyond simple word searches. It detects deeper **scam indicators** and returns a **scam likelihood percentage** with a **short explanation** of its findings.  
 

---

### **How the System Works Together**

The three analyses—**Sentiment Analysis**, **Word Search**, and **AI Analysis**—combine to generate a **scam likelihood** score, which is  presented to the user. Here’s how the results are structured:

- **Scam Likelihood:** A percentage indicating the scam likelihood.
- **Suspicious Keywords:** Keywords from the message that are immediately red-flagged.
- **Threat Breakdown:** A well-rounded explanation of the message, based on all three analysis methods.
- **Tip:** Keep In Mind, anything below 20% is not considered a threat, between 20%-60% entertains a possibility but minimal threat, however, above 60% > is highly risky

---

### **Credits**

- **Scam Keywords GitHub:** The common scam keywords used in the word search are sourced from this [GitHub repository](https://gist.github.com/prasidhda/13c9303be3cbc4228585a7f1a06040a3).  
- This app is set to **expand and refine** this list, especially in cases where no keywords are detected but the AI still flags the message as suspicious.

---

 ### **Experience It Yourself!**

You can test ScamGuard-AI live on **Render**:  
🔗 [Try ScamGuard-AI](https://scamguard-ai.onrender.com)

If the link doesn’t work, here are screenshots of the **UI** for reference.

---

![image](https://github.com/user-attachments/assets/d093c20f-9a22-4a74-9160-80695a39e726)

Tested against a typical scam message that prompts user to click on link and asks for info:

![image](https://github.com/user-attachments/assets/ea442f4d-cede-4ea2-b11f-6b5444a94ebe)


Tested against a simple greeting: "Hi!"

![image](https://github.com/user-attachments/assets/4ba3fee8-33c1-434d-b86a-709c9295073b)


