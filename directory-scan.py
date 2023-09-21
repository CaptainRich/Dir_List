# Directory_Scan performs a scan of a target directory, listing all subdirectories
# below, recursively.  The result of the scan is written to the text file 'dir_list.txt'.

import pathlib            # Module needed for file I/O
import dir_list           # Module with various directory/disk functions


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

    # Setup the file title
    title = 'Directory scan of: ' + str( out_path ) + '\n'
    o_file.write( title )

    # Recursively scan all of the directories below the specified path.
    dir_list.scan_directory( path, num_blanks, file_IO, o_file )


