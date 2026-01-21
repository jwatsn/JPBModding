import subprocess
import unreal
import os
import threading
import shutil

current_step = [0,]
is_done = [False,False]
check_done_handle = [None,]

pak_name = ["none",]
chunk_id = [100,]
process = [None,]

has_error = [False,]

def pakgen_haserror():
    if has_error[0]:
        return 1
    return 0

def pakgen_iscomplete():
    if is_done[1]:
        return 1
    return 0

def stream(pipe, log_func):
    for line in iter(pipe.readline, ""):
        log_func(line.rstrip())

def altstream(pipe, log_func):
    stream(pipe,log_func)
    is_done[0] = True

def run_commands(cmd):
    process[0] = proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    

    threading.Thread(
        target=stream,
        args=(proc.stdout, unreal.log),
        daemon=True
    ).start()

    threading.Thread(
        target=altstream,
        args=(proc.stderr, unreal.log_error),
        daemon=True
    ).start()

def create_paklist(base_path,path):
    ret = ""
    for file in os.listdir(path):
        full_path = f"{path}\\{file}"
        if os.path.isdir(full_path):
            ret += create_paklist(base_path,full_path)
        else:
            relative_path = os.path.relpath(full_path, start=base_path)
            
            
            if relative_path.startswith("ShaderA") or relative_path.startswith("ShaderT"):
                if relative_path.find(f"JPB_Chunk{chunk_id[0]}") < 0:
                    continue

            ret += f"\"{full_path}\" " + "\"" + "../../../JPB/Content/" + relative_path.replace("\\","/") + "\" -compress" + "\n"

    return ret
            

def check_done(delta_time):
    if is_done[0] == True:
        process[0].kill()
        process[0].wait()
        
        if process[0].returncode != 0:
            has_error[0] = True
            unreal.unregister_slate_post_tick_callback(check_done_handle[0])
            is_done[0] = False
            return
        if current_step[0] == 0:
            current_step[0] = 1
            is_done[0] = False
            on_complete()
            print("on complete")
        elif current_step[0] == 1:
            unreal.unregister_slate_post_tick_callback(check_done_handle[0])
            is_done[1] = True
            print("on done")
        else:
            has_error[0] = True

def on_complete():
    project_dir = unreal.Paths.project_dir()
    cook_dir = os.path.abspath(f"{project_dir}\\Saved\\Cooked\\Windows\\JPB\\Content")
    ret = create_paklist(cook_dir,cook_dir)
    engine_dir = os.path.abspath(unreal.Paths.engine_dir())
    response_dir_path = f"{project_dir}\\Saved\\JPBPakGen"
    log_dir_path = response_dir_path
    pak_out_dir = os.path.abspath(f"{project_dir}\\PakOutput")
    os.makedirs(pak_out_dir,exist_ok=True)
    os.makedirs(log_dir_path,exist_ok=True)
    os.makedirs(response_dir_path,exist_ok=True)
    reponse_file_path = f"{response_dir_path}\\PakList_pakchunk{chunk_id[0]}-{pak_name[0]}.txt"
    if os.path.exists(reponse_file_path):
        os.remove(reponse_file_path)
    
    f = open(reponse_file_path,"w")
    f.write(ret)
    f.close()

    command_text = f"\"{pak_out_dir}\\pakchunk{chunk_id[0]}-{pak_name[0]}.pak\" -create=\"{reponse_file_path}\""
    pak_commands_path = f"{log_dir_path}\\PakCommands.txt"
    f = open(pak_commands_path,"w")
    f.write(command_text)
    f.close()
    pak_out_path = f"{pak_out_dir}\\pakchunk{chunk_id[0]}-{pak_name[0]}.pak"
    if os.path.exists(pak_out_path):
        os.remove(pak_out_path)
    cmd = [
        f"{engine_dir}\\Binaries\\Win64\\UnrealPak.exe",
        "-patchpaddingalign=2048",
        "-compressionformats=Oodle", 
        "-compresslevel=4",
        "-compressmethod=Kraken",
        "-platform=Windows",
        f"-CreateMultiple=\"{pak_commands_path}\""
    ]
    run_commands(cmd)

def update_assetlabel(chunkId):
    # asset_data = unreal.EditorAssetLibrary.find_asset_data()
    # if asset_data is None:
    #     has_error[0] = True
    #     return
    asset = unreal.EditorAssetLibrary.load_asset("/Game/ModAssetLabel.ModAssetLabel")
    if asset is None:
        has_error[0] = True
        return
    
    rules = asset.get_editor_property("rules")
    if rules is None:
        has_error[0] = True
        return
    rules.set_editor_property("chunk_id",chunkId)
    unreal.EditorAssetLibrary.save_loaded_asset(asset)
    
def cook_pak_only(chunkId,pakName):
    current_step[0] = 0
    is_done[1] = False
    is_done[0] = False
    has_error[0] = False
    try:
        update_assetlabel(chunkId)
        if has_error[0]:
            return
        check_done_handle[0] = unreal.register_slate_post_tick_callback(check_done)
        pak_name[0] = pakName
        chunk_id[0] = chunkId
        engine_dir = os.path.abspath(unreal.Paths.engine_dir())
        project_path = os.path.abspath(unreal.Paths.get_project_file_path())
        project_dir = unreal.Paths.project_dir()
        cook_dir = f"{project_dir}\\Saved\\Cooked\\Windows\\JPB\\Content"
        if os.path.isdir(cook_dir):
            shutil.rmtree(cook_dir)

        cmd = [
            os.path.join(engine_dir,"Binaries","Win64", "UnrealEditor.exe"),
            f"{project_path}",
            f"-run=cook",
            "-targetplatform=Windows",
            "-cookall",
            "-Compressed",
            "-UnVersioned",
            "-NODEV",
            "-SKIPEDITORCONTENT",
        ]

        unreal.log("Starting Cook + Pak (RunUAT)…")
        
        run_commands(cmd)
    except Exception as e:
        has_error[0] = True

