import sys
import os
import re

class VapeTest():

    def __init__(self):
        self.foldername_array = []
        self.current_path_array= []
        self.cli_handler_path_arguement()
        self.get_folder_name_with_characters()
        self.get_path_name()
        self.match_path_with_folder_name()
        self.get_path_length()
        self.get_extension_types()


    """
    gets the first argument with the python script.
    For this script to run, the first argument should be 
    a relative path to the folder you want the tests to run on.
    """
    def cli_handler_path_arguement(self):
        self.path_location = sys.argv[1]
        
    """
    checks if directories contains special characters,
    prints out the names of ones which do.
    """
    def test_containsCharacters(self, folder_name):
            current_directory = re.findall("[\/@%; ]", folder_name)
            if current_directory:
                self.foldername_array.append(folder_name)

    """
    loops through and gets all folder names
    """
    def get_folder_name_with_characters(self):
        for currentpath, folders, files in os.walk(self.path_location):
            for folder in folders:
                self.test_containsCharacters(folder)

    """
    loops through and gets all path names
    """
    def get_path_name(self):
        for currentpath, folders, files in os.walk(self.path_location):
            self.current_path_array.append(currentpath)

    
    """
    checks if folder name with characters that are not allowed are in the current directory to print it out for easy reading.
    """
    def match_path_with_folder_name(self):
        for current_path in self.current_path_array:
            for folder in self.foldername_array:
                if folder in current_path:
                    print(current_path)
        
    """
    checks the length of paths i believe the maximum character count is 180
    """
    def get_path_length(self):
        for currentpath, folders, files in os.walk(self.path_location):
            for file in files:
                fp = os.path.join(currentpath, file)
                if len(fp) >= 180:
                    print(len(fp), fp)

    """
    if there is a file type ending in docx it prints it out.
    """
    def get_extension_types(self):
        for currentpath, folders, files in os.walk(self.path_location):
            for file in files:
                if file.endswith('.docx'):
                    print(currentpath, file)
    
if __name__ == '__main__':
    VapeTest()