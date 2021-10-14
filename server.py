import socket,pickle
import speech_recognition
from tkinter import *
import tkinter.filedialog as tkFileDialog
import tkinter as ttk

def startSpeaking():
    HOST = '192.168.1.1'
#    HOST = 'localhost'
    PORT = 50007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while 1:
        
        speech = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            print("listening")
            audio = speech.listen(mic)
                
        try:
            text = speech.recognize_google(audio)
        except:
            text = ""
                
        print(text)
        data_string = pickle.dumps(text)
        
        conn.send(data_string)
    conn.close()


gui = Tk()
gui.geometry("250x100")
gui.title("Speech2Text")

c = ttk.Button(gui, text="Connect and Speak", command=startSpeaking)
c.place(relx=0.5, rely=0.5, anchor=CENTER)

gui.mainloop()
            
gui.close()
