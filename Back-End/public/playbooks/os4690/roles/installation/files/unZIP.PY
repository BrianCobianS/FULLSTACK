from zipfile import ZipFile
with ZipFile("/mnt/c/ACE3D/ACE3D001.zip", "r") as zip:
    zip.extractall("/mnt/c/ACE3D")
    print("File is unzipped in %s folder" % "/mnt/c/ACE3D")
