# Print a book from Kindle or VitalSource to PDF

This script simulates mouse clicks and keypresses to take screenshots 

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

After creating the PDF, set page numbers, bookmarks and OCR using software like Adobe Acrobat DC.

## GUI: Electron app

https://github.com/plainlab/plainprinter

I will create a GUI for this app if there is a demand
