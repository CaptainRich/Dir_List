# Routine to list all of the files in a directory.
import os

# Set a global variable for the total file count.
global total_files, total_size
total_files = 0
total_size  = 0


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
    # path       - the starting path to scan
    # num_blanks - the number of spaces for the indentation of this directory level
    # file_IO    - set to TRUE in the caller, forcing text file output
    # o_file     - the file object (handle) to write to

    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():

                sub_path = path + '/' + entry.name                           # Build the path to the subdirectory
                file_size = 0
                num_files = 0

                # Loop over the files in the directory, accumulating their size and number
                for filename in os.listdir( sub_path ):
                    file_path = os.path.join( sub_path, filename )
                    if os.path.isfile( file_path ):      # Only count files, not subdirectories
                        num_files += 1
                        file_size += os.path.getsize( file_path )
                
                # Print or write the directory name with its information.
                name_length = num_blanks + len(entry.name)
                num_dash    = 60 - name_length

                output_string = \
                    (f"{' '*num_blanks}{entry.name} {'-'*num_dash}> {num_files:3} files,  {file_size:13,} bytes\n")
                
                if( file_IO ):
                    o_file.write( output_string )
                else:
                    print( output_string )

                # To summarize the scan at the end of processing.
                global total_files, total_size
                total_files = total_files + num_files
                total_size  = total_size + file_size                    

                # Scan this new subdirectory, increasing the indent for this level.
                scan_directory( sub_path, num_blanks+3, file_IO, o_file )    




#################################################################################################
# Function to return the total number of files scanned and the total size.
def report_sizes( ):
    return( total_size, total_files )
