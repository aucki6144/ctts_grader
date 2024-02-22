import os
from evaluator.AudioSimilarity import AudioSimilarity
from evaluator.AudioMCD import AudioMCD
import numpy as np


def get_files_in_directory(directory_path):
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))
    return file_list


def auto_grader(dataset_name, audio_dir, ground_truth_dir):
    audio_name_list = get_files_in_directory(audio_dir)
    ground_name_list = get_files_in_directory(ground_truth_dir)

    mcd_score = []
    similarity_score = []
    audioMCD = AudioMCD()
    audioSimilarity = AudioSimilarity()

    if len(audio_name_list) == len(ground_name_list):
        for audio_name, ground_name in zip(audio_name_list, ground_name_list):
            mcd_score.append(AudioMCD.compare_audios(audioMCD, audio_name, ground_name))
            similarity_score.append(AudioSimilarity.compare_audios(audioSimilarity, audio_name, ground_name))
        print("Mean MCD Score for {} = {}".format(dataset_name, np.mean(mcd_score)))
        print("Similarity Score for {} = {}".format(dataset_name, np.mean(similarity_score)))
    else:
        print("Length of audio list and ground truth list not equal, check for the disappearance of necessary files")


if __name__ == "__main__":

    audio_dir = "./audio"
    ground_dir = "./audio_ground_truth"

    for root, dirs, files in os.walk(audio_dir):
        for name in dirs:
            auto_grader(name, os.path.join(root, name), ground_dir)
