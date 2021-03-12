# convtographiceq
For converting Equalizer Apo config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/GsyPTNY.png

In the picture above I generated a Graphic EQ file from a SonarWorks Reference equalization (in the form of an IR wav) intended for my non-rooted Android device. The IR wav is for comparison to make sure that the output matches the intended equalization. This is because Graphic EQ has limitations on filtering narrow peaks.

Although, I took a listen to the original curve and the Graphic EQ and basically couldn't tell any differences. In the picture you can see some narrow filter missing from the Graphic EQ but it doesn't seem to affect my hearing perception. YMMV. Anyways, tutorial below.

How to use:
1. Setup AutoEq https://github.com/jaakkopasanen/AutoEq and install Audacity. Also notepad++ or sublime text will help.
2. Git clone this project or download zip.
3. Open cmd, cd to Equalizer Apo folder.
4. Type 'Benchmark.exe -c 1 -f 1 -t 23000 -l 46 -r 48000 -o sweep.wav' (change 48000 to your sampling rate) (sweep.wav is an arbitrary filename) (Benchmark.exe is a part of an AutoEq project)
5. Open sweep.wav on audacity, then File>>Export>>Export Wav. Choose to save as '32 bit float'. For this tutorial, I'll go with 'expfloat.wav'.
6. Put the exported wav in the same folder as 'testing123.py' from this project.
7. Open the 'testing123.py' with text editor.
8. On the first row, change the filename to 'expfloat' (filename without extension)
9. Run y.bat or with cmd python testing123.py
10. There will be a few graph plotted. You can safely close it.
11. After the program is done, there will be a csv file named 'expfloat.csv' (again, arbitrary name)
12. Create a folder called 'expfloat' on the AutoEq folder (where 'autoeq.py' is located in)
13. Put the csv inside your created folder
14. In the AutoEq folder, rename 'constants.py' to something else and replace with the one included from this project.
15. Activate venv in autoeq and use the following command as an example:
    python autoeq.py --input_dir=expfloat" --output_dir="my_results/expfloat" --compensation="compensation/zero.csv" --equalize --show_plot --convolution_eq --fs=48000

    The main thing is we will use the zero.csv as target to generate a new curve for AutoEq.
16. Open my_results/expfloat and take the Graphic EQ.txt file. The equalization curve is now usable on non-rooted devices.
