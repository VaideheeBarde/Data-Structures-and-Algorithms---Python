#Method 1 (without exception handling)

import csv

def get_col_sum1(filename, col):
    #May raise IOError
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)
    running_sum = 0
    for row in csv_reader:
        value = row[col]
        running_sum += int(value)
    csv_file.close()
    print('Sum = ' + str(running_sum))

get_col_sum1('/Users/vaidehee_barde/Documents/Python/pract/FL_insurance_sample.csv', 1)

#Method 2 (with exception raised in the try block propagated to finally)

import json

def get_value(filename, key):
    handle = open(filename)
    try:
        file_contents = handle.read()
        js_text = json.loads(file_contents)
        return js_text[key]

    finally:
        #Prevent resource leak if there is an error parsing file content
        handle.close()

get_value('/Users/vaidehee_barde/Documents/Python/pract/FL_insurance_sample.csv', 1)

#Method 3 (the code below shows basic try/except usage. Does not have 'finally')
#The next method has duplicated code with 'finally' that is used to avoid resource leak

import json

def get_value2(filename, key):
    handle = open(filename)
    try:
        file_contents = handle.read()
        js_text = json.loads(file_contents)
        handle.close()
        return (True, js_text[key])
    except ValueError:
        handle.close()
        return (False, )

#Method 4 (the code below uses finally)
def get_value3(filename, key):
    handle = open(filename)
    try:
        file_contents = handle.read()
        js_text = json.loads(file_contents)
        return (True, js_text[key])
    except ValueError:
        return (False, )
    finally:
        handle.close()

#Method 5 (uses try/except/else/finally blocks. Uses 'raise' to create/propagate exceptions upwards)
class ColSumCsvParseException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.line_number = args[1]

def get_col_sum(filename, col):
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)
    running_sum = line_number = 0

    try:
        for row in csv_reader:
            if col >= len(row):
                raise(IndexError('Not enough entries in row' + str(row)))
            value = row[col]
            #We will skip rows for which the corresponding columns cannot be parsed
            #to an int, logging the fact
            try:
                running_sum += int(value)
            except ValueError:
                print('Cannot convert' + value + 'to int, ignoring')
            line_number += 1
    except csv.Error:
        #Programs should raise exceptions appropriate to their level of abstraction
        #So we propagate the csv.Error upwards as a ColSumCsvParseException
        print('In csv.Error handler')
        raise ColSumCsvParseException('Error processing csv', line_number)
    else:
        print('Sum = ' + str(running_sum))
    finally:
        #Ensure there is no resource leak
        csv_file.close()
        return running_sum