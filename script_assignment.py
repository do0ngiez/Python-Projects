import os
import time

directory = r'C:\Users\USER\Documents\GitHub\Python-Projects\scriptassignment'
#look directory
for filename in os.listdir(directory):
    #absolute fp
    file_path = os.path.join(directory, filename)

    if filename.endswith('.txt') and os.path.isfile(file_path):
        #get mod time
        modified_time = os.path.getmtime(file_path)
        readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modified_time))
        print(f"File: {filename}, Last Modified: {readable_time}")
