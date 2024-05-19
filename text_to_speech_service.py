from gtts import gTTS
from pydub import AudioSegment
import os
import subprocess

class TextToSpeechService:
    def __init__(self, lang='es'):
        self.lang = lang
    
    def generate_audio(self, text, output_path):
        """
        Generates an audio file from the provided text.
        
        Args:
            text (str): The text to convert to speech.
            output_path (str): Path to save the generated audio file.
        """
        try:
            tts = gTTS(text=text, lang=self.lang)
            tts.save(output_path)
            print(f"Audio file generated and saved to {output_path}")
        except Exception as e:
            print(f"Error generating audio: {e}")
    
    def change_audio_properties(self, input_path, output_path, speed=1.0, pitch=0):
        """
        Changes the speed and pitch of the audio file.
        
        Args:
            input_path (str): Path to the input audio file.
            output_path (str): Path to save the modified audio file.
            speed (float): The speed factor (e.g., 1.5 for 1.5x speed).
            pitch (int): The pitch adjustment (e.g., 5 to increase pitch).
        """
        try:
            audio = AudioSegment.from_file(input_path)

            # Apply speed change
            if speed != 1.0:
                audio = audio.speedup(playback_speed=speed)
            
            # Apply pitch change
            if pitch != 0:
                new_frame_rate = int(audio.frame_rate * (2.0 ** (pitch / 12.0)))
                audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
                audio = audio.set_frame_rate(audio.frame_rate)
            
            audio.export(output_path, format="mp3")
            print(f"Audio file with changed speed and pitch saved to {output_path}")
        except Exception as e:
            print(f"Error changing audio properties: {e}")
    
    def play_audio(self, file_path):
        """
        Plays the audio file using VLC.
        
        Args:
            file_path (str): Path to the audio file.
        """
        try:
            vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            subprocess.run([vlc_path, "--play-and-exit", file_path], check=True)
        except Exception as e:
            print(f"Error playing audio: {e}")

if __name__ == "__main__":
    tts_service = TextToSpeechService()
    sample_text = "Hola, esto es una prueba del servicio de texto a voz."
    tts_service.generate_audio(sample_text, "E:\\TEXT2SPEECH\\OUTPUTS\\output.mp3")
    tts_service.change_audio_properties("E:\\TEXT2SPEECH\\OUTPUTS\\output.mp3", "E:\\TEXT2SPEECH\\OUTPUTS\\output_fast.mp3", speed=1.5)
    tts_service.play_audio("E:\\TEXT2SPEECH\\OUTPUTS\\output_fast.mp3")
