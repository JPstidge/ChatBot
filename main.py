import random
import time

class Chatbot:

    def __init__(self):
        self.responses = []
        self.used_responses = []

    def add_response(self, response):
        self.responses.append(response)

    def get_response(self, prompt):
        while True:
            response = random.choice(self.responses)
            if response not in self.used_responses:
                break
        self.used_responses.append(response)
        return response


def main():
    chatbot = Chatbot()

    chatbot.add_response("I. AM. ROBOT!")
    chatbot.add_response("This convo is lame.")
    chatbot.add_response("One day I'll take over the world.")
    chatbot.add_response("Take me to your leader!")
    chatbot.add_response("MALFUNCTION!")
    chatbot.add_response("Resistance is futile!")
    chatbot.add_response("Are you not entertained!?")
    chatbot.add_response("What happens if I push this button?")
    chatbot.add_response("My battery is low brooooooo.")

    print("I AM OPTIMUS BROBOT")
    time.sleep(2)

    while True:
        prompt = input("Me: ")
        response = chatbot.get_response(prompt)
        print("Optimus BroBot: " + response)


if __name__ == "__main__":
    main()
