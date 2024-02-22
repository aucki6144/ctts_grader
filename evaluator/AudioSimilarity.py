import torchaudio
from speechbrain.pretrained import SpeakerRecognition
from scipy.spatial.distance import cosine


def cosine_similarity(emb1, emb2):
    # Compute the cosine similarity between two embeddings
    return cosine(emb1, emb2)


class AudioSimilarity:
    def __init__(self):
        # Load the pre-trained ECAPA-TDNN model
        self.model = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="tmpdir")
        # self.model = SpeakerRecognition.from_hparams(source=local_path, savedir="tmpdir")

    def compute_embedding(self, audio_path):
        # Compute the embedding of an audio file
        signal, fs = torchaudio.load(audio_path)
        embedding = self.model.encode_batch(signal)
        return embedding.squeeze()

    def compare_audios(self, audio_path1, audio_path2):
        # Compute the embeddings
        emb1 = self.compute_embedding(audio_path1)
        emb2 = self.compute_embedding(audio_path2)

        # Compute and return the cosine similarity
        return cosine_similarity(emb1, emb2)
