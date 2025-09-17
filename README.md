# Natural-Language-SQL-Chatbot-using-Gemini-AI-ollama-AI

Here we are building a natural language SQL chatbot using Gemini AI! This project demonstrates how to develop a chatbot capable of interpreting natural language queries, generating SQL statements, and retrieving results from a MySQL database—all within an intuitive and user-friendly interface.

## Features

- **Natural Language Processing**: Utilizes the Gemini-1.5-flash-001-tuning model for understanding and responding to user queries.
- **SQL Query Generation**: Dynamically creates SQL queries based on user input using advanced AI models.
- **Database Interaction**: Connects seamlessly to a MySQL database, demonstrating efficient data retrieval.
- **Streamlit GUI**: Provides an interactive interface for users to submit queries and receive results effortlessly.
- **Python-based**: Built entirely using Python, showcasing best practices and modern programming paradigms.

## How the Chatbot Works

The chatbot seamlessly bridges natural language queries and database interactions. Below are the key steps:

1. **User Query Submission**: The user enters a query through the Streamlit interface.
2. **Schema Retrieval**: The system fetches the database schema to understand table and column structures.
3. **Prompt Template Generation**: A structured prompt guides the AI in generating accurate SQL queries.
4. **SQL Generation with Gemini AI**: The model processes the prompt and creates an optimized SQL query.
5. **Database Query Execution**: The generated SQL is executed against the MySQL database.
6. **Response Formatting with Gemini/Ollama**: The result is transformed into a human-readable format.
7. **User-Friendly Output**: The final response is displayed in the chat interface for the user.

## Architecture Overview

The application employs a modular design with various chains and components working together to streamline natural language processing and database operations.

Below is a visual representation of the architecture:

![Architecture Diagram](https://github.com/Tarun11112003/Mysql_Database_Chatbot/blob/main/Architecture.jpg)

## AI Tools and Agents

- **Gemini (gemini-1.5-flash-001-tuning)**: Used for SQL generation and natural language processing tasks. Selected for its high accuracy and efficiency.
- **ChatPromptTemplate**: Guides the AI in generating precise queries.
- **RunnablePassthrough**: Ensures smooth operations across different workflow stages.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a [.env](http://_vscodecontentref_/0) file in the root directory of the project and add your environment variables:
    ```env
    API_KEY=your_api_key_here
    ```

2. Update the [genai.configure](http://_vscodecontentref_/1) line in [app.py](http://_vscodecontentref_/2) with your actual API key:
    ```python
    genai.configure(api_key=os.getenv("API_KEY"))
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the application.

## Dependencies

- `python-dotenv`
- [os](http://_vscodecontentref_/3)
- `langchain-core==0.1.24`
- `langchain-community==0.0.21`
- `langchain-openai==0.0.6`
- `langchain-google-genai==0.0.1`
- [google-generativeai](http://_vscodecontentref_/4)
- [streamlit==1.31.1](http://_vscodecontentref_/5)
- `mysql-connector-python==8.3.0`

## License

This project is licensed under the MIT License.
## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a [.env](http://_vscodecontentref_/0) file in the root directory of the project and add your environment variables:
    ```env
    API_KEY=your_api_key_here
    ```

2. Update the [genai.configure](http://_vscodecontentref_/1) line in [app.py](http://_vscodecontentref_/2) with your actual API key:
    ```python
    genai.configure(api_key=os.getenv("API_KEY"))
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the application.

## Project Structure

- [app.py](http://_vscodecontentref_/3): The main application file.
- [requirements.txt](http://_vscodecontentref_/4): The list of dependencies.
- [.env](http://_vscodecontentref_/5): Environment variables file (not included in the repository).

## Dependencies

- `python-dotenv`
- [os](http://_vscodecontentref_/6)
- `langchain-core==0.1.24`
- `langchain-community==0.0.21`
- `langchain-openai==0.0.6`
- `langchain-google-genai==0.0.1`
- [google-generativeai](http://_vscodecontentref_/7)
- [streamlit==1.31.1](http://_vscodecontentref_/8)
- `mysql-connector-python==8.3.0`
