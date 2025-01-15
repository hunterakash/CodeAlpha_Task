#import libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import get_close_matches



#Download necessary NLTK resources

nltk.download('punkt')
nltk.download('stopwords')



#FAQ data

FAQS = {
    "What are your support hours?": "Our support team is available 24/7.",
    "How can I reset my password?": "To reset your password, click on 'Forgot Password' on the login page.",
    "Where can I find pricing information?": "You can find pricing details on our website's pricing page.",
}



#Preprocess FAQ questions

stop_words = set(stopwords.words('english'))
processed_faqs = {q: [w for w in word_tokenize(q.lower()) if w not in stop_words] for q in FAQS}



#Function to preprocess user input

def preprocess_input(user_input):
    words = word_tokenize(user_input.lower())
    return [w for w in words if w not in stop_words]



#Function to find the best matching FAQ

def find_best_match(user_input):
    processed_input = preprocess_input(user_input)
    
    #Compare with each FAQ question
    
    matches = {}
    for question, keywords in processed_faqs.items():
        match_score = len(set(processed_input) & set(keywords)) / len(keywords)
        matches[question] = match_score
    
    #Get the best match with a minimum threshold
    
    best_match = max(matches, key=matches.get)
    
    if matches[best_match] > 0.5:  # Minimum similarity threshold
        return FAQS[best_match]
    return "I'm sorry, I couldn't find an answer to your question."



#Chat loop

def chatbot():
    print("FAQ Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = find_best_match(user_input)
        print(f"Chatbot: {response}")



#Run the chatbot

if __name__ == "__main__":
    chatbot()



#User input:
	How can I reset my password?


#Output:
	To reset your password, click on 'Forgot Password' on the login page.




#User input 2:
	What are the support hours?


#Output:
	Our support team is available 24/7.

