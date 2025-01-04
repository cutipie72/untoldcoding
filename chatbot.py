import random
import string

# Define a dictionary of questions and answers
qa_pairs = {
    "What does GPA stand for?" : ["Grade Point Average"],
    "How much GPA is important in any university?" : ["4.00"],
    "Which famous university is located in Cambridge, England?" : ["University of Cambridge"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci"],
    "What is the largest mammal on Earth?": ["Blue Whale"],
    "In which year did World War II end?": "1945",
    "What is your favorite color?": "My favorite color is blue.",
    "What is your biggest fear?": "I don't have fears, but I am still under development.",
    "What is your favorite hobby?": "I enjoy learning and processing information."
}

# Function to normalize user input by removing punctuation and converting to lowercase
def normalize_input(user_input):
    # Remove punctuation and convert to lowercase
    user_input = user_input.translate(str.maketrans('', '', string.punctuation)).strip().lower()
    return user_input

# Function to get the answer based on user input
def get_answer(user_input):
    normalized_input = normalize_input(user_input)
    for question in qa_pairs.keys():
        if normalize_input(question) == normalized_input:
            return qa_pairs[question]
    return "I'm sorry, I don't understand that question."

# Main interaction loop
print("Welcome to the Q&A Chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        answer = get_answer(user_input)
        print(f"Chatbot: {answer}")