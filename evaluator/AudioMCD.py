import librosa
import numpy as np
from scipy.spatial.distance import cdist
from librosa.sequence import dtw


# def compute_mcd(mfcc1, mfcc2):
#     # Compute the MCD between two MFCC feature matrices
#     # Note: Assume that mfcc1 and mfcc2 are aligned
#     mcd = np.sqrt(2 * np.sum((mfcc1 - mfcc2) ** 2, axis=0))
#     mean_mcd = np.mean(mcd)
#     return mean_mcd

def compute_mcd(mfcc1, mfcc2):
    # Calculate the cost matrix using Euclidean distance
    cost_matrix = cdist(mfcc1.T, mfcc2.T, metric='euclidean')

    # Use DTW to find the optimal alignment path. The 'librosa' implementation returns the cost matrix and the warp path
    _, wp = dtw(C=cost_matrix, metric='euclidean', subseq=True, backtrack=True)

    wp_filtered = [(i, j) for i, j in wp if j < mfcc2.shape[1]]

    # Align the MFCC matrices based on the warp path
    aligned_mfcc1 = np.array([mfcc1[:, i] for i, _ in wp_filtered]).T
    aligned_mfcc2 = np.array([mfcc2[:, j] for _, j in wp_filtered]).T

    # Compute the squared differences
    diff_squared = (aligned_mfcc1 - aligned_mfcc2) ** 2

    # Compute the MCD
    mcd = np.sqrt(2 * np.sum(diff_squared, axis=0))  # Sum over features
    mean_mcd = np.mean(mcd)  # Average over frames

    return mean_mcd

class AudioMCD:
    def __init__(self, n_mfcc=13):
        self.n_mfcc = n_mfcc

    def compute_mfcc(self, audio_path):
        # Load the audio file
        y, sr = librosa.load(audio_path)
        # Compute MFCC features from the audio signal
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=self.n_mfcc)
        return mfcc

    def compare_audios(self, audio_path1, audio_path2):
        # Compute MFCCs for both audio files
        mfcc1 = self.compute_mfcc(audio_path1)
        mfcc2 = self.compute_mfcc(audio_path2)

        # Compute and return the MCD
        return compute_mcd(mfcc1, mfcc2)
