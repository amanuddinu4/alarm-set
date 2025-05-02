from datetime import datetime
from pygame import mixer

# Initialize the mixer for playing audio
mixer.init()

# Prompt the user to set the alarm time
alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("Setting up alarm...")

# Infinite loop to check the current time against the alarm time
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    # Compare current time with alarm time
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")

                    # Play the alarm sound
                    mixer.music.load("audio.mp3")
                    mixer.music.play()

                    # Wait for the user to stop the alarm
                    input("Press Enter to stop the alarm...")
                    mixer.music.stop()
                    break
