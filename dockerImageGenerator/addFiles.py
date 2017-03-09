from subprocess import call
import os
import sys
import tempfile
import Tkinter as tk
import tkMessageBox
imageName = None
filesToAdd = None
top = tk.Tk()
frame1 = tk.Frame(top)
frame1.pack()
frame2 = tk.Frame(top)
frame2.pack()
frame3 = tk.Frame(top)
frame3.pack(side=tk.BOTTOM)
L1 = tk.Label(frame1, text='File')
L1.pack(side = tk.LEFT)
E1 = tk.Entry(frame1, bd = 10)
E1.pack(side = tk.RIGHT)
L2 = tk.Label(frame2, text='New Image Name')
L2.pack(side = tk.LEFT)
E2 = tk.Entry(frame2, bd = 10)
E2.pack(side = tk.RIGHT)
def submitCallBack():
    imageName = E2.get()
    filesToAdd = E1.get()
    tkMessageBox.showinfo(imageName, imageName + ' '+filesToAdd)
    top.destroy()
B = tk.Button(frame3, text='Submit', command=submitCallBack)
B.pack()
top.mainloop()

if imageName == None:
    imageName = 'tempimage'
if filesToAdd == None:
    filesToAdd = 'test1.txt'

print 'filesToAdd: '+ filesToAdd
print 'imageName: '+ imageName
try:
    retcode = call('docker load -i ' + imageName + '.tar', shell=True)
    if retcode < 0:
        print >>sys.stderr, "Subprocess was terminated by signal", -retcode
    else:
        print >>sys.stderr, "Subprocess returned", retcode
    fp = tempfile.TemporaryFile()
    fp.write('FROM '+imageName + ':latest')
    # for i in filesToAdd:
    #     fp.write('ADD ' + i + ' /\n')
    fp.write('ADD ' + filesToAdd + ' /\n')
    ok = call('docker build -t tempimage1 .', shell=True)
    if ok < 0:
        print >>sys.stderr, "Subprocess was terminated by signal", -ok
    fp.close()
except OSError as e:
    print >>sys.stderr, "Execution failed:", e