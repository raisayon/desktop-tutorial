#pip install ocr

import easyocr
import json
import re
import pandas as pd
import csv, sys

reader = easyocr.Reader(['en','ch_tra'])

results = reader.readtext('dailydata/wang/f01111881.png')

path = '/Users/sayonrai/Documents/GitHub/desktop-tutorial/dailyinput.csv'
with open(path, 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(results)