# To fill up the program log "proglog.txt"

import datetime as dt

# The following function is used to generate a report for the program log.

def generatereport(action):
    curtime = dt.datetime.now()
    actime = curtime.strftime("%m/%d, %H:%M:%S")
    return "\n{t} | {a}".format(t=actime, a=action)

# The following function is used to write a report to the program log.

def writereport(action, out):
    report = generatereport(action)
    with open(out, 'a') as file:
        file.write(report)
        file.close()

# The following function is used to write an error to the program log.

def writeerror(action, out):
    actionx = generatereport(action + " | Error")
    writereport(actionx, out)

# The following function is used to clean the program log.

def cleanreport(out):
    with open(out, "w") as file:
        file.write("")
        file.close()