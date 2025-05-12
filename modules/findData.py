import os, sys

def findData(childDir:str):
    cwd = os.getcwd()
    parentDir = os.path.join(cwd, 'data')
    targetDir = os.path.join(parentDir, childDir)

    if os.path.isdir(targetDir):
        print(f"Found folder to analyze : {targetDir}")

        filePaths = []
        for fileName in os.listdir(targetDir):
            if fileName.endswith('.dat'):
                filePath = os.path.join(targetDir, fileName)
                filePaths.append(filePath)

        print(f"{len(filePaths)} files are found")
    else:
        print("[Error] Cannot find folder 'data'")
        print("        Check your input folder path and rerun!")
        sys.exit(0)

    return sorted(filePaths)