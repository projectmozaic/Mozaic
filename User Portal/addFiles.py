from subprocess import call
import os
import sys
import Tkinter as tk
import tkMessageBox
imageName = None
filesToAdd = None
packgesName = None
top = tk.Tk()
top.wm_title('User Portal')
all_entries = []
frame2 = tk.Frame(top)
frame2.pack()
frame1 = tk.Frame(top)
frame1.pack()
frame3 = tk.Frame(top)
frame3.pack(side=tk.BOTTOM)
frame4 = tk.Frame(top)
frame4.pack(side=tk.BOTTOM)
frame5 = tk.Frame(top)
frame5.pack(side=tk.BOTTOM)
frame6 = tk.Frame(top)
frame6.pack(side=tk.BOTTOM)

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

L3 = tk.Label(frame4, text='Pip_Packages')
L3.pack(side = tk.LEFT)
E3 = tk.Entry(frame4, bd = 10)
E3.pack(side = tk.RIGHT)

L4 = tk.Label(frame5, text='Git_Packages_url')
L4.pack(side = tk.LEFT)
E4 = tk.Entry(frame5, bd = 10)
E4.pack(side = tk.RIGHT)

L5 = tk.Label(frame6, text='apt-get_Packages')
L5.pack(side = tk.LEFT)
E5 = tk.Entry(frame6, bd = 10)
E5.pack(side = tk.RIGHT)

def buildNewImage(imageName, filesToAdd, pipPackge, git_packages_url, aptGet_packages):
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
            if imageName == '':
                raise Execution('No imageName assigned.')
            fp.write('FROM '+imageName + ':latest\n')
            for i in filesToAdd:
                if i != "":
                    fp.write('ADD ' + i + ' /\n')
            if pipPackge != "":
                fp.write('RUN pip install ' + pipPackge  + '\n')
            if git_packages_url != "":
                fp.write("RUN git clone "+ git_packages_url+ "\n")
            if aptGet_packages != "":
                fp.write("RUN apt-get install "+ aptGet_packages + "\n")
        # fp.write('ADD ' + filesToAdd + ' /\n')
        ok = call('docker build -t tempimage1 .', shell=True)
        if ok < 0:
            print >>sys.stderr, "Subprocess was terminated by signal", -ok
        os.remove('Dockerfile')
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

def submitCallBack():
    imageName = E2.get()
    filesToAdd = E1.get()
    pipPackge = E3.get()
    git_packages_url = E4.get()
    aptGet_packages = E5.get()
    tkMessageBox.showinfo(imageName, imageName + ' '+filesToAdd)
    buildNewImage(imageName, filesToAdd, pipPackge, git_packages_url, aptGet_packages)
    # for i in range(0,len(all_entries)):
    #     all_entries[i] = all_entries[i].get()
    # if imageName == None:
    # 	imageName = 'tempimage'
    # if all_entries == None:
    #     filesToAdd = 'test1.txt'
    # else:
    #     filesToAdd = all_entries
    # try:
    #     retcode = call('docker load -i ' + imageName + '.tar', shell=True)
    #     if retcode < 0:
    #         print >>sys.stderr, "Subprocess was terminated by signal", -retcode2
    #     else:
    #         print >>sys.stderr, "Subprocess returned", retcode
    #     # fp = tempfile.TemporaryFile()
    #     with open('Dockerfile', 'wb') as fp:
    #         if imageName == '':
    #             raise Execution('No imageName assigned.')
    #         fp.write('FROM '+imageName + ':latest\n')
    #         for i in filesToAdd:
    #             if i != "":
    #                 fp.write('ADD ' + i + ' /\n')
    #         if pipPackge != "":
    #             fp.write('RUN pip install ' + pipPackge  + '\n')
    #         if git_packages_url != "":
    #             fp.write("RUN git clone "+ git_packages_url+ "\n")
    #         if aptGet_packages != "":
    #             fp.write("RUN apt-get install "+ aptGet_packages + "\n")
    #     # fp.write('ADD ' + filesToAdd + ' /\n')
    #     ok = call('docker build -t tempimage1 .', shell=True)
    #     if ok < 0:
    #         print >>sys.stderr, "Subprocess was terminated by signal", -ok
    #     os.remove('Dockerfile')
    # except OSError as e:
    #     print >>sys.stderr, "Execution failed:", e
    top.destroy()
B = tk.Button(frame3, text='Submit', command=submitCallBack)
B.pack()
top.mainloop()