# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
from pathlib import Path
import plotly.express as px

def plot_rmsf_analysis(a,b,c,d,e):

	if a == 'folders':
		path = os.getcwd()
		fig, ax = plt.subplots()
		all_dfs = []
		for f in glob.glob(os.path.join(path, '**', '*.dat'), recursive=True):
		
			path1 = Path(f)
			df = pd.read_csv(f, header=0, sep=r'\s+')
			all_dfs.append(df)
			ax.plot(df.iloc[:,0], df.iloc[:,1], label = path1.parent.name, linewidth= .2)
	
		combined_df = pd.concat(all_dfs)
		avg_line = combined_df.groupby('#Res')['AtomicFlx'].mean().reset_index()

		if b == 'True':
			ax.plot(avg_line.iloc[:,0], avg_line.iloc[:,1], color='red', linewidth=1, label='Average')

		elif b == 'False':
			pass

		else:
			return "Invalid parameter for average line plotting preference. Please enter 'True' if you would like the average of all RMSF data to appear on your plot, or 'False' if you would not like the average line to appear."


	elif a == 'files':
		path = os.getcwd()
		fig, ax = plt.subplots()
		all_dfs = []
		for f in glob.glob(os.path.join(path, "*.dat*")):
			if os.path.isfile(f):
				df = pd.read_csv(f, header=0, sep=r'\s+')
				all_dfs.append(df)
				ax.plot(df.iloc[:,0], df.iloc[:,1], label = Path(f).name, linewidth= .2)

		combined_df = pd.concat(all_dfs)
		avg_line = combined_df.groupby('#Res')['AtomicFlx'].mean().reset_index()
        		
		if b == 'True':
			ax.plot(avg_line.iloc[:,0], avg_line.iloc[:,1], color='red', linewidth=1, label='Average')
        
		elif b == 'False':
			pass

		else:
			return "Invalid parameter for average line plotting preference. Please enter 'True' if you would like the average of all RMSF data to appear on your plot, or 'False' if you would not like the average line to appear."


	else:
		return "Invalid parameter for data location. Please enter 'files' if your data is listed in multiple files in one directory, or enter 'folders' if your data is listed in files within multiple subdirectories."

	if type(c) is str:
		plt.xlabel(c)
	else:
		plt.xlabel('Residue number')

	if type(d) is str:
		plt.ylabel(d)
	else: 
		plt.ylabel('Atomic flux')

	if type(e) is str:
		plt.title(e)
	else:
		plt.title('RMSF plot')

	plt.legend()


	plt.show()


def px_rmsf_analysis(a,b,c,d,e):

	fig = None
	if a == 'folders':
		path = os.getcwd()
		all_dfs = []
		for f in glob.glob(os.path.join(path, '**', '*.dat'), recursive=True):
			path1 = Path(f)
			df = pd.read_csv(f, header=0, sep=r'\s+')
			df['source'] = path1.parent.name
			all_dfs.append(df)
		combined_df = pd.concat(all_dfs)

		if b == 'True':
			avg_line = combined_df.groupby('#Res')['AtomicFlx'].mean().reset_index()
			avg_line['source'] = 'Average'
			combined_df = pd.concat([combined_df, avg_line])
			
		elif b == 'False':
			pass
			
		else:
			return "Invalid parameter for average line plotting preference. Please enter 'True' if you would like the average of all RMSF data to appear on your plot, or 'False' if you would not like the average line to appear."
		fig = px.line(combined_df, x='#Res', y='AtomicFlx', color='source')
			
	elif a == 'files':
		path = os.getcwd()
		all_dfs = []
		for f in glob.glob(os.path.join(path, "*.dat*")):	
			if os.path.isfile(f):
				df = pd.read_csv(f, header=0, sep=r'\s+')
				df['source'] = Path(f).name
				all_dfs.append(df)
		combined_df = pd.concat(all_dfs)

		if b == 'True':
			avg_line = combined_df.groupby('#Res')['AtomicFlx'].mean().reset_index()
			avg_line['source'] = 'Average'
			combined_df = pd.concat([combined_df, avg_line])

		elif b == 'False':
			pass

		else:
			return "Invalid parameter for average line plotting preference. Please enter 'True' if you would like the average of all RMSF data to appear on your plot, or 'False' if you would not like the average line to appear."
		fig = px.line(combined_df, x='#Res', y='AtomicFlx', color='source')

	else:
		return "Invalid parameter for data location. Please enter 'files' if your data is listed in multiple files in one directory, or enter 'folders' if your data is listed in files within multiple subdirectories."
	
	if fig:
		x_label = c if type(c) is str else 'Residue number'
		y_label = d if type(d) is str else 'Atomic flux'
		title = e if type(e) is str else 'RMSF plot'
			
		fig.update_layout(
			xaxis_title = x_label,
			yaxis_title = y_label,
			title_text = title
			)
	fig.show()



