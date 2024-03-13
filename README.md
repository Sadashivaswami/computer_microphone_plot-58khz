
3.Make a Git repository on a platform of your choice (Github, Gitlab, etc) for the following
problem
a. Write a C/C++ program that records samples from your computer microphone at 58
kHz sampling rate for 4.5 seconds.
b. Save a graph/plot the recorded sound

Steps to accomplish the task of recording audio in C:(For code go through gen_save_audio.c)

1. Choose a Platform: Determine the platform on which you want to perform audio recording. Different platforms (Windows, Linux, macOS, etc.) may have different libraries and APIs for audio recording.
2. Select an Audio Library: Choose an appropriate audio recording library for your platform. Some common libraries include PortAudio, ALSA (Advanced Linux Sound Architecture), Core Audio (macOS), and WASAPI (Windows Audio Session API).
3. Install Required Tools and Libraries: Install the necessary development tools and libraries for your chosen platform. This may include compilers (such as GCC on Linux) and development packages for the selected audio library.
4. Write Code to Record Audio: Implement a C program that utilizes the chosen audio library to record audio from the microphone. This involves initializing the audio device, setting parameters such as sample rate and recording duration, capturing audio data, and saving it to a file.
5. Compile the Code: Compile your C program using the appropriate compiler for your platform. Make sure to link against the required audio library.
6. Test the Program: Run the compiled executable to test the audio recording functionality. Check if the recorded audio is saved correctly and if it meets your expectations.
7. Debug and Refine: If there are any issues with the recording or the program behavior, debug the code to identify and fix the problems. You may need to adjust parameters or settings based on your requirements.
8. Documentation and Distribution: Document your code with comments and provide instructions for building and running the program. If distributing the program, ensure that users have the necessary dependencies installed.
9. Additional Processing (Optional): Depending on your application, you may want to perform additional processing on the recorded audio data, such as filtering, analysis, or playback.
10. Feedback and Improvement: Gather feedback from users or testers and make any necessary improvements or optimizations to your code.

These are the steps including plotting:(plot.py)

1. Choose a Platform: Determine the platform on which you want to perform audio recording and plotting. Different platforms (Windows, Linux, macOS, etc.) may have different libraries and APIs for audio recording and plotting.
2. Select an Audio Library: Choose an appropriate audio recording library for your platform, as mentioned in the previous steps.
3. Select a Plotting Library: Choose a plotting library suitable for your platform and programming language. Some common options include GNU Plot, Matplotlib (for Python), and gnuplot (for C/C++).
4. Install Required Tools and Libraries: Install the necessary development tools, libraries, and plotting frameworks for your chosen platform. This may include compilers, development packages for the audio library, and plotting libraries.
5. Write Code to Record Audio: Implement a C program that utilizes the chosen audio library to record audio from the microphone, following the steps mentioned earlier.
6. Write Code to Plot Data: Implement code to plot the recorded audio data. This involves loading the recorded audio samples from the file, preparing data for plotting (such as time axis and audio samples), and using the plotting library to create a graph.
7. Compile the Code: Compile your C program and plotting code using the appropriate compiler for your platform. Make sure to link against the required audio and plotting libraries.
8. Test the Program: Run the compiled executable to test both the audio recording and plotting functionality. Check if the recorded audio is saved correctly and if the plot is generated as expected.
9. Debug and Refine: If there are any issues with the recording, plotting, or the program behavior, debug the code to identify and fix the problems. You may need to adjust parameters or settings based on your requirements.
10. Documentation and Distribution: Document your code with comments and provide instructions for building and running the program, including how to generate the plot. If distributing the program, ensure that users have the necessary dependencies installed.
11. Feedback and Improvement: Gather feedback from users or testers and make any necessary improvements or optimizations to your code, including the plotting functionality.

