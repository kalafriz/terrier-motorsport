from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from PIL import ImageTk, Image

# window to simulate the main dashboard
dashboard = Tk()
dashboard.title("Driver Dashboard")
dashboard.geometry("500x300")  # setting window size


class DriverDisplay:
    #Define Image
    bg = PhotoImage(file="/Users/kevinwrenn/Desktop/retro-sunrise-with-sun-and-neon-city-view-vector-29598871.png")
    
    #Create a Canvas
    global canvas
    canvas = Canvas(dashboard, width=500, height = 200) 
    canvas.pack(fill="both", expand=True)
    
    #Set image in canvas
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    
    
    #Create a label 
    
    #canvas.create_text(400, 250, text = "Welcome!", font = ("Helvetica", 50), fill = "black")
    
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
        custom_font = Font(
            family = "pdark",
            slant = "italic",
            size = 30
        )
        #Create a Canvas
    
    
        # creating labels
        #mph = Label(dashboard, text=f"{self.speed} MPH", font=custom_font)
        mph = canvas.create_text(250, 150, text =f"{self.speed} MPH", font = ("Helvetica", 50), fill = "white")
        #rpm = Label(dashboard, text=f"{self.revs} RPM")
        rpm = canvas.create_text(70, 30, text =f"{self.revs} RPM", font = ("Helvetica", 25), fill = "white")
       #energy_output = Label(dashboard, text=f"{self.energy} V")
        energy = canvas.create_text(350, 63, text =f"{self.energy} V", font = ("Helvetica", 25), fill = "white")
        #gear = Label(dashboard, text=f"Gear: {self.gear}", font=("pdark.tff", 20))
        gear = canvas.create_text(440, 32, text =f" Gear: {self.gear}", font = ("Helvetica", 25), fill = "white")

        # position the data labels
        #gear.place(x=205, y=10)
        #mph.place(x=185, y=70)
        #rpm.place(x=10, y=10)
       # energy_output.place(x=450, y=10)
        # canvas.move(mph, -100, -100)
        canvas.move(energy, -100, -35)
    def display_on(self):
        """
        Opens up the window
        """

        # bring up display with data
        dashboard.mainloop()
