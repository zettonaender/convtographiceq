# convtographiceq
For converting Equalizer Apo config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/GsyPTNY.png

In the picture above I generated a Graphic EQ file from a SonarWorks Reference equalization (in the form of an IR wav) intended for my non-rooted Android device. The IR wav is for comparison to make sure that the output matches the intended equalization. This is because Graphic EQ has limitations on filtering narrow peaks.

Although, I took a listen to the original curve and the Graphic EQ and basically couldn't tell any differences. In the picture you can see some narrow filter missing from the Graphic EQ but it doesn't seem to affect my hearing perception. YMMV. Anyways, tutorial below.

How to use:
1. Setup AutoEq https://github.com/jaakkopasanen/AutoEq. Also notepad++ or sublime text will help.
2. Git clone this project or download zip.
3. Open cmd, cd to Equalizer Apo folder.
4. Open your Equalizer Apo config.txt (or peace.txt for Peace) and add `; Benchmark` in the device selection line. Check this image as an example: https://i.imgur.com/jHmKxdv.png
5. Type `Benchmark.exe -c 1 -t 24000 -l 48 -r 48000 -o sweep.wav` (change 48000 to your sampling rate) (sweep.wav is an arbitrary filename) (Benchmark.exe is located in Equalizer APO folder)
6. Open `sweep.wav` on audacity, then `File>>Export>>Export Wav`. Choose to save as `32 bit float`. For this tutorial, I'll go with 'expfloat.wav'.
UPDATE: Using audacity apparently is not needed, rename the file as `expfloat.wav` and continue to the next step.
	
7. Put the exported wav in the same folder as `testing123.py` from this project.
8. Open the `testing123.py` with text editor.
9. On the first row, change the filename to `expfloat` (filename without extension)
10. Run `y.bat` or with cmd `python testing123.py`.
11. There will be a few graph plotted. You can safely close it.
12. After the program is done, there will be a csv file named `expfloat.csv` (again, arbitrary name)
13. Create a folder called `expfloat` on the AutoEq folder (where 'autoeq.py' is located in)
14. Put the csv inside your created folder
15. In the AutoEq folder, rename `constants.py` to something else and replace with the one included from this project.


A few notes on the 'constants' file changes, you can take a look and tweak these if you have inaccuracies with the result:

	`DEFAULT_F_MIN = 20` to `DEFAULT_F_MIN = 1`
	Changes the minimum frequency that will be equalized. Without this, my results are missing an intended peak at 30Hz. 
	You can change this even lower, though the graph may look weird due to the logarithmic scale plot.
	
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

    
16. Open my_results/expfloat and take the Graphic EQ.txt file. The equalization curve is now usable on non-rooted devices.
`python autoeq.py --input_dir="expfloat" --output_dir="my_results/expfloat" --compensation="compensation/zero.csv" --equalize --show_plot --convolution_eq --fs=48000`

	The main thing is we will use the `zero.csv` as target to generate a new curve for AutoEq.
	
17. Open `my_results/expfloat` and take the Graphic EQ.txt file. The equalization curve is now usable on non-rooted devices.




Side note for my signal smoothing method using savgol_filter if you have issues:

	On line 95 of `testing123.py`:
		`yf=savgol_filter(yf,101,2)`
		
	The savgol_filter function takes 3 parameters for the smoothing:
	
		`yf` which is the array to be smoothened
		
		`101` (window_length) which needs to be an odd number and less than the size of `yf`. Reducing it will result in more rough/noisy output and increasing it results in a smoother, but more lossy output.
		
		`2` (polynomial order) which needs to be less than `window_length-1`. Changing this will affect how the smoothing process handles the smoothened curve to represent the input signal.
		
		If you have missing peaks, check the plotted graph when running the `testing123.py` file. 
		The smoothened curve is the orange curve and should not have a very different curve to the peak of the input curve (the blue curve). 
		You can mess around with the window_length by increasing/reducing it to see how it affects the smoothened curve.

The reason this may need to be tweaked is because this isn't really a 'one size fits all' solution since the input equalization can vary wildly in a case-by-case basis. 
I've tested the parameters to generate my Oratory1990 and Sonarworks tuning for my M50x. 
If you have trouble with tweaking the results, do let me know. If I have the time I may take a look at it and see what I can do. 

Do keep in mind that Graphic EQ are not the best solution for headphone equalization since it cannot reproduce some filter accurately.

If you have any issues or feedback and/or want to contribute, let me know about it. Many thanks.
