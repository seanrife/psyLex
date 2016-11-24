
from psyLex.readDict import *
from psyLex.wordCount import *
import sys
import os

# NOTE: this is VERY alpha. You will almost certainly need to tweak things to make it do what you really want. Read the source code and tread lightly.

# It goes like this: accepts two command line arguments: (1) directory with files to analyze, and (2) the path to the dictionary file we should use.
inValue = sys.argv[1]
inDict = sys.argv[2]

outLine = "file"

dictIn = readDict(inDict)

for cat in dictIn[0]:
	outLine = outLine + "," + dictIn[0][cat][0]

with open("out.csv", "a") as outCSV:
	outCSV.write(outLine + "\n")


for workingFile in os.listdir(inValue):

	outLine = workingFile
	with open (inValue + "\\" + workingFile, "r") as myfile:
		count = 0
		inData=myfile.read().replace('\n', ' ')

		# Run the wordCount function using the specified parameters.
		out = wordCount(inData, dictIn)

		for key, value in out[0].items():
			outLine = outLine + "," + str(value)
		with open("out.csv", "a") as outCSV:
			outCSV.write(outLine + "\n")

		