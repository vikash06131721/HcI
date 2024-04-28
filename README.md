# HCI Project Documentation

This project integrates various technologies including Node.js, HTML, jQuery, and Python to create an interactive chat interface powered by the Llama2 large language model. The backend server uses Python Flask to handle API requests, while the frontend leverages HTML and jQuery for a dynamic user experience.

## Technology Stack

- **Node.js**: Used for potentially handling some server-side logic or middleware configurations.
- **HTML**: Structures the frontend presentation of the chat interface.
- **jQuery**: Enhances HTML document manipulation, event handling, and AJAX interactions for responsive client-side scripting.
- **Python**: Utilizes Flask to set up the server that handles API requests to the Llama2 model.

## Components

1. **Llama2 Large Language Model**: Runs on a remote server, processing natural language input and generating responses.
2. **Python Flask Server (`flask_new.py`)**: Handles incoming HTTP requests from the frontend, interacts with the Llama2 model, and sends responses back to the client.
3. **JavaScript and jQuery**: Used on the frontend (`chat.html`) to manage user interactions, send requests to the Flask server, and display responses from the Llama2 model.

## How to Run

To get the system up and running, follow these steps:

1. **Frontend**:
   - Open the `chat.html` file in a browser to load the chat interface.

2. **Backend**:
   - Run the Flask server by executing the following command in your terminal:
     ```bash
     python flask_new.py
     ```

Ensure that all dependencies are installed and that the server is properly configured to accept requests from the frontend.

## Server Requests

All server-related requests (e.g., fetching responses from the Llama2 model) are handled by the Python Flask application. The JavaScript code in `chat.html` makes AJAX calls to this server to submit user input and retrieve responses.

## Additional Notes

- Ensure that your Python environment is equipped with Flask and any other necessary libraries.
- Node.js may be required if additional server-side features are utilized.
- Make sure CORS settings are configured correctly in Flask to allow for communication between the frontend and the backend.


