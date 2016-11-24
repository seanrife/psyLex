
from psyLex.readDict import *
from psyLex.wordCount import *
import sys

# It goes like this: accepts three command line arguments: (1) mode - see below - (2) text to analyze (file vs. raw text), and (3) the path to the dictionary file we should use.
inMode = sys.argv[1]
inValue = sys.argv[2]
inDict = sys.argv[3]

dictIn = readDict(inDict)

# Currently supports two modes: basic text (entered as a command-line argument) and file-based (will read a whole frakin' file).
# If basic text mode, just assign the input value the value of the second command line argument.
if inMode == "0":
    inData = inValue
# If file mode, read the file into a string.
elif inMode == "1":
    with open (inValue, "r") as myfile:
        inData=myfile.read().replace('\n', ' ')

# Run the wordCount function using the specified parameters.
out = wordCount(inData, dictIn)

#print(out[0].items())

for k, v in out[0].items():
	print(k + ": " + str(v))
