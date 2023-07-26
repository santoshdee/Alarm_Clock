from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from datetime import datetime
from pygame import mixer
from time import sleep
from threading import Thread

# #37474F
# colors
bg_color = '#ffffff'
co1 = "#566FC6"  # blue
co2 = "#000000"  # black


# Creating a window
win = Tk()
win.title("Alarm Clock")
win.geometry("350x150")
# win.configure(bg=bg_color)

# Frames
# Frame line
frame_line = Frame(win, width=400, height=5)
frame_line.grid(row=0, column=0)

# Frame body
frame_body = Frame(win, width=400, height=290)
frame_body.grid(row=1, column=0)

# load the image
img = Image.open("icon.png")
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, image=img)
app_image.place(x=10, y=10)

name = Label(frame_body, text="Alarm", font=('20'))
name.place(x=125, y=10)

# Hours
hour = Label(frame_body, text="Hour", font=('Ivy 10 bold'))
hour.place(x=128, y=40)

c_hour = Combobox(frame_body, width=2, font=('arial 15'))
# insert values in the combobox
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)  # current value in the box will be zero
c_hour.place(x=130, y=58)

# Minutes
minute = Label(frame_body, text="Min", font=('Ivy 10 bold'))
minute.place(x=178, y=40)

c_minutes = Combobox(frame_body, width=2, font=('arial 15'))
# insert values in the combobox
c_minutes['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                       "16", "17", "18", "19", "20", "21", "22", "23","24", "25", "26", "27", "28", "29", "30",
                       "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46",
                       "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minutes.current(0)  # current value in the box will be zero
c_minutes.place(x=180, y=58)

# AM/PM
period = Label(frame_body, text="Period", font=('Ivy 10 bold'))
period.place(x=228, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=230, y=58)

# Alarm activate and Deactivate buttons


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print("Deactivated alarm: ", selected.get())
    mixer.music.stop()


selected = IntVar()

activate = Radiobutton(frame_body, value=1, text="Activate", command=activate_alarm, variable=selected)
activate.place(x=125, y=95)


def sound_alarm():
    mixer.music.load('alarm.mp3')  # loads the music
    mixer.music.play()             # plays the music
    # selected.set(0)

    deactivate = Radiobutton(frame_body, value=2, text="Deactivate", command=deactivate_alarm, variable=selected)
    deactivate.place(x=215, y=95)


def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_minutes.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        # print("Time to take break")
                        sound_alarm()
        sleep(28)    # sleep is from time module


mixer.init()
# alarm()

win.mainloop()


