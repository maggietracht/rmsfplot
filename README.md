RMSFPLOT

A plotting tool that generates plots from existing RMSF analysis data files.

Installation

Run this command in a terminal:
	
	python3 -m pip install rmsfplot

Importing

Import with the following command:

	from rmsfplot import rmplot

Running Commands

Run commands using the following format:

	rmplot."first or second command here"

Commands included:

First command:

	px_rmsf_analysis(a, b, c, d, e)

		-This function uses plotly.express to generate a plot from existing RMSF analysis data files (format .dat or .csv)

		
		-Parameter a:

		-Enter 'files' if your data is held within multiple files in one directory. Run this command within the directory that the files reside.

		-Enter 'folders' if your data is held within multiple files in multiple subdirectories. Run this command within the parent directory that holds all subdirectories.


		-Parameter b:

		-Enter 'True' if you would like an average line of the RMSF results to be displayed

		-Enter 'False' if you would not like an average line to be displayed


		-Parameter c:

		-Enter a string for the x axis label.

		-Enter 0 for the default option, which is 'Residue number'


		-Parameter d:

		-Enter a string for the y axis label.

		-Enter 0 for the default option, which is 'Atomic flux'


		-Parameter e:

		-Enter a string for the title of the plot

		-Enter 0 for the default option, which is 'RMSF plot'


Second command:

	plot_rmsf_analysis(a, b, c, d, e)

	-This function takes the same parameters as px_rmsf_analysis, but instead of generating a plot using plotly.express, matplotlib will be used to create a plot.

