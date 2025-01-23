from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

# Initialize the recognizer
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_speech', methods=['POST'])
def process_speech():
    # Check if an audio file was uploaded
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    # Access the uploaded audio file
    audio_file = request.files['audio_data']

    # Save the audio file temporarily
    audio_path = 'temp_audio.wav'
    audio_file.save(audio_path)

    # Recognize the speech in the audio file
    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)  # Record the audio
            speech_text = recognizer.recognize_google(audio_data)  # Recognize speech using Google API
            return jsonify({'message': f'You said: {speech_text}'})
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech could not be understood'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Speech recognition service error: {e}'}), 500
    finally:
        # Remove the temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == '__main__':
    app.run(debug=True)

