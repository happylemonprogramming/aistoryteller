import openai
import os

# openai.api_key_path = r'/path'
openai.api_key = os.environ["openaiapikey"]

# Open AI API creating an image url based on prompt
def text_to_image(user_prompt):
  response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
  )
  cost = 0.02
  
  return response['data'][0]['url'], cost