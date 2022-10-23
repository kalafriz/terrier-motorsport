import dashboard

# example run, test methods
test_dash = dashboard.DriverDisplay(30, 3000, 700, 1)
test_dash.setSpeed(40)
test_dash.setGear(4)
test_dash.setRevs(5000)
test_dash.setEnergy(1000)

# values are finalized and displayed onto window to user
test_dash.set_display()
test_dash.display_on()
