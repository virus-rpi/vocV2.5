# Music & Sounds: https://www.bensound.com; https://mixkit.co; https://www.fesliyanstudios.com pictures:
# https://charactercreator.org/#sex=m&skinColor=%23ffdcb2&irisColor=%230efb05&hairColor=%231a1a1a&pupils=feline
# &body_head=oval&body=android-00&ears=pointed&iris=default&nose=default&facialhair=beard_boxed&hair=wreckingball
# &emotion=alertness&glasses=hipster&warpaint=clawmarks&tatoo=aum_right&shirt=tanktop&vest=athlete&gloves=motorcycle
# &underwear=boxers&pants=cargo&belt=cargo&kneepads=skate&socks=socks&shoes=moon

from tkinter import *
import random
import json
import sys
from cdifflib import CSequenceMatcher
from tkinter import messagebox
from settings import Settings
from langdetect import detect
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

richtig = 0
falsch = 0
score = 0
level = 1
name = ""
askName = False
sound = False
music = False
lastQuestion = ""


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


mixer.init()
levelUpSound = mixer.Sound(resource_path("sounds/levelup.wav"))
sendSounds = ["whoosh1.wav", "whoosh2.wav", "whoosh3.wav", "whoosh4.wav"]
sendSound = mixer.Sound(resource_path("sounds/" + random.choice(sendSounds)))
uffSounds = ["uff1.wav", "uff2.wav", "uff3.wav"]
uffSound = mixer.Sound(resource_path("sounds/" + random.choice(uffSounds)))
bgMusic = random.choice(["epic", "slowmotion", "birthofahero"])

voc = {}


def similar(a, b):
    return CSequenceMatcher(None, a, b).ratio()


def saveData():
    wData = {"vocList": voc, "scoreVar": score, "name": name}
    if sound:
        wData["sound"] = 1
    else:
        wData["sound"] = 0
    if music:
        wData["music"] = 1
    else:
        wData["music"] = 0
    with open(resource_path("data.json"), "w") as f:
        json.dump(wData, f)


def loadData():
    global voc
    global score
    global ChatLog
    global name
    global askName
    global sound
    global music
    with open(resource_path("data.json")) as f:
        rData = json.load(f)
        voc = rData["vocList"]
        score = rData["scoreVar"]
        sound = bool(rData["sound"])
        music = bool(rData["music"])
        if rData["name"] != "":
            name = rData["name"]
        else:
            askName = True
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Bot: Whats your name?" + "\n\n")
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def delete():
    global voc
    try:
        del voc[DelEntryBox.get("1.0", "end-1c").strip()]
        DelEntryBox.delete("0.0", END)
    except:
        pass


def add_if_key_not_exist(dict_obj, key, value):
    if key not in dict_obj:
        voc.update({key: value})


def append(*this_is_an_uselss_variable):
    print(
        LateinEntryBox.get("1.0", "end-1c").strip()
        + ":"
        + DeutschEntryBox.get("1.0", "end-1c").strip()
    )
    add_if_key_not_exist(
        voc,
        LateinEntryBox.get("1.0", "end-1c").strip(),
        DeutschEntryBox.get("1.0", "end-1c").strip(),
    )
    LateinEntryBox.delete("0.0", END)
    DeutschEntryBox.delete("0.0", END)


def send(*this_is_an_uselss_variable):
    global falsch
    global richtig
    global score
    global voc
    global r_key
    global name
    global askName
    global lastQuestion

    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)
    similarity = 0

    if msg != "":
        in_str = msg
        ChatLog.config(state=NORMAL)
        if name != "":
            ChatLog.insert(END, name + ": " + msg + "\n\n")
        else:
            ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        if not askName:
            similarity = similar(in_str, voc.get(r_key))
            print(f"Similarity: {similarity}")

        if askName:
            name = in_str
            askName = False
            r_key = random.choice(list(voc.keys()))
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Bot: " + r_key + "\n\n")
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            return

        if in_str == voc.get(r_key):
            lastQuestion = "_joy"
            if sound:
                mixer.Sound.play(sendSound)
            res = "Perfect!"
            richtig += 1
            score += 2
        elif similarity > 0.8:
            lastQuestion = ""
            if sound:
                mixer.Sound.play(sendSound)
            res = "Correct"
            richtig += 1
            score += 1
        elif in_str == "scoreboard":
            lastQuestion = ""
            res = (
                    "Correct words: "
                    + str(richtig)
                    + "\nIncorrect words: "
                    + str(falsch)
                    + "\nScore: "
                    + str(score)
            )
        elif in_str == "levelup" and name == "virus":
            lastQuestion = ""
            score += 10
            res = "Ok"
        elif in_str == "leveldown" and name == "virus":
            lastQuestion = ""
            score -= 10
            res = "Ok"
        elif in_str == "kp":
            lastQuestion = ""
            res = "But that is a pity. \nCorrect was: " + str(voc.get(r_key))
            score -= 1
        elif in_str == "veto":
            lastQuestion = ""
            falsch -= 1
            richtig += 1
            score += 2
            if sound:
                mixer.Sound.play(sendSound)
            res = "Sorry for the mistake...."
        else:
            lastQuestion = "_angry"
            if sound:
                mixer.Sound.play(uffSound)
            res = "Unfortunately, this is wrong. Correct \nwas: " + str(voc.get(r_key))
            falsch += 1
            score -= 2
        ChatLog.insert(END, "Bot: " + res + "\n\n")
    r_key = random.choice(list(voc.keys()))
    ChatLog.insert(END, "Bot: " + r_key + "\n\n")
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)


def getShortcut(event):
    if event.keysym == "s":
        settings()
    if event.keysym == "h":
        help()


def settings():
    global sound
    global music
    module = Settings(base, on_image, off_image, bool(sound), bool(music))
    sound, music = module.main()
    print(sound, music)


def info():
    messagebox.showinfo("Whats new?", " - This menu bar\n - The settings")


def credit():
    messagebox.showinfo("Credits",
                        "Code: virus_rpi\nMusic & Sounds: https://www.bensound.com; https://mixkit.co; "
                        "https://www.fesliyanstudios.com \nPictures: https://charactercreator.org")

def help():
    messagebox.showinfo("Help", "-scoreboard: Shows the current data \n-veto: Objection to the last valuation\n-kp: If you dont know the answer")


def initMenu(base):
    menu = Menu(base)
    base.config(menu=menu)
    fileMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label="Settings", command=settings, accelerator="Strg+S")
    infoMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Info', menu=infoMenu)
    infoMenu.add_command(label="Whats new?", command=info)
    infoMenu.add_command(label="Credits", command=credit)
    infoMenu.add_command(label="Help", command=help, accelerator="Strg+H")


base = Tk()
base.title("Vocabulary")
base.geometry("900x520")
base.iconbitmap(resource_path("9108.ico"))
base.resizable(width=FALSE, height=FALSE)

base.bind('<Control-s>', getShortcut)
base.bind('<Control-H>', getShortcut)

# Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width=50, font="Arial")

ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog["yscrollcommand"] = scrollbar.set

# Create Button to send message
SendButton = Button(
    base,
    font=("Verdana", 12, "bold"),
    text="↑ Apply",
    width="10",
    height=5,
    bd=0,
    bg="#32de97",
    activebackground="#3c9d9b",
    fg="#ffffff",
    command=send,
)
AppendButton = Button(
    base,
    font=("Verdana", 12, "bold"),
    text="+ Add",
    width="15",
    height=3,
    bd=0,
    bg="#89CFF0",
    activebackground="#4169E1",
    fg="#ffffff",
    command=append,
)

DeleteButton = Button(
    base,
    font=("Verdana", 12, "bold"),
    text="- Delete",
    width="15",
    height=3,
    bd=0,
    bg="#bb4039",
    activebackground="#8B0000",
    fg="#ffffff",
    command=delete,
)

# Create the box to enter message
bild0 = PhotoImage(file=resource_path("pictures/1.png"))
bild0_joy = PhotoImage(file=resource_path("pictures/1_joy.png"))
bild0_angry = PhotoImage(file=resource_path("pictures/1_angry.png"))
bild1 = PhotoImage(file=resource_path("pictures/1.png"))
bild1_joy = PhotoImage(file=resource_path("pictures/1_joy.png"))
bild1_angry = PhotoImage(file=resource_path("pictures/1_angry.png"))
bild2 = PhotoImage(file=resource_path("pictures/2.png"))
bild2_joy = PhotoImage(file=resource_path("pictures/2_joy.png"))
bild2_angry = PhotoImage(file=resource_path("pictures/2_angry.png"))
bild3 = PhotoImage(file=resource_path("pictures/3.png"))
bild3_joy = PhotoImage(file=resource_path("pictures/3_joy.png"))
bild3_angry = PhotoImage(file=resource_path("pictures/3_angry.png"))
bild4 = PhotoImage(file=resource_path("pictures/4.png"))
bild4_joy = PhotoImage(file=resource_path("pictures/4_joy.png"))
bild4_angry = PhotoImage(file=resource_path("pictures/4_angry.png"))
bild5 = PhotoImage(file=resource_path("pictures/5.png"))
bild5_joy = PhotoImage(file=resource_path("pictures/5_joy.png"))
bild5_angry = PhotoImage(file=resource_path("pictures/5_angry.png"))
bild6 = PhotoImage(file=resource_path("pictures/6.png"))
bild6_joy = PhotoImage(file=resource_path("pictures/6_joy.png"))
bild6_angry = PhotoImage(file=resource_path("pictures/6_angry.png"))
bild7 = PhotoImage(file=resource_path("pictures/7.png"))
bild7_joy = PhotoImage(file=resource_path("pictures/7_joy.png"))
bild7_angry = PhotoImage(file=resource_path("pictures/7_angry.png"))
bildLabel = Label(master=base, image=bild2)

EntryBox = Text(base, borderwidth=0, bd=0, bg="white", width=29, height="5", font="Arial")
EntryBox.bind("<Return>", send)

initMenu(base)

leveltxt = "Level " + str(level)
levelText = Label(
    base, bd=0, bg="SystemButtonFace", height="8", width="50", font="Arial"
)
ChatText = Label(
    base, bd=0, bg="SystemButtonFace", height="8", width="50", font="Arial 13 bold"
)
TransformText = Label(
    base, bd=0, bg="SystemButtonFace", height="8", width="50", font="Arial 13 bold"
)
MotivatorText = Label(
    base, bd=0, bg="SystemButtonFace", height="8", width="50", font="Arial 13 bold"
)

LateinEntryBox = Text(base, bd=0, bg="white", width=29, height="5", font="Arial")
DeutschEntryBox = Text(base, bd=0, bg="white", width=29, height="5", font="Arial")
DeutschEntryBox.bind("<Return>", append)
LateinEntryBoxText = Label(
    base, bd=0, bg="SystemButtonFace", width="29", height="5", font="Arial"
)
DeutschEntryBoxText = Label(
    base, bd=0, bg="SystemButtonFace", width="29", height="5", font="Arial"
)
DelText = Label(base, bd=0, bg="SystemButtonFace", height="8", width="50", font="Arial")
DelEntryBox = Text(base, bd=0, bg="white", width=29, height="5", font="Arial")

LateinEntryBoxText.config(text='Latin (z.B. "ire")')
DeutschEntryBoxText.config(text='English (e.g. "walk, \nrun")')
levelText.config(text=leveltxt)
ChatText.config(text="Your Challenge")
DelText.config(text="Lat. word (z.B. ire)")
TransformText.config(text="Edit Your List")
MotivatorText.config(text="Your Score")

# Place all components on the screen
scrollbar.place(x=376, y=26, height=386)
ChatLog.place(x=6, y=26, height=406, width=370)
#
EntryBox.place(x=128, y=441, height=50, width=265)
#
LateinEntryBox.place(x=700, y=250, height=50, width=190)
DeutschEntryBox.place(x=700, y=350, height=50, width=190)
DelEntryBox.place(x=700, y=45, height=80, width=190)
#
LateinEntryBoxText.place(x=700, y=225, height=20, width=190)
DeutschEntryBoxText.place(x=700, y=305, height=40, width=190)
#
SendButton.place(x=6, y=441, height=50)
AppendButton.place(x=706, y=441, height=50)
DeleteButton.place(x=706, y=150, height=50)
#
bildLabel.place(x=400, y=-20, height=500, width=275)
#
levelText.place(x=450, y=20, height=20, width=190)
DelText.place(x=690, y=20, height=20, width=210)
ChatText.place(x=0, y=0, height=20, width=370)
TransformText.place(x=700, y=0, height=20, width=190)
MotivatorText.place(x=450, y=0, height=20, width=190)

loadData()

if music:
    # bgMusic = 'epic'
    # bgMusic = 'slowmotion'
    # bgMusic = 'birthofahero'
    mixer.music.load(resource_path("sounds/bensound-" + bgMusic + ".mp3"))
    mixer.music.play(-1, 0.0)

if name != "":
    r_key = random.choice(list(voc.keys()))
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "Bot: " + r_key + "\n\n")
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

level = round(score / 10)
lastlevel = level

off_image = PhotoImage(file=resource_path("pictures/off.png"))
on_image = PhotoImage(file=resource_path("pictures/on.png"))

while True:
    if sound:
        sendSound = mixer.Sound(resource_path("sounds/" + random.choice(sendSounds)))
        uffSound = mixer.Sound(resource_path("sounds/" + random.choice(uffSounds)))

    base.update()
    lastlevel = level
    level = round(score / 10)
    if level > lastlevel:
        if sound:
            mixer.Sound.play(levelUpSound)
        else:
            pass
    if level <= 1:
        level = 1
    leveltxt = text = "Level " + str(level)
    levelText.config(text=leveltxt)
    if level < 10:
        bildLabel.config(image=eval('bild1' + lastQuestion))
    elif 10 <= level < 75:
        bildLabel.config(image=eval('bild' + str(round(level / 10)) + lastQuestion))
    elif level > 74:
        bildLabel.config(image=eval('bild7' + lastQuestion))
    else:
        break
    saveData()
saveData()
raise SystemExit
