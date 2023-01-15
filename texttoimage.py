import openai
import os

# openai.api_key_path = r'/path'
openai.api_key = os.environ["openaiapikey"]

# Open AI API creating an image url based on prompt
def text_to_image(user_prompt):
  response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    # 256X256, 512X512, 1024X1024
    size="256x256"
  )
  cost = 0.02
  
  return response['data'][0]['url'], cost