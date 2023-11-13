from flask import Flask, request, jsonify
from openai.api import OpenAIAPI

app = Flask(__name__)

# initialize the OpenAI API
api = OpenAIAPI("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")

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()

    # extract the new fields
    ingredients = data.get('ingredients')
    method = data.get('method')
    diet = data.get('diet')

    # combine the fields into a single query
    query = f"{ingredients} {method} {diet}"

    # Query the OpenAI API
    response = api.complete(prompt=query, max_tokens=100)

    # Extract the 'choices' list from the response
    choices = response['choices']

    # If the 'choices' list is not empty, return the 'text' field of the first choice
    if choices:
        text = choices[0]['text']
        return jsonify({'response': text})

    return jsonify({'response': 'Sorry, I was not able to generate a recipe based on your inputs.'})

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
