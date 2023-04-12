from anti_afk import AntiAFK
from time import sleep

# Change this values to change the period of AFK test
minutes_to_test = 1 # 5 minutes to test AFK

anti_afk = AntiAFK()
time = 0
time_limit = int(2 * minutes_to_test)
time_limit = 1 if time_limit <= 0 else time_limit

while True:
    anti_afk.get_current_position()
    time += 1

    if time >= time_limit:
        print(anti_afk.check_afk(time_limit=time_limit))
        time = 0

    sleep(30)
