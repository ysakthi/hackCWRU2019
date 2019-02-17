from Tkinter import *
import tkMessageBox
import complexity
import translate

texts = []

window = Tk()
window.geometry("5000x5000")

top_frame = Frame(window).pack(fill="both", expand=True)
bottom_frame = Frame(window).pack(fill="both", expand=True, side = "bottom")

window.title("Welcome to the worldly Translator app")
window.geometry('350x200')

lbl = Label(top_frame, text="Hello").pack()

txt = Entry(top_frame,width=100)
txt.pack()

def sub_click():
    c_sc = complexity.score(txt.get()) * 0.5
    print(txt.get())
    s_sc = translate.get_similarity_score(txt.get()) * 0.5
    result = round(c_sc + s_sc, 3)
    texts.append((txt.get(), result))
    result_lbl = Label(top_frame, text=str(s_sc) + "\t and \t" + str(round(c_sc, 2))).pack()

def clicked():
    lbl = Label(top_frame, text="Your similarity and complexity scores are:").pack()
    sub_click()


btn = Button(top_frame, text="Travel the world!", command=clicked).pack()

def endgame():
    table = ""
    for text, score in texts:
        table += str(score) + ":\t" + text + "\n"
    tkMessageBox.showinfo("Final scores", table)

endgame = Button(bottom_frame, text="Finish game", command = endgame).pack()
window.mainloop()
