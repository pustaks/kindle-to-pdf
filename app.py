import argparse
import os
import tempfile

import autopy
import img2pdf
import ctypes
import time

def screenshot(top_left, right_bottom, main_window, total_page):
    rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
    images = []
    temp_dir = tempfile.mkdtemp()
    
    autopy.mouse.move(*main_window)
    autopy.mouse.click(delay=0.1)
    
    for i in range(total_page):
        page_num = "{}".format(i).zfill(len(str(total_page)))
        file_name = os.path.join(temp_dir, 'book-page-{}.png'.format(page_num))
        images.append(file_name)

        time.sleep(1)
        autopy.bitmap.capture_screen((top_left, rect_size)).save(file_name)
        ctypes.windll.user32.keybd_event(0x22,0,0,0)

    return images


def image2pdf(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take book screenshots.')
    parser.add_argument('top_left', type=str)
    parser.add_argument('right_bottom', type=str)
    parser.add_argument('next_button', type=str)
    parser.add_argument('total_page', type=int)

    args = parser.parse_args()

    top_left = tuple(map(lambda x: int(x), args.top_left.split(',')))
    right_bottom = tuple(map(lambda x: int(x), args.right_bottom.split(',')))
    next_button = tuple(map(lambda x: int(x), args.next_button.split(',')))
    total_page = args.total_page

    print("Take book screenshot at {} {} and next at {} with {} pages".format(
        top_left, right_bottom, next_button, total_page
    ))

    images = screenshot(top_left, right_bottom, next_button, total_page)
    image2pdf(images)

    print("Done, book saved in book.pdf.")
