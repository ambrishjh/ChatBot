from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr

bot = ChatBot("AJ")

trainer = ChatterBotCorpusTrainer(bot) #training bot with corpus data
trainer.train("chatterbot.corpus.english")



main = Tk() #main window
main.geometry("500x650") #width,Hieght
main.title("My Chat Bot")#title of main window
img= PhotoImage(file="bot.png")#creating photo image object
img1 =img.subsample(10,10)
photoL= Label(main, image=img1)
photoL.pack(pady=5)

def ask_from_bot():
    querry=textF.get()
    answer =bot.get_response(querry)
    msgs.insert(END,"You : " + querry)
    msgs.insert(END,"AJ : " + str(answer))
    textF.delete(0,END)

def voice_bot():
    recog = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Speak up!!!")
        audio = recog.listen(mic)
        try:
            text = recog.recognize_google(audio)#google web search API
            textF.insert(INSERT,text)
        except:
            print("Sorry speak again")

frame = Frame(main)
scroll= Scrollbar(frame)
msgs=Listbox(frame, width=80, height=20)
scroll.pack(side =RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textF= Entry(main, font=("Verdana",20))
textF.pack(fill=X, pady=15)

imgbtn= PhotoImage(file="btnicon.png").subsample(10,10)
button1= Button(main,image=imgbtn,command=voice_bot)
button1.pack()
button= Button(main,text="Ask From AJ", font=("Verdana",20),command=ask_from_bot)
button.pack()

main.mainloop()

