#OpenAI prompt generator
import openai
import os

# openai.api_key_path = r'/path'
openai.api_key = os.environ["openaiapikey"]

def textgenerator(user_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = user_prompt,
        # Temperature
        # What sampling temperature to use. Higher values means the model will take more risks.
        # Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.
        temperature=0.9,
        max_tokens=2048,
        # Top_p
        # An alternative to sampling with temperature, called nucleus sampling, 
        # where the model considers the results of the tokens with top_p probability mass. 
        # So 0.1 means only the tokens comprising the top 10% probability mass are considered.
        top_p=1,
        # Frequency Penalty
        # Number between -2.0 and 2.0. 
        # Positive values penalize new tokens based on their existing frequency in the text so far,
        # decreasing the model's likelihood to repeat the same line verbatim.
        frequency_penalty=0.0,
        # Presence Penalty
        # Number between -2.0 and 2.0. 
        # Positive values penalize new tokens based on whether they appear in the text so far, 
        # increasing the model's likelihood to talk about new topics.
        presence_penalty=0.6,
        # Stop
        # Up to 4 sequences where the API will stop generating further tokens. 
        # The returned text will not contain the stop sequence.
        stop=[" Human:", " AI:"]
    )

    AI_response = response['choices'][0]['text']
    cost = 0.02*(int(response['usage']['total_tokens']))/1000
    return AI_response, cost