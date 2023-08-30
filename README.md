# NMSUnpack

## Usage
Download and run the main.py file.  
If you've changed the installation directory, the script will ask for the new path.

## How does it work?
By unpacking the .pak files in the No Man's Sky installation folder, the CPU overhead while playing is reduced as the game no longer has to decompress large files on the fly. This really helps out on less powerful computers, and you'll still see an improvement on high-end systems.

Personally, I've observed that the lag when transitioning to or from a planet has completely disappeared. Melee boosts over long distances on a planet's surface also feel smoother and I was able to increase my graphics settings overall.

[PSArcTool](https://github.com/periander/PSArcTool) is used to unpack the files. While it's not open source, a VirusTotal scan has indicated that it is unlikely to contain any malicious code.

## FAQ / Troubleshooting
### The terminal window closes instantly
Make sure you have the `requests` module installed by running `pip install requests`.  
If that doesn't fix the problem, launch a terminal manually and run `python path/to/main.py` to see the script's output.

## Contributing
If you encounter any issues, please report them in the [Issues](https://github.com/Swarkin/NMSUnpack/issues) tab.  
Any contribution is highly appreciated! If you do submit a pull request, please test your edited script on a fresh installation. Thank you!
