'''
Author: Vitorio Bimbato-Siqueira (001224534)
Date:21/02/2023
Description: module dedicated to getting and formatting test data to be used as test
             cases
'''


from src.classes import testCase


def get_data():
    try:  # Try statement to ensure the file is valid
        f = open(f"data/generatedFile.txt")  # will open the file from the data directory in the default read state
        filedata = f.read()  # reads the file
        f.close()  # closes the file to prevent any memory leaks or interference
        return filedata  # returns the raw data
    except Exception as e:  # except statement to catch any errors while reading or searching for the file
        print(f"This file was not found, or is not readable.\nPlease try again.\n{'-'*8}\n{e}")


def split_file(data):
    first_split = data.split("\n")
    split_data = []
    for i in first_split:
        new = i.split(',')
        for x in new:
            split_data.append(x)
    return split_data


def format_data(data):
    split_data = split_file(data)
    new_group = []
    split_cases = []
    for i in split_data:
        new_group.append(i.strip())
        if len(new_group) == 6:
            #print(new_group)
            new_case = testCase.TestCase(new_group)
            #print(new_case.line)
            split_cases.append(new_case)
            new_group = []
    #print(split_cases)
    return split_cases



