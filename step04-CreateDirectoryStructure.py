#!/usr/bin/python

import os, sys

for i in range(70):
    for j in range(12):
        year=1955+i
        month=j+1
        YearMonth=str(year)+"-"+str(month).zfill(2)
        print(YearMonth)

        # Path to be created
        path = "./date_directories/"+YearMonth

        os.makedirs(path);
