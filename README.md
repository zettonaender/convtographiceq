# convtographiceq
Update (26 March 2021): Removed the need to install autoeq, still uses the code from it, though.

For converting Equalizer Apo (or Peace) config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/fjK8muf.png

In the picture above I generated a Graphic EQ file from a SonarWorks Reference equalization (in the form of an IR wav) intended for my non-rooted Android device. The IR wav is for comparison to make sure that the output matches the intended equalization. This is because Graphic EQ has limitations on filtering narrow peaks.

The picture also included the deviation of output from input. The only difference is <20Hz and >22000Hz. This is partly because of the trim function in the file to cut unneeded frequencies from the input. You can modify these if you wish.

Before use, please download python 3.7 and get pip:
https://phoenixnap.com/kb/install-pip-windows

How to use:
1. Git clone this project or download zip. 
   Open cmd, cd to the folder from the zip.
   Type `pip install -r requirements.txt`
2. Open cmd, cd to Equalizer Apo folder.
3. Open your Equalizer Apo config.txt (or peace.txt for Peace) and add `; Benchmark` in the device selection line. Check this image as an example: https://i.imgur.com/jHmKxdv.png

4. Type `Benchmark.exe -c 1 -t 24000 -l 48 -r 48000 -o ssweep.wav` (change 48000 to your sampling rate) (ssweep.wav is an arbitrary filename) (Benchmark.exe is located in Equalizer APO folder). 

5. Put `ssweep.wav` in the same folder as `periodogram.py` from this project.
6. Open the `periodogram.py` with text editor.
7. On the first row, change the filename to `ssweep` (filename without extension)
8. Open `run.bat` or with cmd `python periodogram.py`.
9. After the program is done, there will be a folder named `myresult/ssweep`, take the `Graphic EQ.txt` file and import to wavelet.

Do keep in mind that Graphic EQ are not the best solution for headphone equalization since it cannot reproduce some filter accurately.

If you have any issues or feedback and/or want to contribute, let me know about it. Many thanks.
