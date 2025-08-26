from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import soundfile as sf
import cv2
import io

app = Flask(__name__)

def process_text(text):
    # Simple text processing: lowercase and tokenize
    return text.lower().split()

def process_image(file):
    # Open, convert, resize image, and convert to list for JSON serialization
    image = Image.open(file).convert('RGB').resize((224, 224))
    return np.array(image).tolist()

def process_audio(file):
    # Read audio bytes and extract waveform and sample rate
    audio, sample_rate = sf.read(io.BytesIO(file.read()))
    return {'length': len(audio), 'sample_rate': sample_rate}

def process_video(file):
    # Read video bytes, extract first frame, resize and convert to list
    video_bytes = file.read()
    np_array = np.frombuffer(video_bytes, np.uint8)
    cap = cv2.VideoCapture(cv2.imdecode(np_array, cv2.IMREAD_COLOR))
    ret, frame = cap.read()
    cap.release()
    if ret:
        frame_resized = cv2.resize(frame, (224, 224))
        return frame_resized.tolist()
    return None

@app.route('/process', methods=['POST'])
def handle_process_request():
    result = {}

    if 'text' in request.form:
        result['text'] = process_text(request.form['text'])
    if 'image' in request.files:
        result['image'] = process_image(request.files['image'])
    if 'audio' in request.files:
        result['audio'] = process_audio(request.files['audio'])
    if 'video' in request.files:
        result['video'] = process_video(request.files['video'])

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
