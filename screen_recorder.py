from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"), 5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()

#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

#heading
lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)
image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=0)

#entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording25")

#button
start = Button(root, text="Start", font="arial 22", bd=0, command=start_rec)
start.place(x=147, y=250)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#fff", command=pause_rec)
pause.place(x=70, y=405)

image5 = PhotoImage(file="resume.png")
pause = Button(root, image=image5, bd=0, bg="#fff", command=resume_rec)
pause.place(x=170, y=400)

image6 = PhotoImage(file="stop.png")
pause = Button(root, image=image6, bd=0, bg="#fff", command=stop_rec)
pause.place(x=280, y=405)


root.mainloop()
