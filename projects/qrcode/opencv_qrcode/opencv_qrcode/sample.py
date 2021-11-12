"""This module runs main script functionalities with a sample data.

------------

Exports
------------

    - :py:func:`sample.main` is main/entry function

-------------------------------

Related documentations/articles
-------------------------------

    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

from opencv_qrcode.main import generate_qr, read_qr


def main():
    """This is main/entry function.
    """
    data = "https://github.com/iranipy/iranipy"
    output_name = "iranipy_github.png"
    samples_dir = "samples"

    generate_qr(data=data, output_name=output_name, output_path=samples_dir)

    qr_data = read_qr(f"{samples_dir}/{output_name}", show_qr=True)
    print(f"QR Code data:\n{qr_data}")


if __name__ == "__main__":
    main()
