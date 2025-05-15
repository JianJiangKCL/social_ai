#!/usr/bin/env python3
import os
import subprocess
import sys

def extract_7z_files(directory_path):
    """
    Extract 7-zip split archive files in the specified directory.
    Will extract using the first part of the archive.
    """
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory {directory_path} does not exist.")
        return False
    
    # Get all files in the directory
    files = os.listdir(directory_path)
    
    # Find the first part of any 7z split archives
    first_parts = [f for f in files if f.endswith('.7z.001')]
    
    if not first_parts:
        print(f"No 7z split archive files found in {directory_path}")
        return False
    
    # Extract each archive
    for first_part in first_parts:
        archive_path = os.path.join(directory_path, first_part)
        print(f"Extracting {archive_path}...")
        
        try:
            # Check if 7z is installed
            subprocess.run(['7z', '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        except FileNotFoundError:
            print("Error: 7z command not found. Please install p7zip or p7zip-full package.")
            return False
        
        # Extract the archive to the same directory
        cmd = ['7z', 'x', archive_path, '-o' + directory_path]
        
        try:
            process = subprocess.run(cmd, check=True)
            if process.returncode == 0:
                print(f"Successfully extracted {first_part}")
            else:
                print(f"Failed to extract {first_part}. Return code: {process.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"Error extracting {first_part}: {e}")
            return False
    
    return True

if __name__ == "__main__":
    # Default directory path
    directory_path = "/data/datasets/affective/MAFW/MAFW/data/clips"
    
    # Allow custom directory path from command line
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    
    print(f"Extracting 7z archives in: {directory_path}")
    
    if extract_7z_files(directory_path):
        print("Extraction completed successfully.")
    else:
        print("Extraction failed.") 