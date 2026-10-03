time = int(input("Enter the time in seconds: "))

timeSec = time % 60
timeMin = (time//60) % 60
timeH = ((time // 60) // 60) % 24

print('{:02}:{:02}:{:02}'.format(timeH, timeMin, timeH))
