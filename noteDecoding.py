import librosa
import numpy as np

# Load the output .wav file
filename = 'output.wav'
y, sr = librosa.load(filename)

# Load the piano notes
piano_A = 'piano_A.wav'
piano_B = 'piano_B.wav'
piano_C = 'piano_C.wav'
piano_D = 'piano_D.wav'
# ... load all the piano notes

# Compute the length of each note (assuming they are all the same length)
note_length = int(sr * 1.5)

# Compute the cross-correlation between each piano note and the output audio signal
piano_notes = {'A': piano_A, 'B': piano_B, 'C': piano_C , 'D' : piano_D}  # map the piano notes to their corresponding letters
output_text = ''
for i in range(0, len(y), note_length):
    note = y[i:i+note_length]
    max_corr = 0
    max_note = None
    for letter, piano_note in piano_notes.items():
        piano_y, _ = librosa.load(piano_note)
        corr = np.correlate(note, piano_y)
        if corr > max_corr:
            max_corr = corr
            max_note = letter
    output_text += max_note
print(output_text)
