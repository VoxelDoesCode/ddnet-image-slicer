Introduction
------------
This is a tool to automatically slice and crop images from the [DDNet](https://github.com/ddnet/ddnet) assets files into their own, packaged asset bunch.

In its current state, this is merely a proof-of-concept! It only crops images and sorts them into non-compressed folders. In the future there will be ZIP compression and merging of packs.

Dependancies
------------
This project relies on [Pillow](https://pillow.readthedocs.io/en/stable/index.html) for [Python](https://www.python.org/downloads/) in order to trim images.

To install Pillow, run this inside your command line (Make sure you have Python installed first!):

    python -m pip install --upgrade pip
    python -m pip install --upgrade Pillow

If on MacOS, full instructions will be avalable [on the official website.](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

How to use
----------
Make sure you have a folder inside `inputs` containing all the images needed. An example folder named `inputs/defaults` exists for reference.
Then, run in the command line, where NAMEOFFOLDER is the name of the folder you want to slice up:

    python main.py NAMEOFFOLDER

It should split all the image altases into their own assets, and output a folder of the same name inside `outputs`! If any images are missing, a copy is located inside the `inputs/defaults` folder, or inside DDNet's data folder. Don't forget to check `data/editor` for any images from there!

TODO
----
* ~~Create a new folder for each run~~
* ~~Accept other folders as input~~
* Compress into a ZIP, maybe?
* Allow for seperate images to be split
* Allow the rebuilding of already split assets