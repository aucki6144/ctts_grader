# Dump validation wavs according to grader.txt

import os.path
import shutil

if __name__ == "__main__":
    grader_txt_path = "./grader.txt"
    base_path = "./home/ESD_en"
    output_path = "audio_ground_truth"

    try:
        with open(grader_txt_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]

    except Exception as e:
        print(f"An error occurred: {e}")
        lines = []

    # print(lines[:10])
    # lines = lines[:10]

    for line in lines:
        file_name, speaker_name = line.split("|")[:2]
        file_dir = os.path.join(base_path, speaker_name, "wav", f"{file_name}.wav")
        try:
            target_path = shutil.copy(file_dir, output_path)
            print(f"copying {file_dir}")
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")
