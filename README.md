# convtographiceq
Update (23 March 2021): Method changed to use scipy.signal.periodogram and tutorial rewrite.

For converting Equalizer Apo (or Peace) config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/fjK8muf.png

In the picture above I generated a Graphic EQ file from a SonarWorks Reference equalization (in the form of an IR wav) intended for my non-rooted Android device. The IR wav is for comparison to make sure that the output matches the intended equalization. This is because Graphic EQ has limitations on filtering narrow peaks.

The picture also included the deviation of output from input. The only difference is <20Hz and >22000Hz. This is partly because of the trim function in the file to cut unneeded frequencies from the input. You can modify these if you wish.

How to use:
1. Setup AutoEq https://github.com/jaakkopasanen/AutoEq. Also notepad++ or sublime text will help.
2. Git clone this project or download zip.
3. Open cmd, cd to Equalizer Apo folder.
4. Open your Equalizer Apo config.txt (or peace.txt for Peace) and add `; Benchmark` in the device selection line. Check this image as an example: https://i.imgur.com/jHmKxdv.png

5. Type `Benchmark.exe -c 1 -t 24000 -l 48 -r 48000 -o ssweep.wav` (change 48000 to your sampling rate) (ssweep.wav is an arbitrary filename) (Benchmark.exe is located in Equalizer APO folder). 

	Optional: Increasing length to a multiple of 2 and changing the `length` in the `periodogram.py` can yield more accurate result (doesn't mean you need to though). 

6. Put `ssweep.wav` in the same folder as `periodogram.py` from this project.
7. Open the `periodogram.py` with text editor.
8. On the first row, change the filename to `ssweep` (filename without extension)
9. Change `length` to `Sampling rate/Highest frequencies`.
10. Open `run.bat` or with cmd `python testing123.py`.
11. There will be an inverted graph plotted. You can safely close it.
12. After the program is done, there will be a csv file named `ssweep.csv` (again, arbitrary name)
13. Create a folder called `ssweep` on the AutoEq folder (where `autoeq.py` is located in)
14. Put the csv inside your created folder
15. In the AutoEq folder, rename `constants.py` to something else and replace with the one included from this project.

A few notes on the 'constants' file changes, you can take a look and tweak these if you have inaccuracies with the result:

	`DEFAULT_F_MIN = 20` to `DEFAULT_F_MIN = 1`
	Changes the minimum frequency that will be equalized. Without this, my results are missing an intended peak at 30Hz.
	
	`DEFAULT_MAX_GAIN = 6.0` to `DEFAULT_MAX_GAIN = 15.0`
	`DEFAULT_TREBLE_MAX_GAIN = 6.0` to `DEFAULT_TREBLE_MAX_GAIN = 15.0`
	Affects the maximum gain which, when exceeded will clip the resulting equalization curve accordingly. 
	You can change this according to your target. Although, lowering it to match your curve is unnecessary unless you want to increase your pre-amp.
	
	`DEFAULT_SMOOTHING_ITERATIONS = 1` to `DEFAULT_SMOOTHING_ITERATIONS = 0`
	Changes how many times the csv input will be smoothened. Affects the whole range of the equalization frequencies.
	You can increase this to make the result appear smoother, with the possibility of losing narrow-ish peaks. 
	For me, using 0 smoothing results in aliased results but doesn't affect the perceptual sound. 
	If setting this to 0 still result in missing peaks/notches, see note below for the savgol_filter parameter of my code.
	
	`DEFAULT_TREBLE_SMOOTHING_ITERATIONS = 1` to `DEFAULT_TREBLE_SMOOTHING_ITERATIONS = 0`
	Changes how many times AutoEq does heavy treble frequency smoothing.
	Setting this to 0 was required because AutoEq smoothened the treble range heavily. 
	This was intended for equalizing headphone measurements and not for this project.
	
Changing the `F_MIN` and `TREBLE_SMOOTHING_ITERATIONS` only should generate the intended output. If AutoEq was updated and replacing 'constants.py' causes issues, you can change it yourself.

    
15. Open my_results/expfloat and take the Graphic EQ.txt file. The equalization curve is now usable on non-rooted devices.
`python autoeq.py --input_dir="ssweep" --output_dir="my_results/ssweep" --compensation="compensation/zero.csv" --equalize --show_plot --convolution_eq --fs=48000,44100,192000`

	The main thing is we will use the `zero.csv` as target to generate a new curve for AutoEq.
	
16. Open `my_results/ssweep` and take the Graphic EQ.txt file. The equalization curve is now usable on non-rooted devices.


Do keep in mind that Graphic EQ are not the best solution for headphone equalization since it cannot reproduce some filter accurately.

If you have any issues or feedback and/or want to contribute, let me know about it. Many thanks.
