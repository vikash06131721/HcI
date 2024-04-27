from flask import Flask, request, jsonify
import requests
import json
import datetime
import os
app = Flask(__name__)

@app.route('/api/read', methods=['POST'])
def read_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    request_data = request.get_json()
    date = request_data.get("date")
    if not date:
        return jsonify({"error": "Date parameter is required"}), 400

    dir_path = os.path.join('data', date)
    if not os.path.exists(dir_path):
        return jsonify({"error": "Data for the given date does not exist"}), 404
    
    combined_messages = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'r') as f:
            file_contents = json.load(f)
            combined_messages.append(file_contents)
    
    return jsonify(combined_messages), 200

@app.route('/api/save', methods=['POST'])
def save_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()

    # Format the current date and create a directory named after today's date
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')
    dir_path = os.path.join('data', today_date)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')  # Microseconds included

    
    # Construct the file path and save the JSON data
    file_path = os.path.join(dir_path, f'{timestamp}.json')
    with open(file_path, 'a') as f:  # 'a' to append to the file if it already exists
        json.dump(data, f)
        f.write('\n')  # Add a newline to separate JSON objects
    
    return jsonify({"message": "Data saved successfully"}), 200

@app.route('/api/proxy', methods=['POST'])
def proxy_to_generate():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    incoming_data = request.get_json()

    # URL of the external API
    api_url = 'http://localhost:11434/api/generate'

    # Data to be sent to the external API
    data_to_send = {
        "model": incoming_data.get("model", "llama2"),  # Default to "llama2" if not provided
        "prompt": incoming_data.get("prompt")
    }

    response = requests.post(api_url, json=data_to_send)

    if response.status_code == 200:
        # Attempt to handle the response which contains multiple JSON objects separated by newlines
        try:
            # Split the response text by newlines and parse each JSON line individually
            response_parts = response.text.strip().split('\n')
            combined_response = ''
            for part in response_parts:
                if part.strip():  # Ensure part is not empty
                    json_part = json.loads(part)
                    combined_response += json_part['response']

            # Return the combined response
            # import pdb;pdb.set_trace()
            return jsonify({"combined_response": combined_response}), 200
        except json.JSONDecodeError as e:
            # Handle JSON parsing error
            return jsonify({"error": "Failed to parse JSON", "details": str(e)}), 500
    else:
        # Return an error if the external API failed
        return jsonify({"error": "Failed to get response from the external API", "status_code": response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=4000)

