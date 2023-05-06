import os
import whisper
from pydub import AudioSegment

def transcribe_with_whisper(selected_file_path):
    # Convert the file to mono format to improve transcription accuracy
    audio_mono = AudioSegment.from_wav(selected_file_path).set_channels(1)
    mono_audio_path = os.path.join("records", "audio_mono.wav")
    audio_mono.export(mono_audio_path, format="wav")

    model = whisper.load_model("base")
    result = model.transcribe(mono_audio_path)
    text = result["text"]

    # Save the transcription in the "transcripts" folder
    os.makedirs("transcripts", exist_ok=True)
    transcription_name = os.path.splitext(os.path.basename(selected_file_path))[0] + ".txt"
    transcription_path = os.path.join("transcripts", transcription_name)

    with open(transcription_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\nTranscription saved in {transcription_path}")
    input("\nPress Enter to continue...")

