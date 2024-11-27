# Photoshelter-Migration-Tool

## About The Project
### What is Photoshelter?
Photoshelter is a digital assets management platform for visual media used by professional photographers and large organizations. It acts as both a cloud storage for images and an online platform for showcasing and delievering assets for clients.

### What is this project?
Photoshelter lacks migrating tools and the only way to download all photos (and their metadata) in bulk is to download each gallery individually. However, with big organizations (like Arizona State University's Enterprise Marketing Hub) that have 3500+ libraries, this is not at all feasible. To automate this process, I decided to use their API and tackle this problem in two parts.

### How does it work?
Firstly, the script would re-create the file structure of photoshelter onto the downloading machine. Since I don't know the entire file structure, I had to recursively traverse through the folders. This process is similar to the [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) of a graph.
<br><br>
To ease things, Photoshelter has two types of folders. Collections, which can contain other other sub-collections and Galleries but not any images. Images can only be present in Galleries which can not have any sub-collections/galleries. While traversing, I kept a txt file with gallery IDs and their paths, so I wouldn't have to traverse to them again.
<br><br>
Finally, with galleries list curated, I could get the image ID's in each gallery and download+save them using raw image data. This was followed by downloading the metadata (IPTC, XMP, EXIF) of all images.

## Installation and Usage
<b>Note: This application is optimized for ASU's migration, you may need to make some changes for your use case. Contact me if you need more details.</b>
<br><br>
Clone the repository
```bash
$ git clone https://github.com/Ninkuk/Photoshelter-Migration-Tool.git
```
Download the dependencies
```bash
$ python -m pip install requests
```
Open [```api_calls.py```](api_calls.py) and add your [```API_TOKEN```](https://www.photoshelter.com/developer/index/register/api_key) and [```AUTH_TOKEN```](https://www.photoshelter.com/developer/index/getting_started/user_authentication)
```python
headers = {"X-PS-Api-Key": "API_KEY_HERE", "X-PS-Auth-Token": "AUTH_TOKEN_HERE"}
```
Add your Organization ID to [```api_calls.py```](api_calls.py)
```python
endpoint = f"{url}/organization/ORG_ID_HERE/authenticate"
```
Finally run ```main.py```
```bash
$ python main.py
```

## Built With
* Python with Requests Library
* Photoshelter API

## Contribution
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact
Ninad Kulkarni - ninadk.dev@gmail.com
<br>
Project Link: [https://github.com/Ninkuk/Photoshelter-Migration-Tool](https://github.com/Ninkuk/Photoshelter-Migration-Tool)
