class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes 
        self.__seconds = seconds 

    def __str__(self):
        two_digits = 2
        hours_formmated = '0' + str( self.__hours ) if len(str( self.__hours )) < two_digits else self.__hours
        minutes_formmated = '0' + str( self.__minutes ) if len(str( self.__minutes )) < two_digits else self.__minutes
        seconds_formmated = '0' + str( self.__seconds ) if len(str( self.__seconds )) < two_digits else self.__seconds
        return f'{hours_formmated}:{minutes_formmated}:{seconds_formmated}'

    def next_second(self):
        if self.__seconds == 59: 
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0

    def prev_second(self):
        if self.__seconds == 0: 
            self.__seconds = 59 
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hours == 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
