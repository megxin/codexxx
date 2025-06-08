import math
import wave
import struct

SAMPLE_RATE = 44100  # samples per second
DURATION = 0.5  # seconds per note

# Frequencies for a simple C major scale (C4 D4 E4 F4 G4 A4 B4 C5)
FREQUENCIES = [
    261.63, 293.66, 329.63, 349.23,
    392.00, 440.00, 493.88, 523.25,
]

def generate_tone(frequency, duration):
    num_samples = int(SAMPLE_RATE * duration)
    amplitude = 32767 // 2
    samples = []
    for i in range(num_samples):
        # Compute sine wave sample
        sample = amplitude * math.sin(2 * math.pi * frequency * (i / SAMPLE_RATE))
        samples.append(int(sample))
    return samples


def main(filename="melody.wav"):
    all_samples = []
    for freq in FREQUENCIES:
        all_samples.extend(generate_tone(freq, DURATION))
    with wave.open(filename, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16 bits
        wf.setframerate(SAMPLE_RATE)
        for sample in all_samples:
            wf.writeframes(struct.pack('<h', sample))
    print(f"Generated {filename}")

if __name__ == "__main__":
    main()
