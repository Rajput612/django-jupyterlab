from django.shortcuts import redirect,HttpResponse
import subprocess
import time
import os


def open_jupiter_notbook(request,pk=None):
    path = f"C:\\Users\\BLP\\Desktop\\Projects\\learn\\{pk}"
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    b= subprocess.check_output("jupyter-lab list".split()).decode('utf-8')
    if "9999" not in b:
        a=subprocess.Popen("jupyter-lab  --no-browser --port 9999".split())
    start_time = time.time()
    unreachable_time = 10
    while "9999" not in b:
        timer = time.time()
        elapsed_time = timer-start_time
        b= subprocess.check_output("jupyter-lab list".split()).decode('utf-8')
        if "9999" in b:
            break
        if elapsed_time > unreachable_time:
            return HttpResponse("Unreachable")
    path = b.split('\n')[1].split('::',1)[0]
    print("path:-",path)
    #You can here add data to your path if you want to open file or anything
    return redirect(path)