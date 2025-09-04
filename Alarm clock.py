#Python Alarm Clock
import time
import datetime
import pygame
#pygame is for importing sounds
def set_alarm(alarm_time):
    print(f"Alarm set for{alarm_time}")
    sound_file="my_music.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm_time:
            print("WAKE UP!😊")
            pygame.mixer.init()
            #mixer is a module for loading and playing songs
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
           #we did this while loop to return a boolean,if our song is busy i.e it is playing then wait for 1 sec before stopping
            is_running=False
        time.sleep(1)

if __name__=="__main__":
    alarm_time=input("Enter the alarm time(HH:MM:SS):")
    set_alarm(alarm_time)

