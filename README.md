Introduction
------------
This is a tool to automatically slice and crop images from the [DDNet](https://github.com/ddnet/ddnet) assets files into their own, packaged asset bunch.

In its current state, this is merely a proof-of-concept! It only crops images and sorts them into non-compressed folders. In the future there will be tools to help split images in a more tidy sense.

Dependancies
------------
This project relies on [Pillow](https://pillow.readthedocs.io/en/stable/index.html) for [Python](https://www.python.org/downloads/) in order to trim images.

To install Pillow, run this inside your command line (Make sure you have Python installed first!):

    python -m pip install --upgrade pip
    python -m pip install --upgrade Pillow

If on MacOS, full instructions will be avalable [on the official website.](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

How to use
----------
Make sure there are no already split images inside the `images/split` folder (I have yet to run tests for that.)
Then, run in the command line:

    python main.py

It should split all the image altases into their own assets! If any images are missing, a copy is located inside the images folder, or inside DDNet's data folder. Don't forget to check `data/editor` for any images from there!

TODO
----
* Create a new folder for each run
* Accept other folders as input
* Compress into a ZIP, maybe?
* Allow for seperate images to be split
* Allow the rebuilding of already split assets