from tkinter import *
import tkinter.messagebox as box
import hashlib
# MD5 local test strings
# M:/Downloads/Universal-USB-Installer-1.9.7.0.exe
# 6EF9B8E4AAF56E0D48EA8E22ECC90A9D

window = Tk()
window.title('Hash Check App')
window.resizable(0,0)

def dialog():
    path1 = fp.get()
    parent = hsh.get()
    htype = hashtype.get()

    try:
        if htype == 'MD5':
            hasher = hashlib.md5()
        elif htype == 'SHA1':
            hasher = hashlib.sha1()
        elif htype == 'SHA256':
            hasher = hashlib.sha256()
        elif htype == 'SHA512':
            hasher = hashlib.sha512()
# MAIN HASH FUNCTION ===============================
        BLOCKSIZE = 65536
        with open(path1, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        filehash = hasher.hexdigest()
# END HASH FUNCTION ===============================
        if not parent:
            box.showinfo(htype+' Hash Generated',filehash)
            hsh.set(filehash)
        else:
            if filehash == parent or filehash.upper() == parent:
                print("match")
                box.showinfo('Success','The file has is a match!')
            else:
                print("no match")
                print(hasher.hexdigest())
                box.showwarning('Failure','The file and the supplied hash do not match.')
    except FileNotFoundError:
        box.showerror('Error','File path was either left blank or the specified file does not exist.')

fp = StringVar()
filepath = Entry(window, textvariable=fp, width=100)
fplbl = Label(window, text="File Path:")
hsh = StringVar()
hashword = Entry(window,textvariable=hsh,width=100)
hlbl = Label(window, text="Hash:")
btn = Button(window,text = 'Run', command = dialog, width=10)
hashtype = StringVar()
# img = PhotoImage(file = "M:/Python/Capture.gif")
# imgLbl = Label(window, image = img)

# Geometry ====================================
fplbl.grid(row = 1, column = 1, padx = (10,5),pady=(10,5),sticky=W)
filepath.grid(row=1,column=2,padx=(0,10),pady=(10,5),columnspan=6)
hlbl.grid(row = 2, column = 1, padx = (10,5),pady = (5,10),sticky=W)
hashword.grid(row=2, column=2,padx=(0,10),pady = (5,10),columnspan=6)
btn.grid(row =3,column =3,rowspan=4,sticky=W,padx=(0,10))
# imgLbl.grid(row =3, column =4,columnspan=4,rowspan=4)

# GENERATE RADIO BUTTONS
hashoptions = ['MD5','SHA1','SHA256','SHA512']
i = 0
for txt in hashoptions:
    i += 1
    b = Radiobutton(window, text=txt, padx=10, variable=hashtype, value=txt)
    b.grid(row =i+2, column = 2,sticky=W)
    if i == 1:
        b.select()
    if i == 4:
        b.grid(pady = (0,5))

window.mainloop()
