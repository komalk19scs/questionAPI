# Flask Question Generator API

This API generates questions based on the input text using the T5-base question generator model.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/komalk19scs/questionAPI.git
    cd questionAPI
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### /generate_questions Endpoint

#### Description

Generates questions based on the provided input text.

#### Endpoint

`GET /generate_questions`

#### Query Parameters

- `text` (required): The input text for question generation.

#### Example

```bash
curl -X GET "http://your-api-url/generate_questions?text=Your+input+text+here"
```
#### Sample Request
#### Using POSTMAN
- Replace `your-api-url` with the actual URL where your API is hosted.
- Replace `Your+input+text+here` with your text from which you want to generate question.


## Running the Application
``` bash
python app.py
```

## Explanation and Working of the code
- This Flask-based API defines a single endpoint `/generate_questions` that processes GET requests by extracting input text from the URL query parameters.
- It ensures the presence of the 'text' parameter and, if absent, responds with a JSON error message.
- The input text is then modified, prepending it with "Question Generation:," and passed to a T5-based question generation model from Hugging Face's transformers library.
- The generated questions are limited to 50 characters in length, and only one sequence is returned.
- The modified input text and generated questions are printed to the console, and the API responds with a JSON object containing both pieces of information.
- The API can be locally run for testing with debugging enabled.
- `Note:` In Hugging Face's transformers library, pipelines are a high-level abstraction that simplifies the process of using pre-trained models for various natural language processing tasks. Pipelines provide a convenient interface for executing common NLP tasks, such as text generation, sentiment analysis, and question answering, by abstracting away the complexities of loading models, tokenizing input, and handling output. With pipelines, users can easily apply pre-trained models to their text data without the need for extensive coding. They encapsulate the entire process into a single function call, making it accessible for users without deep knowledge of the underlying model architecture. Pipelines in Hugging Face offer a user-friendly and efficient way to leverage state-of-the-art NLP models for diverse applications.
