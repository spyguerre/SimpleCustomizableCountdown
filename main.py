import tkinter as tk
from tkinter import ttk
import datetime


def read_data(i):
    if i == 0:
        full_time = open("data.txt", "r").readlines()[0].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 1:
        full_time = open("data.txt", "r").readlines()[1].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 2:
        full_time = open("data.txt", "r").readlines()[2].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 3:
        return list(eval(open("data.txt", "r").readlines()[3].split("=")[1]))
    elif i == 4:
        return list(eval(open("data.txt", "r").readlines()[4].split("=")[1]))
    elif i == 5:
        return float(eval(open("data.txt", "r").readlines()[5].split("=")[1]))
    elif i == 6:
        return list(eval(open("data.txt", "r").readlines()[6].split("=")[1]))
    elif i == 7:
        return eval(open("data.txt", "r").readlines()[7].split("=")[1])
    elif i == 8:
        return eval(open("data.txt", "r").readlines()[8].split("=")[1])


def write_data(data):
    string = ""
    string += "initial_time=" + str(datetime.timedelta(seconds=data[0])) + "\n"
    string += "current_time=" + str(datetime.timedelta(seconds=data[1])) + "\n"
    string += "current_time_played=" + str(datetime.timedelta(seconds=data[2])) + "\n"
    string += "runs=" + str(data[3]) + "\n"
    string += "initial_time_decrease=" + str(data[4]) + "\n"
    string += "decrease_geometric_reason=" + str(data[5]) + "\n"
    string += "CPnames=" + str(data[6]) + "\n"
    string += "countdownTitleText='" + str(data[7]) + "'\n"
    string += "chronoTitleText='" + str(data[8]) + "'\n"

    open("data.txt", "w").write(string)


def updateBounties():
    time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]
    for i, bountyLabel in enumerate(bountyLabels):
        bountyLabel["text"] = str(time_decrease[i])


def updateCountdown():
    countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))


def updateChrono():
    chrono["text"] = str(datetime.timedelta(seconds=time_played))


def updateRuns():
    runsLabel["text"] = f"Today's runs so far: {CPnames[0]}:{runs[0]} // {CPnames[1]}:{runs[1]} // {CPnames[2]}:{runs[2]} // {CPnames[3]}:{runs[3]} // {CPnames[4]}:{runs[4]}"


def updateCountdownTitleText():
    titleLabels[0]["text"] = countdownTitleText


def updateChronoTitleText():
    titleLabels[1]["text"] = chronoTitleText


def pause():
    global paused
    paused = not paused
    pauseButton["text"] = "Pause" if not paused else "Resume"


def main():
    global time_left, time_played, runs, initial_time_decrease

    canvas = tk.Canvas(width=10000, height=10000, bg="#000000")
    canvas.place(x=-2, y=-2)

    appTitle = tk.Label(window, fg="#ffffff", text="A Simple and Customizable Countdown", font=("Courier", 25, "bold underline"), bg="#000000")
    appTitle.pack()

    appSubtitle = tk.Label(window, fg="#ffffff", text="I made for my stream because no-one else did it :p", font=("Courier", 10), bg="#000000")
    appSubtitle.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    countdownTitle = tk.Label(window, fg="#ffffff", text=countdownTitleText, font=("Courier", 15, "bold"), bg="#000000")
    countdownTitle.pack()

    countdown = tk.Label(window, fg="#ffffff", text=str(datetime.timedelta(seconds=time_left)), font=("Courier", 18, "bold"), bg="#000000")
    countdown.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    chronoTitle = tk.Label(window, fg="#ffffff", text=chronoTitleText, font=("Courier", 15, "bold"), bg="#000000")
    chronoTitle.pack()

    chrono = tk.Label(window, fg="#ffffff", text=str(datetime.timedelta(seconds=time_played)), font=("Courier", 18, "bold"), bg="#000000")
    chrono.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    buttons = tk.Frame(bg="#000000")
    buttons.pack()

    bounties = tk.Frame(bg="#000000")
    bounties.pack()

    def EH():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[0] * (decrease_geometric_reason**runs[0])))
        runs[0] += 1

        updateCountdown()
        updateRuns()
        updateBounties()

    EHbutton = ttk.Button(window, text=f"{CPnames[0]}", width=20, command=EH)
    EHbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    EHbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[0]), font=("Courier", 12, "bold"), bg="#000000", width=13)
    EHbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    def DT():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[1] * (decrease_geometric_reason**runs[1])))
        runs[1] += 1
        updateCountdown()
        updateRuns()
        updateBounties()

    DTbutton = ttk.Button(window, text=f"{CPnames[1]}", width=20, command=DT)
    DTbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    DTbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[1]), font=("Courier", 12, "bold"), bg="#000000", width=13)
    DTbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    def ST():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[2] * (decrease_geometric_reason**runs[2])))
        runs[2] += 1
        updateCountdown()
        updateRuns()
        updateBounties()

    STbutton = ttk.Button(window, text=f"{CPnames[2]}", width=20, command=ST)
    STbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    STbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[2]), font=("Courier", 12, "bold"), bg="#000000", width=13)
    STbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    def RC():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[3] * (decrease_geometric_reason**runs[3])))
        runs[3] += 1
        updateCountdown()
        updateRuns()
        updateBounties()

    RCbutton = ttk.Button(window, text=f"{CPnames[3]}", width=20, command=RC)
    RCbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    RCbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[3]), font=("Courier", 12, "bold"), bg="#000000", width=13)
    RCbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    def Golden():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[4] * (decrease_geometric_reason**runs[4])))
        runs[4] += 1
        updateCountdown()
        updateRuns()
        updateBounties()

    Goldenbutton = ttk.Button(window, text=f"{CPnames[4]}", width=20, command=Golden)
    Goldenbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    Goldenbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[4]), font=("Courier", 12, "bold"), bg="#000000", width=13)
    Goldenbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    def reset():
        global time_left, runs, time_played
        time_played = 0
        time_left = initial_time
        runs = [0, 0, 0, 0, 0]
        updateCountdown()
        updateChrono()
        updateRuns()
        updateBounties()

    button = ttk.Button(window, text="Reset", width=20, command=reset)
    button.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    pauseButton = ttk.Button(window, text="Resume", width=20, command=pause)
    pauseButton.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    runsLabel = tk.Label(window, fg="#ffffff", text=f"Today's runs so far: {CPnames[0]}:{runs[0]} // {CPnames[1]}:{runs[1]} // {CPnames[2]}:{runs[2]} // {CPnames[3]}:{runs[3]} // {CPnames[4]}:{runs[4]}", font=("Courier", 18, "bold"), bg="#000000")
    runsLabel.pack()

    creditsLabel = tk.Label(window, fg="#ffffff", text="Fait à l'arrache par SpygR", font=("Courier", 10), bg="#000000")
    creditsLabel.pack(side=tk.BOTTOM, anchor="sw")

    titleLabels = [countdownTitle, chronoTitle]
    CPbuttons = [EHbutton, DTbutton, STbutton, RCbutton, Goldenbutton]
    bountyLabels = [EHbounty, DTbounty, STbounty, RCbounty, Goldenbounty]
    return countdown, chrono, pauseButton, titleLabels, runsLabel, CPbuttons, bountyLabels


# Create window
window = tk.Tk()

# Set window size & name
window.geometry("1000x642")
window.resizable(True, True)
window.title("SimpleCustomizableCountdown")

# Variables globales
initial_time = read_data(0)
time_left = read_data(1)
time_played = read_data(2)
runs = read_data(3)
initial_time_decrease = read_data(4)
decrease_geometric_reason = read_data(5)
CPnames = read_data(6)
countdownTitleText = read_data(7)
chronoTitleText = read_data(8)
paused = True
time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]

countdown, chrono, pauseButton, titleLabels, runsLabel, CPbuttons, bountyLabels = main()


def update():
    window.after(1000, update)
    global initial_time, time_left, time_played, runs, initial_time_decrease, decrease_geometric_reason, \
        CPnames, countdownTitleText, chronoTitleText, time_decrease

    # Update variables from data.txt
    initial_time = read_data(0)
    initial_time_decrease = read_data(4)
    decrease_geometric_reason = read_data(5)
    CPnames = read_data(6)
    countdownTitleText = read_data(7)
    chronoTitleText = read_data(8)

    # Update data.txt
    data = [initial_time, time_left, time_played, runs, initial_time_decrease, decrease_geometric_reason, CPnames, countdownTitleText, chronoTitleText]
    write_data(data)

    # Update times if not paused
    if not paused:
        time_left = max(0, time_left - 1)
        time_played += 1

    # Update visuals
    updateCountdown()
    updateChrono()
    updateRuns()
    updateCountdownTitleText()
    updateChronoTitleText()
    for i, button in enumerate(CPbuttons):
        button["text"] = CPnames[i]
    updateBounties()


window.after(0, update)  # begin updates
window.mainloop()
