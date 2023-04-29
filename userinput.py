import logger as l
import csvdatahandler as csv
import os

logfile = "proglog.txt"

# This function asks the user for input & uses repetitive error checking to get the name of the CSV file to import the data from.

def get_csv_filename():
    while True:
        filename = input("Please enter the name of the CSV file: ")
        if not filename.endswith('.csv'):
            l.writeerror("Invalid file format. Please enter a CSV file.", logfile)
            return None
        elif not os.path.exists(filename):
            l.writeerror("File not found. Please enter a valid file name.", logfile)
            return None
        else:
            l.writereport("CSV file {f} selected.".format(f=filename), logfile)
            return filename

logfile = "proglog.txt"

# This function asks the user for input & uses repetitive error checking to get the columns from the CSV file to include in the dataframe with exception handling built-in.

def get_columns(csvfile):
    frame = csv.importfromcsvsimple(csvfile, logfile)
    if frame.empty:
        l.writeerror("Empty dataframe received in get_columns() function", logfile)
        return []
    else:
        columns = frame.columns.tolist()
        print("Select the columns to include (enter the corresponding numbers, separated by commas): ")
        for i, column in enumerate(columns):
            print("{num}. {col}".format(num=i+1, col=column))
        while True:
            try:
                selected_columns = [int(x) for x in input("> ").strip().split(",")]
                selected_columns = [columns[i-1] for i in selected_columns]
                if not all(column in columns for column in selected_columns):
                    raise ValueError("One or more selected columns do not exist in the CSV file")
                l.writereport("Selected columns: {cols}".format(cols=selected_columns), logfile)
                print(selected_columns)
                return selected_columns
            except ValueError as e:
                l.writeerror("Error in selecting columns: {error}".format(error=e), logfile)
            except KeyError as e:
                l.writeerror("Error in selecting columns: {error}".format(error=e), logfile)

# This function asks the user for input & uses repetitive error checking to get the constraints from the CSV file to include in the dataframe with exception handling built-in.

def get_constraints(csvfile, columns=None):
    columnx = get_columns(csvfile) if columns is None else columns
    try:
        l.writereport(f"Data imported from {csvfile} with columns: {columnx}", logfile)
        constraints = input("Enter additional constraints (optional, separate with '|'): ")
        if len(constraints) > 0:
            constraints = [constraint.strip() for constraint in constraints.split("|")]
            l.writereport(f"Constraints: {constraints}", logfile)
        else :
            constraints = []
        return constraints
    except Exception as keyerror:
        l.writeerror(f"Error in selecting columns: {keyerror}", logfile)
        print("Could not retrieve a frame with the expected constraints.")
        return None

# This function asks the user for the starting & ending rows & then truncates the dataframe to the specified range of rows.

def get_start_stop():
    st = {
        "start": 0,
        "stop": 0
    }
    start = int(input("Enter the starting row: "))
    stop = int(input("Enter the ending row: "))
    st["start"] = start
    st["stop"] = stop
    l.writereport("Starting & stopping values input. Start: {start}, Stop: {stop}".format(start=start, stop=stop), logfile)
    return st

# This function asks the user for the name of the file to export the new dataframe to. It also checks if the file already exists.

def get_export_filename(frame):
    filename = ""
    while not filename.endswith('.csv'):
        filename = input("Please enter the name of the export file: ")
        if not filename.endswith('.csv'):
            l.writeerror(f"Could not create an export file {filename} because of bad file extension.", logfile)
        elif not os.path.exists(filename):
            l.writereport("Export file {f} selected.".format(f=filename), logfile)
            frame.to_csv(filename, index=False)
            return filename
        elif 'quit' in filename.lower():
            l.writeerror("Export file {f} already exists.".format(f=filename), logfile)
            break

# This function asks the user for the name of the file to delete from the current directory. It also checks if the file does not already exist.

def get_deletion_filename():
    filename = ""
    while not filename.endswith('.csv'):
        filename = input("Please enter the name of the export file: ")
        if not filename.endswith('.csv'):
            l.writeerror(f"Could not create an export file {filename} because of bad file extension.", logfile)
        elif os.path.exists(filename):
            l.writereport("Export file {f} selected.".format(f=filename), logfile)
            os.remove(filename)
            return filename
        elif 'quit' in filename.lower():
            l.writeerror("Export file {f} already exists.".format(f=filename), logfile)
            break

# This function hierarchically calls all other user input functions to return a final dataframe for further analysis. It also uses loops to ask the user which files they want to export their data to & which files they want to delete from the current directory. It also prints the final dataframe to the terminal.

def askforinput():
    csvfile = get_csv_filename()
    frame = csv.importfromcsvsimple(csvfile, logfile)
    columns = get_columns(csvfile)
    frame = csv.modifycolumns(frame, logfile, columns)
    ss = get_start_stop()
    frame = csv.modifyss(frame, logfile, ss["start"], ss["stop"])
    export = ""
    deletion = ""
    export = input("Export the file? (y/n): ")
    while export.lower() == 'y':
        get_export_filename(frame)
        export = input("Export another file? (y/n): ")
    deletion = input("Delete the original file? (y/n): ")
    while deletion.lower() == 'y':
        get_deletion_filename()
        deletion = input("Delete another file? (y/n): ")
    print(frame)
    return frame