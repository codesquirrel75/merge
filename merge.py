from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import os, os.path
from pathlib import Path

root = Tk()

# ----get monitor height and width to make a full screen window. ----

width = int(root.winfo_screenwidth() * .4)
height=400

file = ""
newFile = ""
folder=""


message = "fun, come, went, Junk"

photo = PhotoImage(file="icon.png")

root.title("1918 NC Gears Merge Data")

root.tk.call('wm', 'iconphoto', root._w, photo)

root.geometry("{}x{}+600+200".format(width, height))

select_folder_frame = ttk.Frame(root, width=width, height=height/3)
select_folder_frame.grid(row=0, column=1)

file_setup_frame = ttk.Frame(root, width=width, height=height/3)
file_setup_frame.grid(row=1, column=1)

display_frame = ttk.Frame(root, width=width, height=height/3)
display_frame.grid(row=2, column=1)



folder_label = ttk.Label(select_folder_frame,font="times 20 bold", text="Folder Selected: ")
folder_label.grid(row=0, column=0, sticky="w")

folder_selected_label = ttk.Label(select_folder_frame, font="times 12", text="No folder selected")
folder_selected_label.grid(row=0, column=0, sticky="e")



wordInFileName = ttk.Label(file_setup_frame, text="Type of Data: ")
wordInFileName.grid(row=0, column=0)



def setFile():
	if dataType.get() == 1:
		dotCsvLabel['text'] = "pitData.csv"
	elif dataType.get() == 2:
		dotCsvLabel['text'] = "matchData.csv"

dataType= tk.IntVar()

pitDataTypeRadioBtn = ttk.Radiobutton(file_setup_frame, variable=dataType, value=1, text="pit", command=setFile)
pitDataTypeRadioBtn.grid(row=0,column=1)

matchDataTypeRadioBtn = ttk.Radiobutton(file_setup_frame, variable=dataType, value=2, text="match", command=setFile)
matchDataTypeRadioBtn.grid(row=0,column=2)

newFileName = ttk.Label(file_setup_frame, text="New File Name: ")
newFileName.grid(row=1, column=0)

dotCsvLabel = ttk.Label(file_setup_frame, text="")
dotCsvLabel.grid(row=1, column=2)

def selectSourceFolder():
	newFolder = filedialog.askdirectory()
	
	if newFolder != "":
		folder = newFolder
		folder_selected_label['text']= folder

def merge():
	folder = folder_selected_label['text']
	if dataType.get() == 1:
		word = "pit"
	elif dataType.get() == 2:
		word = "match"
	else:
		print("Sorry there was an error.")
		return

	newFile = word + "Data.csv"

	if Path(folder + "/" + newFile).exists():
		destfile = open(folder + "/" + newFile, 'a')
	else:
		labels =open(folder + "/" + word + "Labels.csv", 'r')
		destfile = open(folder + "/" + newFile, 'a')
		destfile.write(labels.read() + "\n")
		labels.close()

	for filename in os.listdir(folder):
		if filename.lower().find(word) != -1 and filename.endswith(".csv"):
			if filename == word + "Data.csv" or filename == word + "Labels.csv":
				continue
			else:
				f = open(folder + "/" + filename, 'r')
				destfile.write(f.read() + "\n")
				f.close()
		else:
			continue

	destfile.close()
	print("Operation Complete! Check it out!")


def resetPit():
	folder = folder_selected_label['text']
	if folder.find("pit") != -1:
		f = open(folder + "/pitData.csv","w")
		fl = open(folder +"/pitLabels.csv","r")
		f.write(fl.read() + "\n")
		f.close
		fl.close
	else:
		return


def resetMatch():
	folder = folder_selected_label['text']
	if folder.find("pit") != -1:
		f = open(folder + "/matchData.csv","w")
		fl = open(folder +"/matchLabels.csv","r")
		f.write(fl.read() + "\n")
		f.close
		fl.close
	else:
		return



folderBtn = ttk.Button(select_folder_frame, text="select source folder", width=60, command=selectSourceFolder)
folderBtn.grid(row=1, column=0)

mergeBtn = ttk.Button(file_setup_frame, text="Merge Files", width=14, command=merge)
mergeBtn.grid(row=2, column=2)

resetPitDataBtn = ttk.Button(file_setup_frame, text="Reset Pit Data",width=14, command=resetPit).grid(row=4, column=0, sticky="ew")

resetMatchDataBtn = ttk.Button(file_setup_frame, text="Reset Match Data",width=14, command=resetMatch).grid(row=4, column=1, sticky="ew")



root.mainloop()