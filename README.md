# Speech-to-Text Application

This project is a Speech-to-Text (STT) application that converts spoken language into written text using a combination of a Flask backend and a frontend interface with HTML, CSS, and JavaScript. The backend processes audio input, recognizes speech using Google's Speech Recognition API, and returns the transcribed text to the frontend.

---

## Features
- **Real-time Speech Recognition**: Converts audio input into text in real-time.
- **Flask Backend**: Handles audio processing and interacts with the Speech Recognition API.
- **Frontend Interface**: Allows users to interact with the app through a clean and responsive UI.
- **Error Handling**: Provides feedback in case of errors during speech recognition or file uploads.

---

## Project Structure
```
.
├── app.py                 # Flask backend script
├── templates
│   └── index.html         # Frontend HTML file
├── static
│   └── style.css          # CSS styles for the frontend
├── static
│   └── script.js          # JavaScript for frontend functionality
└── README.md              # Project documentation
```

---

## Requirements
- Python 3.7+
- Flask
- SpeechRecognition

### Install Dependencies
To install the required Python libraries, run:
```bash
pip install flask SpeechRecognition
```

---

## Setup and Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/stt-application.git
   cd stt-application
   ```

2. **Run the Flask Server**:
   ```bash
   python app.py
   ```

3. **Access the Application**:
   Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

4. **Use the Application**:
   - Click the "Start Recording" button to record your voice.
   - The application will transcribe your speech and display it on the screen.

---

## Technologies Used
- **Flask**: A lightweight Python web framework.
- **SpeechRecognition**: A library for performing speech-to-text using various engines.
- **HTML, CSS, JavaScript**: For building the frontend interface.

---

## Future Enhancements
- Add support for multiple languages.
- Improve the UI/UX design.
- Integrate with other speech recognition APIs.
- Add offline recognition capabilities.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it for your own projects.

