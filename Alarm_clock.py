from datetime import datetime
#from playsound import playsound

def alarm():
    (hour,min,sec,period) = current_time()
    print(f'The current time is {hour}:{min}:{sec} {period}')
    user_alarm = set_alarm()

    if check_alarm(user_alarm) == "OK":
        print(f'The alarm is set at {user_alarm}')
        while True: 
            (hour,min,sec,period) = current_time()
            if user_alarm[0:2] == hour:
                if user_alarm[3:5] == min:
                    if user_alarm[6:8] == sec:
                        if user_alarm[9:11] == period:
                            print("Alarm is ringing!!!")
                            break

def current_time():
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    return(current_hour,current_min,current_sec,current_period)

def set_alarm():
    while True:
        alarm = input('Enter the alarm time in the "HH:MM:SS AM/PM" format:\n')
        if len(alarm) != 11:
            print('The format that you chose in invalid')
        else:
            return(alarm)

def check_alarm(user_alarm):
    check = ''
    if int(user_alarm[0:2]) > 12:
        print('The entered hour is not valid, please enter a valid hour')
    elif int(user_alarm[3:5]) > 59:
        print('The entered minutes are not valid, please enter valid minutes')
    elif int(user_alarm[6:8]) > 59:
        print('The entered seconds are not valid, please enter valid seconds')
    elif user_alarm[9:11] == "AM" or user_alarm[9:11] == "PM":
        check = 'OK'
    else:
        print('The entered period is not valid, please enter a valid period')
        
    
    return(check)

if __name__ == '__main__':
    alarm()
