#### instructions
# delete all contents of public
# copy all files, subdirectories, nested files etc
# log each copy
from os import listdir, mkdir
from os.path import exists, join, isfile, isdir
from shutil import copy, rmtree



def copy_static_to_public(fromdir, todir):
    mapping_dict = {}
    if exists(fromdir) and len(listdir(fromdir)) > 0:
        items = listdir(fromdir)
        print(f"[items] {items}")
        for item in items:
            fromdiritem = join(fromdir, item)
            todiritem = join(todir, item)
            print(f"fromdiritem {fromdiritem}, todiritem {todiritem}")
            mapping_dict[fromdir] = todir
            if isdir(fromdiritem):
                sub_mapping = copy_static_to_public(fromdiritem, todiritem)
                mapping_dict.update(sub_mapping)
    print(f"[mapping_dict] {mapping_dict}")
    return mapping_dict
    
"""
from pathlib import Path

def find_markdown_files(folder: Path):
    matches = []

    for entry in folder.iterdir():
        if entry.is_file() and entry.suffix == ".md":
            matches.append(entry)
        elif entry.is_dir():
            # Recursively search the subfolder
            sub_matches = find_markdown_files(entry)
            # Combine the results into our current matches list
            matches.extend(sub_matches)  # or matches += sub_matches

    return matches"""

"""
#def copy_static_to_public(static, public):
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
            print(f"[fromdiritem] {fromdiritem}")
            # pathdiritem = join(fromdir, diritem)
            # print(f"[pathdiritem] {pathdiritem}")
            print(f"[item] {item} isfile(fromdiritem): {isfile(fromdiritem)}, isdir(fromdiritem): {isdir(fromdiritem)}")
            if not isdir(fromdiritem):
                print(f"[FILE FOUND] adding {fromdiritem} to files")
                files.append(fromdiritem)
            else:
                dirs.append(diritem)
                print(f"[DIRECTORY FOUND] adding {diritem} to dirs, and searching further")
                find_dir_cont(fromdiritem)
    print(f"[FIND DIR CONT COMPLETE] returing files {files}, and dirs {dirs}\n")
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

    """
