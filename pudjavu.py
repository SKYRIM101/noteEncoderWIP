import PyDejavu
import os

# Create a Dejavu instance
config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "password",
        "db": "dejavu",
    }
}

djv = PyDejavu.Dejavu(config)

# Fingerprint audio file A
filename = "A.wav"
song_name = "A"
djv.fingerprint_file(filename, song_name=song_name)

# Fingerprint audio file B
filename = "B.wav"
song_name = "B"
djv.fingerprint_file(filename, song_name=song_name)

# Fingerprint audio file C
filename = "C.wav"
song_name = "C"
djv.fingerprint_file(filename, song_name=song_name)

# Fingerprint audio file D
filename = "D.wav"
song_name = "D"
djv.fingerprint_file(filename, song_name=song_name)
