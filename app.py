# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for generating questions
@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    # Retrieve 'text' parameter from the form data
    input_text = request.form.get('inputText', '')
    
    # Check if 'text' parameter is missing
    if not input_text:
        return render_template('index.html', error='Missing text parameter')

    # Prepend a task-specific token to the input text
    input_text = 'Question Generation: ' + input_text
    
    # Initialize T5-based question generation pipeline
    pipe = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")
    
    # Generate questions based on the input text
    response = pipe(input_text, max_length=50, num_return_sequences=1)
    
    # Extract generated questions from the response
    generated_question = response[0]["generated_text"]

    # Print input text and generated questions for logging
    print(input_text, ': \n Question : ', generated_question)

    # Return rendered template with input text and generated questions
    return render_template('result.html', input_text=input_text, generated_question=generated_question)


