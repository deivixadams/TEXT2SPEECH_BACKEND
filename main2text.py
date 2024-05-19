import os
from PyPDF2 import PdfReader
from backend.text_to_speech_service import TextToSpeechService

def read_pdf(file_path):
    """
    Reads a PDF file and extracts text from it.
    
    Args:
        file_path (str): Path to the PDF file.
    
    Returns:
        str: The extracted text.
    """
    pdf_text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                pdf_text += page.extract_text() if page.extract_text() else ""
    except Exception as e:
        print(f"Error reading PDF file: {e}")
    return pdf_text

def get_speed_factor():
    """
    Prompts the user to select a speed factor.
    
    Returns:
        float: The selected speed factor.
    """
    print("Seleccione el factor de velocidad:")
    print("a. Normal")
    print("b. Media")
    print("c. Rápida")
    choice = input("Ingrese la opción (a/b/c): ").strip().lower()
    if choice == 'a':
        return 1.0
    elif choice == 'b':
        return 1.5
    elif choice == 'c':
        return 2.0
    else:
        print("Opción inválida, seleccionando velocidad normal por defecto.")
        return 1.0

def get_pitch_adjustment():
    """
    Prompts the user to select a pitch adjustment.
    
    Returns:
        int: The selected pitch adjustment.
    """
    print("Seleccione el ajuste de tono (semitonos):")
    print("0. Sin cambio")
    print("1. Aumento leve")
    print("2. Aumento moderado")
    print("3. Aumento grande")
    print("-1. Disminución leve")
    print("-2. Disminución moderada")
    print("-3. Disminución grande")
    try:
        pitch = int(input("Ingrese el ajuste de tono: ").strip())
        return pitch
    except ValueError:
        print("Entrada inválida, seleccionando sin cambio de tono por defecto.")
        return 0

def generate_audio_from_pdf(pdf_path, audio_output_path, speed=1.0, pitch=0):
    """
    Reads a PDF file, extracts text, and generates an audio file from the text.
    
    Args:
        pdf_path (str): Path to the PDF file.
        audio_output_path (str): Path to save the generated audio file.
        speed (float): The speed factor (e.g., 1.5 for 1.5x speed).
        pitch (int): The pitch adjustment (e.g., 5 to increase pitch).
    """
    text = read_pdf(pdf_path)
    if text:
        tts_service = TextToSpeechService(lang='es')  # Set language to Spanish
        temp_output_path = os.path.join("E:\\TEXT2SPEECH\\OUTPUTS", "temp_output.mp3")
        tts_service.generate_audio(text, temp_output_path)
        tts_service.change_audio_properties(temp_output_path, audio_output_path, speed, pitch)
        os.remove(temp_output_path)
        print(f"Archivo de audio guardado en: {audio_output_path}")
        tts_service.play_audio(audio_output_path)
    else:
        print("No se extrajo texto del PDF.")

if __name__ == "__main__":
    pdf_path = "E:\\TEXT2SPEECH\\OUTPUTS\\POLITICA_INCLUSION.PDF"
    audio_output_path = "E:\\TEXT2SPEECH\\OUTPUTS\\output.mp3"
    speed = 1.0  # Fixed speed to avoid issues
    pitch = get_pitch_adjustment()
    
    if not os.path.isfile(pdf_path):
        print(f"Archivo PDF no encontrado: {pdf_path}")
    else:
        generate_audio_from_pdf(pdf_path, audio_output_path, speed, pitch)
