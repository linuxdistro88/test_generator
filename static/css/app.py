# app.py
from flask import Flask, request, jsonify
from helpers.openai_helper import OpenAIHelper
import os

app = Flask(__name__)

# initialize the OpenAI API
api_helper = OpenAIHelper(os.getenv('OPENAI_API_KEY'))

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()

    # extract the new fields
    ingredients = data.get('ingredients')
    method = data.get('method')
    diet = data.get('diet')

    # Generate the response using the OpenAI API helper
    response = api_helper.generate_response(ingredients, method, diet)

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
