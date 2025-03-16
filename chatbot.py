from google import genai
# get your API key at https://ai.google.dev/gemini-api/docs/api-key
client = genai.Client(api_key="AIzaSyCqJx-MM8OQTpFAsUIxJYBLGn5ABB5cALc")
while True:
  message=input("You: ")
  print(message)
  if message.lower()=="bye":
    break
  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=[message])
  print("chatbot: ",response.text)

