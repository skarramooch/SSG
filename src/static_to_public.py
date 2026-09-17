#### instructions
# delete all contents of public
# copy all files, subdirectories, nested files etc
# log each copy
from os import listdir, mkdir
from os.path import exists, join, isfile, isdir
from shutil import copy, rmtree


def create_map(fromdir, todir):
    mapping_dict = {}
    if exists(fromdir) and len(listdir(fromdir)) > 0:
        items = listdir(fromdir)
        for item in items:
            fromdiritem = join(fromdir, item)
            todiritem = join(todir, item)
            mapping_dict[fromdiritem] = [todir, item]
            if isdir(fromdiritem):
                sub_mapping = create_map(fromdiritem, todiritem)
                mapping_dict.update(sub_mapping)
    return mapping_dict


def copy_static_to_public(fromdir,todir):
    mapping_dict = create_map(fromdir, todir)
    if exists(todir) and todir != "deleted":
        rmtree(todir)
    for key in mapping_dict:
        prefix = ""
        for value in range(len(mapping_dict[key]) - 1):
            prefix = join(prefix, mapping_dict[key][value])
            if not exists(prefix):
                mkdir(prefix)
        if isdir(prefix):
            if not exists(prefix):
                mkdir(prefix)
        suffix = mapping_dict[key][-1]
        fulldest = join(prefix, suffix)
        if isdir(key):
            if not exists(prefix):
                mkdir(prefix)
            mkdir(fulldest)
        else:
            copy(key, join(prefix, suffix))

