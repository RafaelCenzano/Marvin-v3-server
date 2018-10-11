# Imports
from time import sleep as wait # import sleep as wait for timer
from marvin.essentials import speak # speak function
from word2number import w2n


##############################
# File containing Timer code #
##############################


class TimerService():
    def __init__(self, time_for, speak_type):
        self.speak_type = speak_type
        self.time_for = time_for
        self.bob = 1
        try:
            if time_for == '':
                raise Exception
        except Exception:
            self.bob = 0

    def timerLogic(self):
        time_for_timer = self.time_for.split(" ")[0]
        if time_for_timer.lower() == 'zero' or time_for_timer == '0':
            self.bob = 0
            speak('You can\'t have a timer for 0 time')
        if self.bob >= 1:
            time_unit = marvin.essentials.splitJoin(self.time_for, 1)
            if time_unit == '':
                time_unit = 'minutes'
            try:
                bob = float(time_for_timer)
                self.time_for_timer = float(time_for_timer)
            except ValueError:
                self.time_for_timer = float(w2n.word_to_num(str(time_for_timer)))

            if 'min' in time_unit:
                abs_time = abs(float(self.time_for_timer))
                seconds_in_minutes = abs_time * 60
                self.timer(seconds_in_minutes)

            elif 'sec' in time_unit:
                abs_time = abs(float(self.time_for_timer))
                if abs_time >= 5.0:
                    self.timer(float(abs_time))
                else:
                    speak('Any timer less than 5 seconds is to small count thousands', self.speak_type)

            elif 'hr' in time_unit:
                abs_time = abs(float(self.time_for_timer))
                if abs_time <= 3:
                    seconds_in_hour = abs_time * 3600
                    self.timer(seconds_in_hour)
                else:
                    speak('Timer does not support reminders over 3 hours use a calander reminder for long reminders', self.speak_type)

            elif 'day' in time_unit:
                speak('Timer does not support days use a calander reminder for long reminders', self.speak_type)
            else:
                speak('I couldn\'t find the time unit you wanted to use', self.speak_type)
        else:
            speak('You need to input a number for the timer', self.speak_type)

    def timer(self, delay):
        print('Timer Started')
        time.sleep(float(delay))
        speak('Timer Done!', self.speak_type)