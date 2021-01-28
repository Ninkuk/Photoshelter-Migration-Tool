# python libraries
import requests

headers = {"X-PS-Api-Key": "API_KEY_HERE", "X-PS-Auth-Token": "AUTH_TOKEN_HERE"}
url = "https://www.photoshelter.com/psapi/v3/mem"


# authenticates your organization, needed for downloading  images
def authenticate_organization():
    session = requests.Session()
    endpoint = f"{url}/organization/ORG_ID_HERE/authenticate"
    session.get(endpoint, headers=headers)
    return session


# get the image file name with extension
def get_image_file_name(session, image_id):
    endpoint = f"{url}/image/{image_id}"
    request = session.get(endpoint, headers=headers)
    return request.json()["data"]["Image"]["file_name"]


# get/download the raw image data as I/O stream
def download_image(session, image_id):
    endpoint = f"{url}/image/{image_id}/download"
    request = session.get(endpoint, headers=headers, stream=True)
    return request.raw


# get the image metadata (iptc, exif, xmp, license, custom etc.)
def get_image_metadata(session, image_id, metadata_type):
    endpoint = f"{url}/image/{image_id}/{metadata_type}"
    request = session.get(endpoint, headers=headers)
    return request.json()["data"]


# get the collection name for creating directories
def get_collection_name(collection_id):
    endpoint = f"{url}/collection/{collection_id}"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Collection"]["name"]


# get the children id's for a collection
def get_sub_collections(collection_id):
    endpoint = f"{url}/collection/{collection_id}/children"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Children"]


# get the gallery name for creating directories
def get_gallery_name(gallery_id):
    endpoint = f"{url}/gallery/{gallery_id}"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Gallery"]["name"]


# get the image id's for a gallery
def get_gallery_children(gallery_id):
    endpoint = f"{url}/gallery/{gallery_id}/images"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["GalleryImage"]
