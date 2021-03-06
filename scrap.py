import os.path
import sys
import urllib.request
import urllib.parse
import time

api_url = "http://scrap.hankapi.com"
scrap_key_filename = sys.path[0] + "/scrap_key"
scrap_version = 6

def get_key_from_file():
    if os.path.isfile(scrap_key_filename):
        with open (scrap_key_filename, "r") as f:
            key = f.read()

        return key
    else:  
        print ("Error: scrap_key setup file does not exist. Invoke scrap.setup (key-name) from a python script to set.")
        return "ERROR"

def write(text):
    key = get_key_from_file()
    if key == "ERROR" or key == "":
        return
    else:
        url = api_url + "/write"
        values_to_post = {
            'key': key,
            'text': text,
            'version': str(scrap_version)}
        data_to_post = urllib.parse.urlencode(values_to_post)
        data_to_post = data_to_post.encode('ascii')
        try:
            request_to_post = urllib.request.Request (url, data_to_post)
            with urllib.request.urlopen(request_to_post) as response:
                x = response.read() 
        except Exception as e:
            time.sleep(5)

def setup(key):
    with open (scrap_key_filename, "w") as f:
        f.write (key)

def new_section():
    write("~~~~~~~~~~~~~~~~~~~~")

def auto_scrap_on_print():
    sys.stdout.write = write

def auto_scrap_on_error():
    sys.stderr.write = write

