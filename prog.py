#!/usr/bin/env python
import os
import subprocess
import sys

command = "sudo perf trace -p 2977 2>&1 >/dev/null | awk '{print $5}' > trainingData.txt"
proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
result=proc.communicate()[0]
proc.terminate()