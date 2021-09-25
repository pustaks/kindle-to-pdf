# Print a book from Kindle or VitalSource to PDF

This script simulates mouse click in the next page button and takes screenshot of current page in the opened book.

## Pre-requirements
Download Python: https://www.python.org/downloads/
Change to the repository's directory and run:

```bash
pip install -r requirements.txt
```

## Usage
Run in command line:

```bash
python app.py top_left right_bottom main_window total_page
# Ex: python app.py 153,78 892,990 941,537 785
```

When running this, keep the command line window in front of and smaller than the main window (Kindle/Vitalsource window). Set the main_window input to a spot in the main window that is not a button.

## GUI: Electron app

https://github.com/plainlab/plainprinter

(I will create my own GUI for this app if there is any demand)
