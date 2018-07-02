"""
How this works:
Pass in the file path into undo_sv(), and it should create a new difficulty
"""


import os

def is_inheritable(timing_point):
    parsed_data = timing_point.split(',')
    #technically redundant code, because one automatically implies the other
    milli_per_beat = parsed_data[1]
    inherited = parsed_data[6]
    if int(inherited):
        return True
    else:
        return False
    
def undo_sv(file_path):
    original_file = open(file_path, 'r')
    
    #Formatting New Filename
    file_name, file_extension = os.path.splitext(file_path)
    new_file = file_name + "[No SV]" + file_extension

    #Opening New and Old File
    
    new_file = open(new_file, 'w')    
    
    in_timing_points = False
    #Get to the timing_points section
    #import pdb; pdb.set_trace()
    while(not in_timing_points):
        line = original_file.readline()
        if "Version:" in line:
            new_file.write("Version:No SV\n")
        else:
            new_file.write(line)
        if("[TimingPoints]" in line):
            print("Found timing points")
            in_timing_points = True
        
    #Filter out only inheritable time section
    print("Filtering out time section")
    while(True):
        line = original_file.readline()
        if(line == '\n'):
            break
        if(is_inheritable(line)):
            new_file.write(line)
        
    for line in original_file.readlines():
        new_file.write(line)
        
    original_file.close()
    new_file.close()

