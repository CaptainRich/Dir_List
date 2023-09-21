# Directory_Scan performs a scan of a target directory, listing all subdirectories
# below, recursively.  The result of the scan is written to the text file 'dir_list.txt'.
# by: Richard Ay, September 2023

import pathlib            # Module needed for file I/O
import dir_list           # Module with various directory/disk functions
import datetime           # Used to time-stamp the output file


###################################################################################################
# Function to generate the output file title block.
def file_title( o_file ):
    title = '\n' + 'Directory scan of: ' + str( out_path ) + '\n'
    o_file.write( title )
    date = datetime.datetime.now()
    title = 'Scan created on ' + date.strftime("%A") + ' ' + date.strftime("%x") + '\n'
    o_file.write( title )
    title = 'by: Richard Ay, September 2023' + '\n\n'
    o_file.write( title )

###################################################################################################
# Main


# Prompt for the starting (top level) directory to scan.

outfile = input( "Specify the output file name: " )
print( "Specify the desired starting directory to scan,"  )
path = input( "(Use an absolute path name): " )

num_blanks = 2         # The initial indentation for the top level directory
file_IO    = True      # Output is sent to a text file

# Build the output file path and open it.
out_path = pathlib.Path( path + '/' + outfile )
out_path.touch() 

# When the 'with' block ends, the file is close automatically
with out_path.open( mode='w', encoding='utf-8' ) as o_file:

    # Setup the file title.  See https://www.w3schools.com/python/python_datetime.asp
    # for details on date/time formats.
    file_title( o_file )

    # Recursively scan all of the directories below the specified path.
    dir_list.scan_directory( path, num_blanks, file_IO, o_file )


