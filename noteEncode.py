import pygame
import numpy as np
import wave

# Initialize pygame
pygame.init()

# Define a dictionary to map letters to piano notes
note_map = {
    'A': pygame.mixer.Sound("piano_A.wav"),
    'B': pygame.mixer.Sound("piano_B.wav"),
    'C': pygame.mixer.Sound("piano_C.wav"),
    'D': pygame.mixer.Sound("piano_D.wav"),
    # 'E': pygame.mixer.Sound("piano_E.wav"),
    # 'F': pygame.mixer.Sound("piano_F.wav"),
    # 'G': pygame.mixer.Sound("piano_G.wav"),
}

# Get input from the user
text = input("Enter a word: ")

# Convert the input to uppercase
text = text.upper()

# Create a list to store the samples of the played notes
samples = []

# Play the corresponding piano notes for each letter and append the samples to the list
for letter in text:
    if letter in note_map:
        sound = note_map[letter].get_raw()
        samples.append(np.fromstring(sound, dtype=np.int16))

# Concatenate the samples into a single array
concatenated_samples = np.concatenate(samples)

# Open a new wave file to save the concatenated samples
with wave.open("output.wav", "w") as f:
    # Set the sample width and number of channels
    f.setsampwidth(2)
    f.setnchannels(1)
    # Set the sample rate
    f.setframerate(44100*2)
    # Write the samples to the file
    f.writeframes(concatenated_samples.tostring())

# Wait for the notes to finish playing
pygame.time.wait(1000)

# Exit pygame sasas
pygame.quit()
