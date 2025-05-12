def parseData(filePath):
    # open file with 'latin-1' encoding. this is important to open '.dat' file
    with open(filePath, 'r', encoding='latin-1') as file:
        lines = file.readlines()

    isDataStarted = False
    attachZ = [] # attach, Z axis data
    detachZ = [] # detach, Z axis data
    attachSignal = [] # attach, signal data
    detachSignal = [] # detach, signal data

    # read lines from top to bottom and catch lines after text "[Data]"
    for line in lines:
        line = line.strip() # remove whitespace

        if line == "[Data]":
            isDataStarted = True # mark isDataStarted as True
            continue

        if isDataStarted and line: # empty line ignored
            values = line.split("\t")
            if len(values) == 4: # store only if have 4 columns
                attachZ.append(float(values[0]))
                attachSignal.append(float(values[1]))
                detachZ.append(float(values[2]))
                detachSignal.append(float(values[3]))

    # reverse data if decreasing order
    if attachZ[0] < attachZ[1]:
        detachZ.reverse()
        detachSignal.reverse()
    else:
        attachZ.reverse()
        attachSignal.reverse()

    return [attachZ,attachSignal,detachZ,detachSignal]