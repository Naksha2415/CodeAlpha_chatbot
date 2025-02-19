import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking!", "I'm just a bot, but I'm good!"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot! You can call me ChatBot."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! See you soon!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Run chatbot in IDLE
if __name__ == "__main__":
    import sys
    if sys.stdin.isatty():
        start_chat()
0
