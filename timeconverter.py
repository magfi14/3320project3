import datetime as dt
import logger as l

logfile = 'proglog.txt'

# This function computes the difference between two floating point numbers.

def computedifference(num1, num2):
    l.writereport(f"Calculated the difference between {num1} and {num2}.", logfile)
    return float(num1) - float(num2)

# This function computes the quotient or the ratio of two floating point numbers.

def computequotient(num1, num2):
    l.writereport(f"Calculated the quotient between {num1} and {num2}.", logfile)
    return float(num1) / float(num2)

# This function converts a time in the format HH:MM:SS to a datetime format.

def convert_time(time):
    l.writereport(f"Converted time {time} to a datetime format.", logfile)
    return dt.datetime.strptime(time, "%H:%M:%S")

# This function converts a time in the format HH:MM:SS to a minute format.

def converttominutes(time):
    actualtime = convert_time(time)
    try:
        l.writereport(f"Converted time {time} to a minute format.", logfile)
        return float(actualtime.strftime("%H")) * 60 + float(actualtime.strftime("%M")) + computequotient(actualtime.strftime("%S"), 60)
    except AttributeError as e:
        l.writeerror("Error in converting time: {error}".format(error=e), logfile)
        return None
    
# This function converts a time in the format HH:MM:SS to a hour format.

def converttohours(time):
    actualtime = convert_time(time)
    try:
        l.writereport(f"Converted time {time} to a hour format.", logfile)
        return float(actualtime.strftime("%H")) + computequotient(actualtime.strftime("%M"), 60) + computequotient(actualtime.strftime("%S"), 3600)
    except AttributeError as e:
        l.writeerror("Error in converting time: {error}".format(error=e), logfile)
        return None

# This function converts a time in the format HH:MM:SS to a second format.

def converttoseconds(time):
    actualtime = convert_time(time)
    try:
        l.writereport(f"Converted time {time} to a second format.", logfile)
        return float(actualtime.strftime("%H")) * 3600 + float(actualtime.strftime("%M")) * 60 + float(actualtime.strftime("%S"))
    except AttributeError as e:
        l.writeerror("Error in converting time: {error}".format(error=e), logfile)
        return None

# This function calculates the difference from one time to the other in seconds.

def calculatetimedifferenceinseconds(time1, time2):
    try:
        l.writereport(f"Calculated the time difference between {time1} and {time2}.", logfile)
        seconds1 = converttoseconds(time1)
        seconds2 = converttoseconds(time2)
        return abs(computedifference(seconds1, seconds2))
    except TypeError as e:
        l.writeerror("Error in calculating time difference: {error}".format(error=e), logfile)
        return None

# This function calculates the difference from one time to the other in minutes.

def calculatetimedifferenceinminutes(time1, time2):
    try:
        l.writereport(f"Calculated the time difference between {time1} and {time2}.", logfile)
        minutes1 = converttominutes(time1)
        minutes2 = converttominutes(time2)
        return abs(computedifference(minutes1, minutes2))
    except TypeError as e:
        l.writeerror("Error in calculating time difference: {error}".format(error=e), logfile)
        return None
    
# This function calculates the difference from one time to the other in hours.

def calculatetimedifferenceinhours(time1, time2):
    try:
        l.writereport(f"Calculated the time difference between {time1} and {time2}.", logfile)
        hours1 = converttohours(time1)
        hours2 = converttohours(time2)
        return abs(computedifference(hours1, hours2))
    except TypeError as e:
        l.writeerror("Error in calculating time difference: {error}".format(error=e), logfile)
        return None

# This function converts seconds to minutes.

def secondstominutes(seconds):
    l.writereport(f"Converted {seconds} seconds to minutes.", logfile)
    return seconds / 60

# This function converts seconds to hours.

def secondstohours(seconds):
    l.writereport(f"Converted {seconds} seconds to hours.", logfile)
    return seconds / 3600

# This function converts minutes to seconds.

def minutestoseconds(minutes):
    l.writereport(f"Converted {minutes} minutes to seconds.", logfile)
    return minutes * 60

# This function converts minutes to hours.

def minutestohours(minutes):
    l.writereport(f"Converted {minutes} minutes to hours.", logfile)
    return minutes / 60

# This function converts hours to minutes.

def hourstoseconds(hours):
    l.writereport(f"Converted {hours} hours to seconds.", logfile)
    return hours * 3600

# This function converts hours to seconds.

def hourstominutes(hours):
    l.writereport(f"Converted {hours} hours to minutes.", logfile)
    return hours * 60