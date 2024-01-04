from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/generate_questions', methods=['GET'])
def generate_questions():
    input_text = request.args.get('text', '')
    if not input_text:
        return jsonify({'error': 'Missing text parameter'}), 400
    input_text = 'Question Generation: ' + input_text
    pipe = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")
    response = pipe(input_text, max_length=50, num_return_sequences=1)
    questions = [q["generated_text"] for q in response]
    print(input_text , ': \n Question : ' , questions)
    return jsonify({'input_text': input_text, 'generated_questions': questions})

if __name__ == '_main_':
    app.run(debug=True)