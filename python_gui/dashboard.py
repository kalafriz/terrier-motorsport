from tkinter import *
from tkinter.ttk import *

# window to simulate the main dashboard
dashboard = Tk()
dashboard.title("Driver Dashboard")
dashboard.geometry("500x200")  # setting window size


class DriverDisplay:
    def __init__(self, speed, rpm, energy, gear):
        """
        initializing data that will be displayed
        """

        self.speed = speed
        self.revs = rpm
        self.energy = energy
        self.gear = gear


    def setSpeed(self, mph):
        """
        sets the mph to new input
        """
        self.speed = mph


    def setRevs(self, rpm):
        """
        sets the rpm to new input
        """
        self.revs = rpm


    def setEnergy(self, energy):
        """
        sets the energy output to new input
        """
        self.energy = energy


    def setGear(self, gear):
        """
        sets the gear to new input
        """
        self.gear = gear


    def set_display(self):
        """
        creates labels for data values and displays them on the window
        """

        # creating labels
        mph = Label(dashboard, text=f"{self.speed} MPH", font=("Verdana", 30))
        rpm = Label(dashboard, text=f"{self.revs} RPM")
        energy_output = Label(dashboard, text=f"{self.energy} V")
        gear = Label(dashboard, text=f"Gear: {self.gear}", font=("Verdana", 20))

        # position the data labels
        gear.place(x=205, y=10)
        mph.place(x=185, y=70)
        rpm.place(x=10, y=10)
        energy_output.place(x=450, y=10)


    def display_on(self):
        """
        Opens up the window
        """

        # bring up display with data
        dashboard.mainloop()
