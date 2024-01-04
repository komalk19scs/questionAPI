

## Question Generation API Documentation

### Introduction
This API allows you to generate relevant questions from a given block of text using Hugging Face's "question-generation" pipeline. It accepts a GET request with the input text as a query parameter and returns a JSON response with the generated questions.

### API Endpoint
- **Endpoint:** `/generate_questions`
- **Method:** GET

### Request Parameters
- **Query Parameter:**
  - `text` (string, required): The input text for which questions need to be generated.

### Response Format in Postman/Insomnia
The API responds with a JSON object containing the input text and the generated questions.

- **JSON Response Format:**
  ```json
  {
    "input_text": "Input text goes here.",
    "generated_questions": ["Question ?"]
  }
  ```

### Error Responses
- If the 'text' parameter is missing:
  - **Status Code:** 400 (Bad Request)
  - **Response:**
    ```json
    {
      "error": "Missing text parameter"
    }
    ```

### Sample Usage
#### cURL Request
```bash
curl -X GET "http://your-api-url/generate_questions?text=Your%20input%20text%20here"
```

#### Sample Output
```json
{
  "input_text": "Your input text here.",
  "generated_questions": ["What is the main idea of the text?"]
}
```



### Github Repository
```
https://github.com/komalk19scs/questionAPI.git
```
- Clear instructions on how to set up and run the API is given in the README.

### Conclusion
This API provides a simple and efficient way to generate questions from a given block of text. This documentation guides users on how to interact with the API using the specified endpoint and parameters.
