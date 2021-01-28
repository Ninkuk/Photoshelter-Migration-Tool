# python libraries
import json
import os

# program modules
import api_calls

collection_count = 0
gallery_count = 0


# get the root collections
def get_root_data():
    with open("root_children.json") as f:
        data = json.load(f)
        return data


# replace characters to make valid dir names in os filesystem
def fix_directory_name(directory_name):
    char_replace = {
        "\\": "-",
        "/": "-",
        ":": "-",
        "*": ".",
        "?": " ",
        "\"": "'",
        "<": "(",
        ">": ")",
        "|": "-",
    }

    return directory_name.translate(str.maketrans(char_replace))


# handle folder creation in os
def make_os_directory(base_path, directory_name):
    path = os.path.join(base_path, directory_name)

    try:
        os.mkdir(path)
    except Exception as error:
        # handle error
        log_error(error)
        print(f"Error Saving Collection: {directory_name}")

        # create dummy directory to keep program running
        directory_name = "ERROR"
        path = os.path.join(base_path, directory_name)
        os.mkdir(path)
    finally:
        print(f"Created Collection: {directory_name}")
        return path


# adds the gallery path to a list
def save_path(gallery_id, path):
    with open("galleries.txt", 'a', encoding="utf-8") as f:
        try:
            f.write(f"{gallery_id}: {path}\n")
        except Exception as error:
            log_error(error)


def log_error(error):
    with open("errors.txt", "a") as f:
        f.write(f"\n{error}\n\n\n--------------------------------------------------")


# handles the collections recursively
def create_collections(collections, base_path):
    for collection in collections:
        global collection_count
        collection_count += 1

        # get collection name
        directory_name = api_calls.get_collection_name(collection["collection_id"])

        # fix collection directory name
        directory_name = fix_directory_name(directory_name)

        # create the directory in os
        path = make_os_directory(base_path, directory_name)

        # create sub collections
        sub_collections = api_calls.get_sub_collections(collection["collection_id"])
        create_directories(sub_collections, path)


# handles the galleries and saves in a list
def create_galleries(galleries, base_path):
    for gallery in galleries:
        global gallery_count
        gallery_count += 1

        # get gallery name
        gallery_id = gallery["gallery_id"]
        directory_name = api_calls.get_gallery_name(gallery_id)

        # fix gallery directory name
        directory_name = fix_directory_name(directory_name)

        # create the directory in os
        path = make_os_directory(base_path, directory_name)

        # add path to list
        save_path(gallery_id, path)


# recursive function create shell folders
def create_directories(children, base_path):
    if "Collection" in children:
        create_collections(children["Collection"], base_path)

    if "Gallery" in children:
        create_galleries(children["Gallery"], base_path)


def create():
    create_directories(get_root_data(), "Downloaded")
    print("\n--------------------------------------")
    print(f"Number of collections = {collection_count}")
    print(f"Number of galleries = {gallery_count}")
