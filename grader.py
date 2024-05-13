# auto grader

import os
from evaluator.AudioSimilarity import AudioSimilarity
from evaluator.AudioMCD import AudioMCD
import numpy as np
from pathlib import Path


def file_exists(filepath):
    path = Path(filepath)
    return path.exists()


def get_files_in_directory(directory_path):
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_list.append(file_name)
    return file_list


def auto_grader(audio_dir, ground_truth_dir):
    audio_name_list = get_files_in_directory(audio_dir)

    mcd_score = []
    similarity_score = []
    audioMCD = AudioMCD()
    audioSimilarity = AudioSimilarity()

    for audio_name in audio_name_list:
        audio_path = os.path.join(audio_dir, audio_name)
        ground_truth_path = os.path.join(ground_truth_dir, audio_name)

        if not file_exists(audio_path) or not file_exists(ground_truth_path):
            print(f"Invalid file paths: {audio_path}, {ground_truth_path}")
            continue

        mcd = audioMCD.compare_audios(audio_path, ground_truth_path)
        similarity = audioSimilarity.compare_audios(audio_path, ground_truth_path)

        mcd_score.append(mcd)
        similarity_score.append(similarity)

    return np.mean(mcd_score), np.mean(similarity_score)


if __name__ == "__main__":

    audio_dir = "./audio"
    ground_dir = "audio_ground_truth"
    output_path = "./grader_result.txt"

    base_dirs = [
        "FastSpeech2_10000",
        "Naive_10000",
        "CLN_8000",
        "HierSpeechPP",
    ]

    emotions = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

    lines = []

    for name in base_dirs:
        print("=======================================================================")
        print(f"Executing auto grader for {name}")
        lines.append("=======================================================================")
        lines.append(f"Executing auto grader for {name}")
        mcd, similarity = auto_grader(os.path.join(audio_dir, name), ground_dir)

        print(f"MCD Score for {name} = {mcd}")
        print(f"Similarity Score for {name} = {similarity}")
        print("-----------------------------------------------------------------------")
        print("{0:<10}{1:<20}{2:<20}".format("emotion", "MCD", "Similarity"))
        lines.append(f"MCD Score for {name} = {mcd}")
        lines.append(f"Similarity Score for {name} = {similarity}")
        lines.append("-----------------------------------------------------------------------")
        lines.append("{0:<10}{1:<20}{2:<20}".format("emotion", "MCD", "Similarity"))
        for emotion in emotions:
            emotions_dir = f"{name}_emotions"
            dataset_name = f"{name}_{emotion}"
            mcd, similarity = auto_grader(os.path.join(audio_dir, emotions_dir, dataset_name), ground_dir)
            print("{0:<10}{1:<20}{2:<20}".format(emotion, mcd, similarity))
            lines.append("{0:<10}{1:<20}{2:<20}".format(emotion, mcd, similarity))

    print("=======================================================================")
    lines.append("=======================================================================")

    with open(output_path, 'w', encoding='utf-8') as f:
        for item in lines:
            f.write(f"{item}\n")
