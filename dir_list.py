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
def scan_directory( path, num_blanks, file_IO, o_file ):

    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                
                # Print or write the directory name, then scan it.
                output_string = " "*num_blanks + entry.name + '\n'
                if( file_IO ):
                    o_file.write( output_string )
                else:
                    print( output_string )

                sub_path = path + '/' + entry.name                           # Build the path to the subdirectory
                scan_directory( sub_path, num_blanks+3, file_IO, o_file )    # Increase the indent level for this subdirectory



#################################################################################################
