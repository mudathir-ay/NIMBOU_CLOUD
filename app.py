from flask import Flask, render_template, request,jsonify
import os
from google import genai
# get your API key at https://ai.google.dev/gemini-api/docs/api-key
client = genai.Client(api_key="AIzaSyCqJx-MM8OQTpFAsUIxJYBLGn5ABB5cALc")
app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/chat", methods=['POST'])
def chat():
    if request.method == 'POST':
        input_message= request.form['input_message']
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[input_message])
        output_message=response.text
        if output_message=="":
            return render_template('index.html')
        else:
            return render_template('index.html',chatbot_reply=output_message)
    else:
        return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    text=request.get_json().get("message")
    reply = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[text])
    response=reply.text
    message ={"answer":response}
    return jsonify(message)

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)