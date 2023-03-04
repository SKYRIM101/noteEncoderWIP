from pydub import AudioSegment

# Load the audio files into pydub AudioSegment objects
piano_A = AudioSegment.from_file("piano_A.wav")
piano_B = AudioSegment.from_file("piano_B.wav")
piano_C = AudioSegment.from_file("piano_C.wav")
piano_D = AudioSegment.from_file("piano_D.wav")

# Extract the audio fingerprints
piano_A_fp = piano_A.fingerprint()
piano_B_fp = piano_B.fingerprint()
piano_C_fp = piano_C.fingerprint()
piano_D_fp = piano_D.fingerprint()

# Create a dictionary to map the fingerprints to the notes
note_map = {piano_A_fp: "A", piano_B_fp: "B", piano_C_fp: "C", piano_D_fp: "D"}

# Load an audio file to match
audio = AudioSegment.from_file("output.wav")

# Extract the audio fingerprint
audio_fp = audio.fingerprint()

# Try to match the audio fingerprint to one of the 4 piano notes
if audio_fp in note_map:
    print("The audio file corresponds to the piano note:", note_map[audio_fp])
else:
    print("Could not match the audio file to any of the 4 piano notes.")
