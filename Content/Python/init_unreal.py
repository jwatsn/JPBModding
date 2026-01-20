import subprocess
import unreal
import os
import threading

def cook_pak_only():
    engine_dir = os.path.abspath(unreal.Paths.engine_dir())
    project_path = os.path.abspath(unreal.Paths.get_project_file_path())
    #runuat = os.path.join(engine_dir, "Build", "BatchFiles", "RunUAT.bat")
    runuat = os.path.join(engine_dir,"Binaries","Win64", "UnrealEditor.exe")
    cmd = [
        runuat,
        f"{project_path}",
        f"-run=cook",
        "-targetplatform=Windows",
        "-cookall",
        "-Compressed",
        #"-NODEV",
        "-SKIPEDITORCONTENT",
        #"-NoGameAlwaysCook",
        #"-NoDefaultMaps",
        #"-CookSkipRequests"
    ]

    unreal.log("Starting Cook + Pak (RunUAT)…")
    
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    def stream(pipe, log_func):
        for line in iter(pipe.readline, ""):
            log_func(line.rstrip())

    threading.Thread(
        target=stream,
        args=(proc.stdout, unreal.log),
        daemon=True
    ).start()

    threading.Thread(
        target=stream,
        args=(proc.stderr, unreal.log_error),
        daemon=True
    ).start()

cook_pak_only()