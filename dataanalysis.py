import csvdatahandler as csv
import logger as log
import userinput as ui
import timeconverter as tc

logfile = "proglog.txt"

# This function is used to get the data from the CSV file via the user input.

def getdata():
    return ui.askforinput()

# This function is used to calculate the efficiency of each route by computing the ratio of the time difference between the arrival and departure times and the distance traveled. The efficiency is then added as a new column to the dataframe. However, I could not get this code working properly in the required time.

def calculateefficiency(frame, time1x, time2x, distance):
    time1 = [tc.converttominutes(f) for f in frame[time1x]]
    time2 = [tc.converttominutes(f) for f in frame[time2x]]
    log.writereport(f"Calculated the time difference between {time1x} and {time2x}.", logfile)
    distancez = frame[distance]
    efficiency = []
    for i in range(len(time1)):
        time_diff = tc.calculatetimedifferenceinminutes(time1[i], time2[i])
        if time_diff is None or distancez[i] is None or distancez[i] == 0:
            efficiency.append(None)
        else:
            efficiency.append(time_diff / distancez[i])
    frame['efficiency'] = efficiency
    log.writereport(f"Calculated the efficiency by adding an efficiency column.", logfile)
    print(frame)
    csv.exporttocsv('newdata.csv', logfile, frame)
    return frame

# This is the function call to calculate the efficiency & thus run the entire program.

calculateefficiency(getdata(), 'arrival_time', 'departure_time', 'shape_dist_traveled') 