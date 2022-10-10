import datetime
import os
import time
import random
import webbrowser



# if video URL file does not exist create one
if not os.path.isfile("youtube_videos.txt"):
    print('Creating "youtube_videos.txt')

with open("youtube_videos.txt", "w") as alarm_file:
    alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")


def check_alarm_input(alarm_time):
    """
    Checks to see if the user has entered in a valid alarm time
    """

    if len(alarm_time) == 1: #[hour] format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True

    if len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True

    elif len(alarm_time) == 3: # [Hour:MInute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True


    else:
        return False


#Get user input for the alarm time
print("Set a time for the alarm")

while True:

    alarm_input = input(">>")

    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break

        else:
            raise ValueError
    except:
        ValueError

    print("Error: Enter time in HH:MM or HH:MM:SS format")


# convert alarm time to seconds
seconds_hms = [3600,60,1]

alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)],alarm_time)])

#get the current time ofday in seconds
now = datetime.datetime.now()

current_time_seconds = sum([a*b for a,b in zip(seconds_hms,[now.hour,now.minute,now.second])])

#calculate the number of seconds until alarm goes off
time_diff = alarm_seconds - current_time_seconds

# if time difference is negative set alarm for next day
if time_diff < 0:
    time_diff += 86400

#Display the amount of time until alarm goes off

print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff))

#sleep until the alarm goes off

time.sleep(time_diff)

print("Wake Up!")

# Load list of possible video URLs

with open("youtube_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()


# Open a random video from the list

webbrowser.open(random.choice(videos))