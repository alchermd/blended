#!/usr/bin/env python3
import pytesseract
import glob
import os

def main():
    """
    Reads the contents of the images folder and writes them into
    a file named output.txt

    TODO: Automate the population of images folder.
    """
    try:
        import Image
    except ImportError:
        from PIL import Image

    # Delete outfile.
    os.remove('output.txt')
    print('output.txt deleted')

    for pg, img in enumerate(sorted(glob.glob('./src/*'))):
        with open('output.txt', 'a+') as f:
            f.write(
                '\n --- THIS IS PAGE #{} --- \n'.format(pg + 1) +
                pytesseract.image_to_string(Image.open(img))
            )

    print('Your text is now completed - see output.txt')

if __name__ == '__main__':
    main()