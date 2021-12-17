import re
import sys


payload = sys.argv[1]
intruder_result = sys.argv[2]

intruder_results = open(intruder_result,'r')
line = intruder_results.readlines()
for lines in line:
    if payload in lines:

        b = re.findall(payload+'(.+?)&',lines)[0]
        print(b)
        
