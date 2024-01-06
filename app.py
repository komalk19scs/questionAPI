# Import necessary libraries
from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Define the route for generating questions
@app.route('/generate_questions', methods=['GET'])

def generate_questions():
    # Retrieve 'text' parameter from the query string
    input_text = request.args.get('text', '')
    
    # Check if 'text' parameter is missing
    if not input_text:
        return jsonify({'error': 'Missing text parameter'}), 400
        
    # Prepend a task-specific token to the input text
    input_text = 'Question Generation: ' + input_text
    
    # Initialize T5-based question generation pipeline
    pipe = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")
    
    # Generate questions based on the input text
    response = pipe(input_text, max_length=50, num_return_sequences=1)
    
    # Extract generated questions from the response
    questions = [q["generated_text"] for q in response]

    # Print input text and generated questions for logging
    print(input_text , ': \n Question : ' , questions)

     # Return JSON response containing input text and generated questions
    return jsonify({'input_text': input_text, 'generated_questions': questions})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
