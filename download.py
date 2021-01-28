# python libraries
import json
import os
import shutil
import requests

# program modules
import api_calls
import filesystem


# retrieve the gallery IDs and paths stored in galleries.txt
def get_data():
    with open("galleries.txt") as f:
        lines = [line.rstrip('\n') for line in f]
        data = {}
        for line in lines:
            temp = line.split(": ")
            data[temp[0]] = temp[1]
        return data


# save the image from raw data to jpg
def save_image(file_path, raw_img):
    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(raw_img, f)
    except Exception as error:
        filesystem.log_error(error)
        print(f"Error Saving Image: {file_path}")


# download the raw image data and other useful info
def download_image(session, image, path):
    image_id = image["image_id"]
    file_name = api_calls.get_image_file_name(session, image_id)
    raw_image = api_calls.download_image(session, image_id)
    save_image(os.path.join(path, file_name), raw_image)
    download_metadata(session, image_id, file_name, path)


def save_metadata(file_path, data):
    with open(file_path, "w") as f:
        f.write(json.dumps(data))


# download the metadata if it exists
def download_metadata(session, image_id, image_name, path):
    iptc_meta = api_calls.get_image_metadata(session, image_id, "iptc")
    xmp_meta = api_calls.get_image_metadata(session, image_id, "xmp")
    exif_meta = api_calls.get_image_metadata(session, image_id, "exif")

    if iptc_meta is not None:
        save_metadata(os.path.join(path, f"iptc/{image_name}.json"), iptc_meta)
    if xmp_meta is not None:
        save_metadata(os.path.join(path, f"xmp/{image_name}.json"), xmp_meta)
    if exif_meta is not None:
        save_metadata(os.path.join(path, f"exif/{image_name}.json"), exif_meta)


# make 3 directories for each gallery
def make_metadata_directories(path):
    os.mkdir(os.path.join(path, "IPTC"))
    os.mkdir(os.path.join(path, "XMP"))
    os.mkdir(os.path.join(path, "EXIF"))
    print("Created metadata directories...")


# main function that drives downloading of all images
def download_all():
    # get IDs and paths of galleries
    data = get_data()

    # auth org
    session = api_calls.authenticate_organization()

    # traverse galleries
    for gallery in data:
        print("------------------------------")
        print(f"Started downloading {gallery}...")

        # get img ID's
        images = api_calls.get_gallery_children(gallery)

        # save the path
        path = data[gallery]

        # make metadata folders for each gallery
        make_metadata_directories(path)

        for image in images:
            download_image(session, image, path)

        print("Downloaded all images...")
        print("------------------------------")
