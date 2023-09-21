# Directory_Scan performs a scan of a target directory, listing all subdirectories
# below, recursively.  The result of the scan is written to the text file 'dir_list.txt'.

import pathlib            # Module needed for file I/O
import dir_list           # Module with various directory/disk functions


###################################################################################################
# Main


# Prompt for the starting (top level) directory to scan.

print( "Specify the desired starting directory to scan,"  )
path = input( "(Use an absolute path name): " )

num_blanks = 2         # The initial indentation for the top level directory

dir_list.scan_directory( path, num_blanks )
