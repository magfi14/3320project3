import pandas as pd
import logger as log
import os

outfilex = "proglog.txt"

# This function imports a CSV file and returns a data frame.

def importfromcsvsimple(file, outfile):
    frame = pd.read_csv(file)
    log.writereport("Data frame created with the following attributes: {attributes}".format(attributes=frame.columns.tolist()), outfile)
    return frame

# This function modifies a data frame by selecting the columns specified in the columns parameter.

def modifycolumns(frame, outfile, columns = []):
    log.writereport("Data frame modified with the following attributes: {attributes}".format(attributes=columns), outfile)
    return frame[columns]

# This function modifies a data frame by selecting the rows that satisfy the constraints specified in the constraints parameter.

def modifyconstraints(frame, outfile, constraints):
    log.writereport("Data frame modified with the following constraints: {constraints}".format(constraints=str(constraints)), outfile)
    try:
        return frame[constraints]
    except KeyError as keyerror:
        log.writeerror("Error in selecting columns: {error}".format(error=keyerror), outfile)
        print(f"Could not retrieve a frame with the expected constraints: {constraints}.")
        return frame

# This function modifies a data frame by selecting the rows from start to stop.

def modifyss(frame, outfile, start=0, stop=0):
    startx = start
    stopx = len(frame) if stop == 0 or stop > len(frame) else stop + 1
    log.writereport("Data frame modified from row {row1} to {row2}".format(row1=startx, row2=stop), outfile)
    return frame.iloc[startx:stopx]

# This function modifies a data frame by selecting the columns specified in the columns parameter, selecting the rows that satisfy the constraints specified in the constraints parameter, and selecting the rows from start to stop.

def modifyframe(frame, outfile, columns = [], constraints=None, start=0, stop=0):
    frame = modifycolumns(frame, outfile, columns)
    frame = modifyconstraints(frame, outfile, constraints)
    frame = modifyss(frame, outfile, start, stop)
    return frame

# This function imports a CSV file and returns a data frame. It also modifies the data frame by selecting the columns specified in the columns parameter, selecting the rows that satisfy the constraints specified in the constraints parameter, and selecting the rows from start to stop.

def importfromcsv(file, outfile, columns=[], constraints=None, start=0, stop=0):
    frame = importfromcsvsimple(file, outfile)
    frame = modifyframe(frame, outfile, columns, constraints, start, stop)
    return frame

# This function imports a CSV file and returns a data frame. It also modifies the data frame by selecting the columns specified in the columns parameter, selecting the rows that satisfy the constraints specified in the constraints parameter, and selecting the rows from start to stop. It also exports the data frame to a CSV file.

def getcolumns(frame):
    return frame.columns.tolist()

# This function returns the columns of a data frame as a list, truncating the range only to the columns which meet specific conditions.

def conditionaltruncate(frame, outfile, conditions):
    framex = frame[conditions]
    log.writereport("Data frame truncated successfully.", outfile)
    return framex

# This function exports a data frame to a CSV file.

def exporttocsv(file, outfile, frame):
    frame.to_csv(file, index=False)
    log.writereport("Frame exported to {f}, with {r} rows".format(f=file, r=len(frame)), outfile)

# This function deletes a CSV file which already exists in the directory.

def deletecsv(file, outfile):
    try:
        os.remove(file)
        log.writereport("CSV file {f} successfully deleted.".format(f=file), outfile)
    except Exception:
        print("File {f} could not be deleted because it doesn't exist".format(f=file))
        log.writeerror("CSV file {f} could not be deleted as it does not exist in the current directory".format(f=file), outfile)