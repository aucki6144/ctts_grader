# split generated wav files into different directories

import os.path
import shutil


def split_emotion_wavs(model_name):
    input_dir = f"./audio/{model_name}"
    grader_path = "./grader.txt"

    try:
        with open(grader_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]

    except Exception as e:
        print(f"An error occurred: {e}")
        lines = []

    for line in lines:
        name = line.split("|")[0]
        emotion = line.split("|")[4]

        target_dir = os.path.join(f"{input_dir}_emotions", f"{model_name}_{emotion}")
        os.makedirs(target_dir, exist_ok=True)

        from_path = os.path.join(input_dir, f"{name}.wav")
        target_path = os.path.join(target_dir, f"{name}.wav")

        try:
            target_path = shutil.copy(from_path, target_path)
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")


if __name__ == "__main__":
    model_name_list = [
        "FastSpeech2_10000",
        "CLN_8000",
        "Naive_10000"
    ]

    for model_name in model_name_list:
        print(f"Splitting emotion sets for {model_name}")
        split_emotion_wavs(model_name)
