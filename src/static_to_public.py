#### instructions
# delete all contents of public
# copy all files, subdirectories, nested files etc
# log each copy
from os import listdir, mkdir
from os.path import exists, join, isfile
from shutil import copy, rmtree

def copy_static_to_public(static, public):
    static_contents = find_dir_cont(static)
    public_contents = find_dir_cont(public)
    copy_to_dest(public_contents[0], public_contents[1], "deleted")
    copy_to_dest(static_contents[0], static_contents[1], public)


def find_dir_cont(fromdir):
    print(f"\nchecking directory {fromdir}")
    files = []
    dirs = []
    if exists(fromdir) and len(listdir(fromdir)) > 0 :
        items = listdir(fromdir)
        print(f"directory {fromdir} exists")
        print(f"contents are : {items}")
        for item in items:
            diritem = fromdir +  "/" + item 
            print(f"[item] {item} isfile(diritem): {isfile(diritem)}")
            if isfile(diritem):
                files.append(diritem)
            else:
                dirs.append(diritem)
                find_dir_cont(diritem)
    print(f"returing files {files}, and dirs {dirs}\n")
    return files, dirs

def copy_to_dest(files, dirs, todir):
    if todir != "deleted":
        rmtree(todir)

    for d in dirs:
        print(f"[copying d todir] d:{d} todir:{todir}")
        if not exists(d):
            mkdir(d)
    for f in files:
        print(f"[copting f todir] f:{f} todir:{todir}")
        if not exists(f):
            copy(f, todir)
    print(f"\nfiles and dirs copied to {todir}")
