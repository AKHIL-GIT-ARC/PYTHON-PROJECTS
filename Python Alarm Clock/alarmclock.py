# Python alarm clock

import datetime
import time
import pygame

def set_timer(alarm_time):
    print(f"Timer is activated for '{alarm_time}'")
    sound_file = "mixkit-hip-hop-02-738.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP YOU IDIOT!! 🫨")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
            
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter alarm time ( HH:MM:SS ):")
    set_timer(alarm_time)

