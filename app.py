import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from text_to_speech_service import TextToSpeechService

# Configuración de base del directorio y aplicación
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app)

# Configuración del servicio TTS
tts_service = TextToSpeechService()

# Crear y asegurar directorios de trabajo
uploads_dir = os.path.join(BASE_DIR, 'uploads')
outputs_dir = os.path.join(BASE_DIR, 'outputs')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)
if not os.path.exists(outputs_dir):
    os.makedirs(outputs_dir)

# Configuración de logging
if not os.path.exists('logs'):
    os.makedirs('logs')
file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('TextToSpeechService startup')

# Definición de rutas y lógica de negocio
@app.route('/upload', methods=['POST'])
def upload_file():
    app.logger.info('Received upload request')
    file = request.files['file']
    if not file:
        app.logger.error('No file part in the request')
        return jsonify({'error': 'No file part'}), 400

    file_path = os.path.join(uploads_dir, file.filename)
    file.save(file_path)
    app.logger.info(f'File saved to {file_path}')

    text = read_pdf(file_path)
    if not text:
        app.logger.error('Failed to extract text from PDF')
        return jsonify({'error': 'Failed to extract text from PDF'}), 400

    output_audio_path = os.path.join(outputs_dir, 'output.mp3')
    tts_service.generate_audio(text, output_audio_path)
    tts_service.change_audio_properties(output_audio_path, output_audio_path, float(request.form.get('speed', 1.0)), float(request.form.get('pitch', 0)))
    app.logger.info(f'Audio generated and properties adjusted at {output_audio_path}')

    return jsonify({'message': 'Audio generated', 'audio_url': f'/outputs/output.mp3'})

@app.route('/outputs/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(outputs_dir, filename)

def read_pdf(file_path):
    from PyPDF2 import PdfReader
    pdf_text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                pdf_text += extracted_text if extracted_text else ""
        app.logger.info(f'Extracted text from {file_path}')
    except Exception as e:
        app.logger.error(f'Error reading PDF file: {e}')
    return pdf_text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
