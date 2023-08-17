'''Utilities module'''

import os
import logging
import cv2
import hashlib


def load_images(path: str) -> list:
    """Verify which files are images in path folder and returns a dictionary"""

    ret_images = []
    try:
        for filename in os.listdir(path):
            filepath = os.path.join(os.getcwd(), path, filename)
            if os.path.isfile(filepath):
                if not cv2.haveImageReader(filepath):
                    logging.warning('Could not read %s because it is not a file. Skipping. ', filename)
                else:
                    hash = hash_file_sha1(filepath)
                    if not hash:
                        raise Exception('Could not obtain hash of the file %s', filename)
        
                    img = cv2.imread(filepath)

                    # Add filename and hash to the returned object
                    setattr(img, 'filename', filepath)
                    setattr(img, 'hash', hash)
                    setattr(img, 'hashfunc', 'sha1')
                    ret_images.append(img)
            else:
                logging.warning('Could not read %s because it is not a file.', filename)
    except Exception as exception:
        raise ValueError(f'Error trying to open images from \'{path}\'') from exception
    return ret_images


# ref: https://www.programiz.com/python-programming/examples/hash-file
def hash_file_sha1(filename):
   '''This function returns the SHA-1 hash
   of the file passed into it'''

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()    