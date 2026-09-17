# SIMPLE AI CHAT-BOT

import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()


    if "hello" in user_input or "hii" in user_input:
        return "Hello ! How can I help you today"
    
    elif "how are you" in user_input:
        return "i am just chatbot, but i am doing great ! what about you"
    
    elif "your name" in user_input:
        return "I am your friendly chatbot!"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Good bye ! have a nice day 😊"
    
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}"
    
    else:
        return "I am sorry, I don't understand that yet."
    
    # MAIN PROGRAM

print("🤖 AI Chatbot: Hello! Type 'bye' to exit.\n")


while True:
    user = input("You : ")
    response = chatbot_response(user)
    print("Bot : ",response)
    if "bye" in user.lower():
        break
