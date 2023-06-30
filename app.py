import os
import time
import subprocess

start_time = time.time()
path = input("Path: ")
path = path.replace('\\', '/')
files = os.listdir(path)

for file in files:
    if file.lower().endswith(('.mts')):
        process = subprocess.run(f'ffmpeg -i "{file}" -c:v copy -c:a aac "{os.path.splitext(file)[0]}.mp4"', cwd=path, shell=True)

files = os.listdir(path)
with open(path + '/list.txt','w') as f:
    for file in files:
        if file.lower().endswith(('.mp4')):
            f.write(f"file '{file}'\n")
            
process = subprocess.run(f'ffmpeg -safe 0 -f concat -i list.txt -c copy output.mp4', cwd=path, shell=True)
print("--- %s seconds ---" % (time.time() - start_time))