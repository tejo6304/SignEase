from flask import Flask, render_template, request, jsonify
import os
import cv2

app = Flask(__name__)

# Path to the directory containing ASL images
asl_image_dir = r"C:\Users\Dell\Desktop\SignEase\Speech to sign\ASL"

# Function to check and return ASL images
def get_asl_image_paths(word):
    word = word.upper()  # Convert input to uppercase
    image_paths = []
    for char in word:
        image_path = None
        for ext in [".jpg", ".jpeg", ".png"]:
            potential_path = os.path.join(asl_image_dir, f"{char}{ext}")
            if os.path.exists(potential_path):
                image_path = potential_path
                break
        if image_path:
            image_paths.append(image_path)
        else:
            image_paths.append(None)  # No image found for this character
    return image_paths

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the input word and return images
@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('word', '').strip()
    if not data.isalpha():
        return jsonify({'error': 'Please enter valid letters only.'}), 400

    image_paths = get_asl_image_paths(data)
    result = []
    for char, path in zip(data.upper(), image_paths):
        if path:
            result.append({'char': char, 'path': f"/static/{os.path.basename(path)}"})
        else:
            result.append({'char': char, 'path': None})
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
