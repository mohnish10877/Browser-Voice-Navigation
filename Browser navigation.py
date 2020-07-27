                                                                
import speech_recognition as sr  
import keyboard                                                                    
def record():
    r = sr.Recognizer()
    f = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")                                                                                   
        audio = r.record(source, duration = 1.5)   
    try:
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
        record()        
    dict = { "new tab" : "ctrl + t", "bookmark" : "ctrl + d", "Close tab": "ctrl + w", 
             "switch" : "ctrl + tab", "refresh": "f5", "browse" : "ctrl + l", 
             "back" : "alt + left arrow", "Next" : "alt + right arrow", 
             "download" : "ctrl + j", "open file": "ctrl + o", "full screen": "f11",
             "scroll down" : "down arrow", "scroll up": "up arrow", "next link" : "tab"}
    for x in dict:
        if r.recognize_google(audio)== x:
            keyboard.press_and_release(dict[x])
            if r.recognize_google(audio) == "browse":
                with sr.Microphone() as source:
                    print("Search:")                                                                                   
                    s=f.record(source, duration = 3)
                    search = f.recognize_google(s)
                try:
                    print("You said " + search)
                    keyboard.write(search,delay=0.1)
                    keyboard.press_and_release("ctrl + enter")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                keyboard.press_and_release("enter")
        if r.recognize_google(audio)== "disable":
            window.destroy()
def do():
    while window:
        record()
from tkinter import *
window = Tk()
window.title("YTNAV")
window.geometry("400x300")
button_frame = Frame(window, width = 250, height = 50)
button_frame.pack(padx = 10, pady = 10)
Listen_button = Button(button_frame, text = "Listen", width = 35,
font = ('arial',10,'bold'), fg = "red" ,command = do)
Listen_button.grid(row = 4, column = 0, padx = 2, pady = 2)
window.mainloop()