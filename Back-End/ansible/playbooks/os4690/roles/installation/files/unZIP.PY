from zipfile import ZipFile
import sys

with ZipFile("/mnt/c/ACE"+str(sys.argv[1])+"D/ACE"+str(sys.argv[1])+"D001.zip", "r") as zip:
    zip.extractall("/mnt/c/ACE"+str(sys.argv[1])+"D")
    print("File is unzipped in %s folder" % "/mnt/c/ACE"+str(sys.argv[1])+"D")
