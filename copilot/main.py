from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline('text-generation', model='gpt-2')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.json.get('input_text')
    output = model(input_text)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
