class WeekDayError(Exception):
    pass
	

class Weeker:
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # number_weekdays = len(Weeker.weekdays) # Can't be done since Weeker doesn't seem to be defined yet
    number_weekdays = len(weekdays)
    
    def __init__(self, day):
        if not day in Weeker.weekdays:
            raise WeekDayError
        self.__weekday = day

    def __str__(self):
        return self.__weekday

    def add_days(self, n):
        weekday_index = n % Weeker.number_weekdays
        self.__weekday = Weeker.weekdays[weekday_index]

    def subtract_days(self, n):
        weekday_index = n % Weeker.number_weekdays
        self.__weekday = Weeker.weekdays[weekday_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
