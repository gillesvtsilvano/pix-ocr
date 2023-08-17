import numpy
import os
import cv2
from utils import hash_file_sha1


class Image:
    image: numpy.ndarray
    hash: str
    hash_function: str
    filepath: str
    filename: str

    def __init__(self, filepath):
        try:
            self.filepath = filepath
            self.filename = filepath.split(os.path.sep)[-1]
            if not cv2.haveImageReader(filepath):
                raise Exception('Error trying to read an image %s', filepath)
            else:
                hash = hash_file_sha1(filepath)
                if not hash:
                    raise Exception('Could not obtain hash of the file %s', filepath)
                self.hash = hash
                self.hash_function = 'SHA1'
                self.image = cv2.imread(filepath)
        except Exception as exception:
            raise Exception('Error in Image constructor') from exception