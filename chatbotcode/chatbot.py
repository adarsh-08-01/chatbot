from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('ApplicationBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Define a dictionary to store application URLs and corresponding data
app_urls = {
    'bhuvan': 'https://bhuvan.nrsc.gov.in',
    'aadhaar': 'https://bhuvan-app3.nrsc.gov.in/aadhaar/',
    # Add more application URLs as needed
}

# Function to fetch data from the corresponding application
def fetch_data(application):
    # Add logic to fetch data from the application using its URL
    # This might involve using APIs, web scraping, or other methods
    return f"Fetching data from {app_urls[application]}..."

# Function to handle user input and provide responses
def chat_with_bot(user_input):
    response = chatbot.get_response(user_input)

    # Check if the user input contains a known application name
    for app_name, app_url in app_urls.items():
        if app_name.lower() in user_input.lower():
            data_response = fetch_data(app_name)
            return f"{response} {data_response}"

    return response

# Interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    bot_response = chat_with_bot(user_input)
    print("Bot:", bot_response)
