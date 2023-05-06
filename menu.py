from audio_tools.audio import record_audio, list_devices
from audio_tools.list_files import list_files
from audio_tools.transcriptor_whisper import transcribe_with_whisper
import sys
import os
import platform


def clear_terminal():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    while True:
        clear_terminal()
        print("\nMenu:")
        print("1. Record audio")
        print("2. Generate transcriptions")
        print("3. Exit")

        option = input("\nSelect an option: ")

        if option == "1":
            clear_terminal()
            list_devices()
            device_index = int(input("\nSelect the recording device ID: "))
            record_audio(device_index)
        elif option == "2":
            clear_terminal()
            selected_file_path = list_files()
            if selected_file_path:
                transcribe_with_whisper(selected_file_path)
        elif option == "3":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
