""" Directory_Scan performs a scan of a target directory, listing all subdirectories
    below, recursively.  The result of the scan is written to the text file '<specified_by_User>'.
    by: Richard Ay, September/November 2023
"""

import pathlib            # Module needed for file I/O
import dir_list           # Module with various directory/disk functions
import datetime           # Used to time-stamp the output file
import easygui as gui     # For the data acquisition dialog box


###################################################################################################
# Function to generate the output file title block.
def file_title( o_file, path ):

    title = '\n' + 'Directory scan of: ' + str( out_path ) + '\n'
    o_file.write( title )

    date = datetime.datetime.now()
    title = 'Scan created on ' + date.strftime("%A") + ' ' + date.strftime("%x") + '\n'
    o_file.write( title )

    title = 'by: Richard Ay, Nov 2023 - Updated May 2024' + '\n\n'
    o_file.write( title )
    o_file.write( path+'\n' )

###################################################################################################
# Main




# Prompt for the starting (top level) directory to scan.

# These three lines work, but are replaced by the GUI dialog box
#outfile = input( "Specify the output file name: " )
#print( "Specify the desired starting directory to scan,"  )
#path    = input( "(Use an absolute path name): " )

# Setup the dialog boxes.

outfile = path = ""

path = gui.diropenbox(
    title   = "Select the target directory:"
)

outfile = gui.enterbox(
    msg     = "Enter the output file name:", 
    title   = "Output File Specification"
)

#print( "Specified pathname: ", path )
#print( "Output file is:     ", outfile )

# Verify the necessary information was defined.
if( path is None ) or ( outfile is None ):
    exit()

if( len(path) < 1 ) or ( len(outfile) < 1 ):
    exit()



num_blanks = 2         # The initial indentation for the top level directory
file_IO    = True      # Output is sent to a text file

# Build the output file path and open it.
out_path   = pathlib.Path( path + '/' + outfile )
out_path.touch()     # Create the file

# When the 'with' block ends, the file is close automatically
with out_path.open( mode='w', encoding='utf-8' ) as o_file:

    # Setup the file title.  See https://www.w3schools.com/python/python_datetime.asp
    # for details on date/time formats.
    file_title( o_file, path )

    # Recursively scan all of the directories below the specified path.
    dir_list.scan_directory( path, num_blanks, file_IO, o_file )

    # Summarize the number of files found
    output_string = \
        (f" Total Files Scanned: {total_files:,}, Total Size: {total_size:,} bytes\n")
    
    if( file_IO ):
        o_file.write( output_string )
    else:
        print( output_string )


