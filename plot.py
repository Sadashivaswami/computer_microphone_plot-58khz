#To plot the recorded sound, you can use Python along with libraries like NumPy and Matplotlib. Here's how you can do it:

python
import numpy as np
import matplotlib.pyplot as plt

# Load the recorded audio file
filename = 'recorded_audio.raw'  # Change this to the path of your recorded audio file
sampling_rate = 58000  # Sampling rate used during recording
duration = 4.5  # Duration of the recorded audio in seconds

# Read the recorded audio data from the file
data = np.fromfile(filename, dtype=np.float32)

# Calculate the time array corresponding to the audio data
time = np.arange(0, len(data)) / sampling_rate

# Plot the recorded sound
plt.figure(figsize=(10, 4))
plt.plot(time, data, color='blue')
plt.title('Recorded Sound')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


