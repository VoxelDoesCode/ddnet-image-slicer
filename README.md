Introduction
------------
This is a tool to automatically slice and crop images from the [DDNet](https://github.com/ddnet/ddnet) assets files into their own, packaged asset bunch and ZIP files.

In its current state, this is merely a proof-of-concept! There will be more features in the future.

Dependancies
------------
This project relies on [Pillow](https://pillow.readthedocs.io/en/stable/index.html) for [Python](https://www.python.org/downloads/) in order to trim images.

To install Pillow, run this inside your command line (Make sure you have Python installed first!):

    python -m pip install --upgrade pip
    python -m pip install --upgrade Pillow

If on MacOS, full instructions will be avalable [on the official website.](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

How to use
----------
Make sure you have a folder inside `inputs` containing all the images needed. If any images are missing, a copy is located inside the `inputs/default` folder, or inside DDNet's data folder. Don't forget to check `data/editor` for any images from there!

Then, run in the command line, where NAME_OF_FOLDER is the name of the folder you want to slice up (for example default):

    python main.py NAME_OF_FOLDER

It should split all the image altases into their own assets, and output a folder of the same name inside `outputs`! Inside the folder will include the compressed and uncompressed version for all the assets.

TODO
----
* Allow for seperate images to be split
* Allow the rebuilding of already split assets