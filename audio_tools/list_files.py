import os

def list_files():
    path = "records"
    files = [f for f in os.listdir(path) if f.endswith(".wav")]

    if not files:
        print("No recorded audios.")
        input("Press Enter to continue...")
        return None

    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")

    selection = int(input("Select the file you want to transcribe: "))
    selected_file = files[selection - 1]
    selected_file_path = os.path.join(path, selected_file)

    return selected_file_path
