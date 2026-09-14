#### instructions
# delete all contents of public
# copy all files, subdirectories, nested files etc
# log each copy
from os import listdir, mkdir
from os.path import exists, join, isfile, isdir
from shutil import copy, rmtree

def copy_static_to_public(static, public):
    static_contents = find_dir_cont(static)
    public_contents = find_dir_cont(public)
    print(f"copy to dest public {public_contents[0]}, {public_contents[1]}, to deleted")
    copy_to_dest(public_contents[0], public_contents[1], public, "deleted")
    copy_to_dest(static_contents[0], static_contents[1], static, public)


def find_dir_cont(fromdir):
    print(f"\nchecking directory {fromdir}")
    files = []
    dirs = []
    if exists(fromdir) and len(listdir(fromdir)) > 0 :
        items = listdir(fromdir)
        print(f"directory {fromdir} exists")
        print(f"contents are : {items}")
        for item in items:
            diritem =  "/" + item
            fromdiritem = fromdir + "/" + item
            print(f"[item] {item} isfile(fromdiritem): {isfile(fromdiritem)}, isdir(fromdiritem): {isdir(fromdiritem)}")
            if not isdir(fromdiritem):
                # pathdiritem = join(fromdir, diritem)
                print(f"adding {diritem} to files")
                files.append(diritem)
            else:
                # pathdiritem = join(fromdir, diritem)
                dirs.append(diritem)
                print(f"[DIRECTORY FOUND] adding {diritem} to dirs, and searching further")
                find_dir_cont(diritem)
    print(f"returing files {files}, and dirs {dirs}\n")
    return files, dirs

def copy_to_dest(files, dirs, fromdir, todir):
    print(f"[todir]: {todir}")
    print(f"[{todir} exists] {exists(todir)}")
    if exists(todir) and todir != "deleted":
        rmtree(todir)
    if not exists(todir):
        mkdir(todir)
        print(f"[{todir} created] {exists(todir)}")

    for d in dirs:
        print(f"[copying d todir] d:{d} todir: {todir}")
        fulld = todir + d
        if not exists(fulld):
            mkdir(fulld)
    for f in files:
        print(f"[copying f todir] f:{f} todir: {todir}")
        fullf = fromdir + f
        copy(fullf, todir)
    print(f"\nfiles and dirs copied to {todir}|\n**********\n")
