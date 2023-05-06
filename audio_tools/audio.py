import pyaudio
import wave
import os
import datetime
import errno
import keyboard

def record_audio(device_index):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    records_folder = "records"

    # Create the "records" folder if it doesn't exist
    try:
        os.makedirs(records_folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index=device_index,
                        frames_per_buffer=CHUNK)

    print("\nRecording... (press ESC to stop)")

    frames = []

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('esc'):  # Change 'esc' to any key you want to use to stop the recording
            print("Recording stopped")
            break

    file_name = input("\nEnter a name for the recording (press ENTER to use the current date and time): ").strip()
    if not file_name:
        file_name = f"audio_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

    WAVE_OUTPUT_FILENAME = os.path.join(records_folder, f"{file_name}.wav")

    print("Saving audio file...")

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    stream.stop_stream()
    stream.close()
    audio.terminate()

def list_devices():
    audio = pyaudio.PyAudio()
    info = audio.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print(f"Input Device id {i} - {audio.get_device_info_by_host_api_device_index(0, i).get('name')}")
