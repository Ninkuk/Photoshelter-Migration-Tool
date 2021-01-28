# python libraries
import requests

headers = {"X-PS-Api-Key": "ampJX8YXDtY", "X-PS-Auth-Token": "FW8yu6tCN0OxKmw6oZly"}
url = "https://www.photoshelter.com/psapi/v3/mem"


def authenticate_organization():
    session = requests.Session()
    endpoint = f"{url}/organization/O0000gsayrCMBhsM/authenticate"
    session.get(endpoint, headers=headers)
    return session


def get_image_file_name(session, image_id):
    endpoint = f"{url}/image/{image_id}"
    request = session.get(endpoint, headers=headers)
    return request.json()["data"]["Image"]["file_name"]


def download_image(session, image_id):
    endpoint = f"{url}/image/{image_id}/download"
    request = session.get(endpoint, headers=headers, stream=True)
    return request.raw


def get_image_metadata(session, image_id, metadata_type):
    endpoint = f"{url}/image/{image_id}/{metadata_type}"
    request = session.get(endpoint, headers=headers)
    return request.json()["data"]


def get_collection_name(collection_id):
    endpoint = f"{url}/collection/{collection_id}"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Collection"]["name"]


def get_sub_collections(collection_id):
    endpoint = f"{url}/collection/{collection_id}/children"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Children"]


def get_gallery_name(gallery_id):
    endpoint = f"{url}/gallery/{gallery_id}"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["Gallery"]["name"]


def get_gallery_children(gallery_id):
    endpoint = f"{url}/gallery/{gallery_id}/images"
    request = requests.get(endpoint, headers=headers)
    return request.json()["data"]["GalleryImage"]
