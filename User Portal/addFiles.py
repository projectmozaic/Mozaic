from subprocess import call
import os
import sys
import Tkinter as tk
import tkMessageBox
imageName = None
filesToAdd = None
packgesName = None
top = tk.Tk()
all_entries = []
frame2 = tk.Frame(top)
frame2.pack()
frame1 = tk.Frame(top)
frame1.pack()
frame3 = tk.Frame(top)
frame3.pack(side=tk.BOTTOM)
frame4 = tk.Frame(top)
frame4.pack(side=tk.BOTTOM)
L1 = tk.Label(frame1, text='File     ')
L1.pack(side = tk.LEFT)
E1 = tk.Entry(frame1, bd = 10)
all_entries.append(E1)

def addNewEntryField():
    newFrame = tk.Frame(top)
    newFrame.pack()
    Li = tk.Label(newFrame, text = 'File')
    Li.pack(side = tk.LEFT)
    Ei = tk.Entry(newFrame, bd = 10)
    Ei.pack(side=tk.RIGHT)
    all_entries.append(Ei)
B1 = tk.Button(frame1, text='addFile', command=addNewEntryField)
B1.pack(side=tk.RIGHT)
E1.pack(side = tk.RIGHT)

L2 = tk.Label(frame2, text='ImageFrom')
L2.pack(side = tk.LEFT)
E2 = tk.Entry(frame2, bd = 10)
E2.pack(side = tk.RIGHT)

L3 = tk.Label(frame4, text='Add_Packages')
L3.pack(side = tk.LEFT)
E3 = tk.Entry(frame4, bd = 10)
E3.pack(side = tk.RIGHT)

def submitCallBack():
    imageName = E2.get()
    filesToAdd = E1.get()
    packgesName = E3.get()
    tkMessageBox.showinfo(imageName, imageName + ' '+filesToAdd)
    for i in range(0,len(all_entries)):
        all_entries[i] = all_entries[i].get()
    if imageName == None:
    	imageName = 'tempimage'
    if all_entries == None:
        filesToAdd = 'test1.txt'
    else:
        filesToAdd = all_entries
    try:
        retcode = call('docker load -i ' + imageName + '.tar', shell=True)
        if retcode < 0:
            print >>sys.stderr, "Subprocess was terminated by signal", -retcode2
        else:
            print >>sys.stderr, "Subprocess returned", retcode
        # fp = tempfile.TemporaryFile()
        with open('Dockerfile', 'wb') as fp:
            fp.write('FROM '+imageName + ':latest\n')
            for i in filesToAdd:
                if i != "":
                    fp.write('ADD ' + i + ' /\n')
            package_command = 'RUN pip install ' + packgesName  + '\n'
            fp.write(package_command)
        # fp.write('ADD ' + filesToAdd + ' /\n')
        ok = call('docker build -t tempimage1 .', shell=True)
        if ok < 0:
            print >>sys.stderr, "Subprocess was terminated by signal", -ok
        os.remove('Dockerfile')
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e
    top.destroy()
B = tk.Button(frame3, text='Submit', command=submitCallBack)
B.pack()
top.mainloop()
