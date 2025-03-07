from pathlib import Path
import os
def rename_files(folder):
    path = Path(folder)
    for item in path.iterdir():
        if os.path.isfile(item):
            try:
                old_name = str(item)
                print(f"Renaming file {item} to .md")
                os.rename(old_name,old_name.replace(".txt",".md"))
            except Exception as e:
                print(e)
                

dir = input("Enter dir path for all files to renamed by removing space to _ : ")
if dir=="":
    print("DIR path is empty")
    exit()
if not os.path.exists(dir):
    print(f"{dir} DIR path is not found")
    exit()
if os.path.isfile(dir):
    print(f"{dir} is a file")
    exit()
rename_files(dir)