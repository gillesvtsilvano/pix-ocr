'''Utilities module'''

import os
import logging
import cv2

def load_images(path: str) -> list:
    """Verify which files are images in path folder and returns a dictionary"""

    ret_images = []
    try:
        for file in os.listdir(path):
            if os.path.isfile(file):
                if cv2.haveImageReader(file):
                    logging.warning('Could not read %s bacause it is not an image ' + 
                                    'or it is not supported by OpenCV.', file)
                else:
                    img = cv2.imread(file)

                    # Add filename to the returned object
                    img.filename = file
                    ret_images.append(cv2.imread(file))
            else:
                logging.warning('Could not read %s because it is not a file.', file)
    except Exception as exception:
        raise ValueError(f"Error trying to open images from \'{path}\'") from exception
    return ret_images
