"""This module provides `QR Code` basic functionalities.

------------

Exports
------------

    - :py:func:`main.generate_qr` is a function which generates `QR Code` and saves it in an output file
    - :py:func:`main.read_qr` is a function which reads `QR Code` image

-------------------------------

Related documentations/articles
-------------------------------

    - numpy module: https://numpy.org
    - cv2 module: https://github.com/opencv/opencv-python
    - qrcode module: https://github.com/lincolnloop/python-qrcode
    - typing module: https://docs.python.org/3/library/typing.html
    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

import numpy as np
import cv2

from typing import Tuple
from qrcode import QRCode


def generate_qr(
    data: str,
    output_path: str,
    output_name: str,
    fill_color="black",
    back_color="white",
) -> Tuple[int, int]:
    """Generates `QR Code` and saves it in an output file.

    :param data: any string tha you want to store in `QR Code`
    :type data: str
    :param output_path: path, where the output should be saved in
    :type output_path: str
    :param output_name: output filename (includes extension, e.g. test.png)
    :type output_name: str
    :param fill_color: color, `QR Code` to be filled with, defaults to "black"
    :type fill_color: str, optional
    :param back_color: `QR Code` background color, defaults to "white"
    :type back_color: str, optional
    :return: shape of the image
    :rtype: Tuple[int, int]
    """
    qr = QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make()

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f"{output_path}/{output_name}")

    return np.array(qr.get_matrix()).shape


def read_qr(file_path: str, show_qr = False) -> str:
    """Reads `QR Code` image.

    :param file_path: path of `QR Code` image (includes extension, e.g. test.png)
    :type file_path: str
    :param show_qr: should show `QR Code` in a windows or not, defaults to False
    :type show_qr: bool, optional
    :return: `QR Code` data
    :rtype: str
    """
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    if bbox is not None:
        n_lines = len(bbox[0])
        for i in range(n_lines):
            point1 = tuple(map(int, bbox[0][i]))
            point2 = tuple(map(int, bbox[0][(i + 1) % n_lines]))
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

    if show_qr:
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return data
