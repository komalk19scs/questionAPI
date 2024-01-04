# Flask Question Generator API

This API generates questions based on the input text using the T5-base question generator model.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/komalk19scs/questionAPI.git
    cd your-repo
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
