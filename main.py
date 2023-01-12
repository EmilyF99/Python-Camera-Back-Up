# Media Tech Assignment - Emily Fletcher 18410839
# Import Statements

import motion
from tkinter import *
from tkvideo import tkvideo
import tkinter as tk
from tkinter import ttk

videoPath1 = 'nv232.MOV'
# video1 = motion.motion_detection(videoPath1)

# Raw Videos
video1 = videoPath1
video2 = videoPath1
video3 = videoPath1
video4 = videoPath1

MDVideo1 = motion.motion_detection(videoPath1)
MDVideo2 =  motion.motion_detection(videoPath1)
MDVideo3 =  motion.motion_detection(videoPath1)
MDVideo4 =  motion.motion_detection(videoPath1)

root = tk.Tk()
root.title("Warehouse Security Camera")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Live Feed')
tabControl.add(tab2, text='Motion Detection')
tabControl.add(tab3, text='Saved Motion')
tabControl.pack(expand=1, fill="both")

# Live Feed Tab
LFLabel = tk.Label(tab1, text="Live Feed")
VSource1Pos = tk.Label(tab1, text="Source 1")
VSource1Lb = tk.Label(tab1, text="Source 1")
source1 = tkvideo(video1, VSource1Pos, size=(300, 150))
source1.play()

VSource2Pos = tk.Label(tab1, text="Source 2")
VSource2Lb = tk.Label(tab1, text="Source 2")
source2 = tkvideo(video2, VSource2Pos, size=(300, 150))
source2.play()

VSource3Pos = tk.Label(tab1, text="Source 3")
VSource3Lb = tk.Label(tab1, text="Source 3")
source3 = tkvideo(video3, VSource3Pos, size=(300, 150))
source3.play()

VSource4Pos = tk.Label(tab1, text="Source 4")
VSource4Lb = tk.Label(tab1, text="Source 3")
source4 = tkvideo(video4, VSource4Pos, size=(300, 150))
source4.play()

actionLogLb = tk.Label(tab1, text="Action Log")
actionLog = tk.Text(tab1, height=5)

LFLabel.grid(row=0, column=0)
VSource1Lb.grid(row=1, column=0)
VSource1Pos.grid(row=2, column=0)
VSource2Lb.grid(row=1, column=1)
VSource2Pos.grid(row=2, column=1)
VSource3Lb.grid(row=3, column=0)
VSource3Pos.grid(row=4, column=0)
VSource4Lb.grid(row=3, column=1)
VSource4Pos.grid(row=4, column=1)
actionLogLb.grid(row=5, column=0)
actionLog.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

# Motion Detection Tab
MDLabel = tk.Label(tab2, text="Motion Detection")

MDSource1Pos = tk.Label(tab2, text="Source 1")
MDSource1Lb = tk.Label(tab2, text="Source 1")
MDSource1 = tkvideo(video1, MDSource1Pos, size=(300, 150))
MDSource1.play()

MDSource2Pos = tk.Label(tab2, text="Source 2")
MDSource2Lb = tk.Label(tab2, text="Source 2")
MDSource2 = tkvideo(video2, MDSource2Pos, size=(300, 150))
MDSource2.play()

MDSource3Pos = tk.Label(tab2, text="Source 3")
MDSource3Lb = tk.Label(tab2, text="Source 3")
MDSource3 = tkvideo(video3, MDSource3Pos, size=(300, 150))
MDSource3.play()

MDSource4Pos = tk.Label(tab2, text="Source 4")
MDSource4Lb = tk.Label(tab2, text="Source 4")
MDSource4 = tkvideo(video4, MDSource4Pos, size=(300, 150))
MDSource4.play()

MDactionLogLb = tk.Label(tab2, text="Action Log")
MDactionLog = tk.Text(tab2, height=5)

MDLabel.grid(row=0, column=0)
MDSource1Lb.grid(row=1, column=0)
MDSource1Pos.grid(row=2, column=0)
MDSource2Lb.grid(row=1, column=1)
MDSource2Pos.grid(row=2, column=1)
MDSource3Lb.grid(row=3, column=0)
MDSource3Pos.grid(row=4, column=0)
MDSource4Lb.grid(row=3, column=1)
MDSource4Pos.grid(row=4, column=1)
MDactionLogLb.grid(row=5, column=0)
MDactionLog.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)


SMLabel = tk.Label(tab3, text="Saved Motion")
myLabel14 = tk.Label(tab3, text="Scroll Box")

SMLabel.grid(row=0, column=0)
myLabel14.grid(row=1, column=0)


root.mainloop()
