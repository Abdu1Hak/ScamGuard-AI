from flashtext import KeywordProcessor

# STORE SCAM WORD
file_path = "scam_repo/common_spam_words_2020.txt"
def scam_keywords(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        keywords = [line.strip().lower() for line in file.readlines()] 
    return keywords 


# RETURN MATCHING WORDS
keyword_processor = KeywordProcessor() # Initialize the Library
scam_words = scam_keywords(file_path) # Store scam words
keyword_processor.add_keywords_from_list(scam_words) # add it to keyword_processor


def return_matching_words(suspicious_text):
    matched_words = keyword_processor.extract_keywords(suspicious_text.lower())
    return matched_words # returns a list
    


def risk_score(suspicious_text, scam_matching_words): 
    count_user_text = len(suspicious_text.split())
    matching_count = 0
    seen = set()

    for word in scam_matching_words:
        if word not in seen:
            matching_count += 1
            seen.add(word)
        else:
            matching_count += 2 # Double the instance to deal with duplicates

    # Scaling Mechanism
    if count_user_text <= 20: 
        risk_weight = 0.35
    elif 20 <= count_user_text <= 40:
        risk_weight = 0.20
    else: 
        risk_weight = 0.15


    return int((min((matching_count*risk_weight), 1.0))*100)


