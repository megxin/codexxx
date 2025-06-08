import math
import wave
import struct

SAMPLE_RATE = 44100  # samples per second
DURATION = 0.5  # seconds per note

# Frequencies for notes used in "Kaeru no Uta" (Frère Jacques)
NOTE_FREQUENCIES = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "C5": 523.25,
}

# Melody sequence for "Kaeru no Uta" (each note has the same duration)
MELODY = [
    "C4", "D4", "E4", "C4",
    "C4", "D4", "E4", "C4",
    "E4", "F4", "G4",
    "E4", "F4", "G4",
    "G4", "A4", "G4", "F4", "E4", "C4",
    "G4", "A4", "G4", "F4", "E4", "C4",
    "C4", "G4", "C5",
    "C4", "G4", "C5",
]

def generate_tone(frequency, duration):
    num_samples = int(SAMPLE_RATE * duration)
    amplitude = 32767 // 2
    samples = []
    for i in range(num_samples):
        sample = amplitude * math.sin(2 * math.pi * frequency * (i / SAMPLE_RATE))
        samples.append(int(sample))
    return samples

def main(filename="kaeru_no_uta.wav"):
    all_samples = []
    for note in MELODY:
        frequency = NOTE_FREQUENCIES.get(note)
        if frequency is None:
            continue
        all_samples.extend(generate_tone(frequency, DURATION))
    with wave.open(filename, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16 bits
        wf.setframerate(SAMPLE_RATE)
        for sample in all_samples:
            wf.writeframes(struct.pack('<h', sample))
    print(f"Generated {filename}")

if __name__ == "__main__":
    main()
