from tkinter import *
from tkinter.ttk import *

# window to simulate the main dashboard
dashboard = Tk()
dashboard.title("Driver Dashboard")
dashboard.geometry("500x200")  # setting window size


class DriverDisplay:
    def __init__(self, speed, rpm, energy):
        """
        initializing data that will be displayed
        """

        self.speed = speed
        self.revs = rpm
        self.energy = energy


    def set_display(self):
        """
        creates labels for data values and displays them on the window
        """

        # creating labels
        mph = Label(dashboard, text=f"{self.speed} MPH", font=("Verdana", 30))
        rpm = Label(dashboard, text=f"{self.revs} RPM")
        energy_output = Label(dashboard, text=f"{self.energy} V")

        # position the data labels
        mph.place(x=185, y=70)
        rpm.place(x=10, y=10)
        energy_output.place(x=450, y=10)

        # bring up display with data
        dashboard.mainloop()
