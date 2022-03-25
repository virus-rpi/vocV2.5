from tkinter import *
import sys
import os


class Settings(Toplevel):
    def __init__(self, root, on_image, off_image, in_sound=False, in_music=False):
        Toplevel.__init__(self)
        self.input_sound = in_sound
        self.input_music = in_music

        self.on_image = on_image
        self.off_image = off_image

        self.exit = False

        self.withdraw()
        self.lift(root)

        self.saveButton = Button(
            self,
            text="Save",
            font=("Verdana",12),
            bg="lightblue",
            fg="white",
            command=self.closeWindow
        )

        # sound
        self.soundLable = Label(
            self,
            text="Sound: ",
            font=("Verdana", 24),
            bg='white',
            anchor=W
        )
        self.soundVar = BooleanVar()
        self.soundVar.set(self.input_sound)
        self.soundCheckbox = Checkbutton(
            self,
            indicatoron=False,
            font=("Verdana", 12),
            variable=self.soundVar,
            bg='white',
            activebackground='white',
            bd=0,
            anchor=E
        )

        # music
        self.musicLable = Label(
            self,
            text="Music: ",
            font=("Verdana", 24),
            bg='white',
            anchor=W
        )
        self.musicVar = BooleanVar()
        self.musicVar.set(self.input_music)
        self.musicCheckbox = Checkbutton(
            self,
            indicatoron=False,
            font=("Verdana", 12),
            variable=self.musicVar,
            bg='white',
            activebackground='white',
            bd=0,
            anchor=E
        )

    def main(self):
        self.title("Settings")
        self.geometry("400x200")
        self.iconbitmap(self.resource_path("9108.ico"))
        self.configure(background='white')

        self.soundLable.grid(row=0, column=0)
        self.soundCheckbox.grid(row=0, column=1)

        self.musicLable.grid(row=1, column=0)
        self.musicCheckbox.grid(row=1, column=1)

        self.saveButton.grid(row=3, column=1)

        while True:
            try:
                self.update()
                self.deiconify()
            except:
                break

            if self.soundVar.get():
                self.soundCheckbox["image"] = self.on_image
            else:
                self.soundCheckbox["image"] = self.off_image
            self.sound = self.soundVar.get()

            if self.musicVar.get():
                self.musicCheckbox["image"] = self.on_image
            else:
                self.musicCheckbox["image"] = self.off_image
            self.music = self.musicVar.get()

            if self.exit:
                self.destroy()
                return self.sound, self.music
    def closeWindow(self):
        self.exit = True


    def resource_path(self, relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


if __name__ == "__main__":
    print("Do not run this code directly")
