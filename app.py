#!/usr/bin/env python3
import pytesseract
import glob

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

    for pg, img in enumerate(sorted(glob.glob('./src/*'))):
        with open('output.txt', 'a+') as f:
            f.write(
                '\n --- THIS IS PAGE #{} --- \n'.format(pg + 1) +
                pytesseract.image_to_string(Image.open(img))
            )

    print('Your text is now completed.')

if __name__ == '__main__':
    main()