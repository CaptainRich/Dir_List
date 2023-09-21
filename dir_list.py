# Routine to list all of the files in a directory.
import os


###############################################################################################
# Function to list all of the files in a directory (the argument to the function).
def view_dir( path='.', sorted=False):
    names = os.listdir(path)   # Get a list of all files/directories in 'path'

    # Review/update the list so everything is lower case
    for index, name in enumerate( names ):
        names[index] = name.lower()

    if sorted:
        names.sort()               # Sort the list, in place

    # Display the list of files/directories.
    for name in names:
        print( name, '\n', end = ' ' )


#################################################################################################
# Function to scan for a list of directories, with subdirectories indented by level.
def scan_directory( path, num_blanks ):
    blanks = num_blanks
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                # Print the directory name, then scan it.
                print( ' '*blanks, entry.name )
                sub_path = path + '/' + entry.name    # Build the path to the subdirectory
                blanks = blanks + 4                   # Indent each level an additional 4 spaces
                scan_directory( sub_path, blanks )


#################################################################################################
