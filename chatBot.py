import wikipedia
import openai
import wolframalpha

# Set up API credentials
openai.api_key = "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"
wolframalpha_app_id = "GUHEA9-5AJGJQJKPK"

# Set up ChatGPT API
def chat(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {text}\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Set up Wolfram Alpha API
def wolframalpha_query(text):
    client = wolframalpha.Client(wolframalpha_app_id)
    res = client.query(text)
    answer = next(res.results).text
    return answer

# Main chat loop
while True:
    user_input = input("Chatbot: Hey, it's your friendly chatbot. How can I be of value to you today?\nYou: ")

    # Check for exit command
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Check for Wikipedia query
    try:
        wikipedia_result = wikipedia.summary(user_input, sentences=1)
        print("Chatbot: " + wikipedia_result)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Chatbot: " + e.options)
    except wikipedia.exceptions.PageError:
        # If not found on Wikipedia, try Wolfram Alpha
        try:
            wolframalpha_result = wolframalpha_query(user_input)
            print("Chatbot: " + wolframalpha_result)
        except:
            # If not found on Wolfram Alpha, use ChatGPT
            chat_result = chat(user_input)
            print("Chatbot: " + chat_result)
