import tkinter as tk
import webbrowser

window = tk.Tk()
window.resizable(False, False)

titleFrame = tk.Frame(master=window, height=100)
titleFrame.pack(fill=tk.X)
titleLabel = tk.Label(master=titleFrame, text="Online Class Manager", font='Helvetica 18 bold')
titleLabel.pack(fill=tk.X)

buttonsFrame = tk.Frame(master=window, height=300, bg='blue')
buttonsFrame.pack(fill=tk.X)


classNames = [
    "Sheikh Alimur Razi\nEEE-421 Microprocessor and Interfacing",
    "Unknown\nEEE-421 Microprocessor and Interfacing",
    "Dr. Nur Mohammad\nEEE-471 Switchgear and Protection",
    "Dr. Muhammad Quamruzzaman\nEEE-471 Switchgear and Protection",
    "E.M.K Ikball Ahamed\nEEE-473 Semiconductor Physics and Devices",
    "Dr. Nusrat Jahan\nEEE-473 Semiconductor Physics and Devices",
    "Mohammad Mahmudul Hasan Tareq\nEEE-491 High Voltage Engineering",
    "Fahim Mahmud\nEEE-491 High Voltage Engineering",
    "Naqib Sad Pathan\nEEE-495 Digital Signal Processing",
    "Dr. Muhammad Ahsan Ullah\nEEE-495 Digital Signal Processing"
]

links = [
    "www.google.com",
    "www.wikipedia.com",
    "www.youtube.com",
    "www.amazon.com",
    "www.cnn.com",
    "www.duckduckgo.com",
    "www.bing.com",
    "www.ctgmovies.com",
    "www.crazyctg.com",
    "www.yahoo.com"
]

buttons = []

def handleButtonClick(buttonIndex):
    print(links[buttonIndex])
    webbrowser.open(links[buttonIndex])

buttonIndex = 0
for i in range(5):
    for j in range(2):
        button = tk.Button(
            master = buttonsFrame,
            relief = tk.RAISED,
            borderwidth = 2,
            text = classNames[buttonIndex],
            font='Helvetica 12',
            width = 38,
            height = 2,
            bg = "black",
            fg = "white",
            command = lambda index=buttonIndex : handleButtonClick(index)
        )
        button.grid(row=i, column=j, padx=2, pady=2)
        buttons.append(button)
        buttonIndex += 1


window.mainloop()

