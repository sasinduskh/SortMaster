from setuptools import setup

APP = ['main.py']  # Your main Python file
DATA_FILES = []  # Any additional files (like icons, images, etc.)
OPTIONS = {
    'argv_emulation': True,  # Allows the app to receive command-line arguments
    'iconfile': 'assets/icon.icns',  # Path to your app's icon (optional)
    'packages': ['tkinter', 'os', 'shutil']  # Specify the libraries you used
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
