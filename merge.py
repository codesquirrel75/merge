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
folder_label.grid(row=0, column=2, sticky="w")

source_folder_selected_label = ttk.Label(select_folder_frame, font="times 12", text="No folder selected")
source_folder_selected_label.grid(row=1, column=2, sticky="e")

destination_folder_selected_label = ttk.Label(select_folder_frame, font="times 12", text="No folder selected")
destination_folder_selected_label.grid(row=2, column=2, sticky="e")

wordInFileName = ttk.Label(file_setup_frame, text="Type of Data: ")
wordInFileName.grid(row=0, column=0)

message_label = ttk.Label(display_frame, font="times 12")
message_label.grid(row=0, column=0)


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
		source_folder_selected_label['text']= folder

def selectDestinationFolder():
	newFolder = filedialog.askdirectory()
	
	if newFolder != "":
		folder = newFolder
		destination_folder_selected_label['text']= folder

def merge():
	sourceFolder = source_folder_selected_label['text']
	destinationFolder = destination_folder_selected_label['text']
	if dataType.get() == 1:
		word = "pit"
	elif dataType.get() == 2:
		word = "match"
	else:
		message_label['text'] = "Sorry there was an error."
		print("Sorry there was an error.")
		return

	newFile = word + "Data.csv"

	if Path(destinationFolder + "/" + newFile).exists():
		destfile = open(destinationFolder + "/" + newFile, 'ab')
	else:
		labels =open(destinationFolder + "/" + word + "Labels.csv", 'rb')
		destfile = open(destinationFolder + "/" + newFile, 'ab')
		destfile.write(labels.read())
		labels.close()

	for filename in os.listdir(sourceFolder):
		if filename.lower().find(word) != -1 and filename.endswith(".csv"):
			if filename == word + "Data.csv" or filename == word + "Labels.csv":
				continue
			else:
				f = open(sourceFolder + "/" + filename, 'rb')
				destfile.write(f.read())
				f.close()
		else:
			continue

	destfile.close()
	message_label['text'] = "Operation Complete! Check it out!"
	print("Operation Complete! Check it out!")


def resetPit():
	folder = destination_folder_selected_label['text']
	if folder.find("pit") != -1:
		f = open(folder + "/pitData.csv","wb")
		fl = open(folder +"/pitLabels.csv","rb")
		f.write(fl.read())
		f.close
		fl.close
		message_label['text'] = "pitData.csv has been reset!"
		print("pitData.csv has been reset!")
	else:
		message_label['text'] = "Oh Snap! I could not reset pitData file."
		print("Oh Snap! I could not reset pitData file.")
		return


def resetMatch():
	folder = destination_folder_selected_label['text']
	if folder.find("match") != -1:
		f = open(folder + "/matchData.csv","wb")
		fl = open(folder +"/matchLabels.csv","rb")
		f.write(fl.read())
		f.close
		fl.close
		message_label['text'] = "matchData.csv has been reset!"
		print("matchData.csv has been reset!")
	else:
		message_label['text'] = "Oh Snap! I could not reset matchData file."
		print("Oh Snap! I could not reset matchData file.")
		return



sourceFolderBtn = ttk.Button(select_folder_frame, text="select source folder", width=30, command=selectSourceFolder)
sourceFolderBtn.grid(row=1, column=1)

destinationFolderBtn = ttk.Button(select_folder_frame, text="select destination folder", width=30, command=selectDestinationFolder)
destinationFolderBtn.grid(row=2, column=1)



mergeBtn = ttk.Button(file_setup_frame, text="Merge Files", width=14, command=merge)
mergeBtn.grid(row=2, column=2)

resetPitDataBtn = ttk.Button(file_setup_frame, text="Reset Pit Data",width=14, command=resetPit).grid(row=4, column=0, sticky="ew")

resetMatchDataBtn = ttk.Button(file_setup_frame, text="Reset Match Data",width=14, command=resetMatch).grid(row=4, column=1, sticky="ew")



root.mainloop()