# NMSUnpack

## Usage
Download and run the main.py file.  
If you've changed the installation directory, the script will ask for the new path.

## How does it work?
By unpacking the .pak files in the No Man's Sky installation folder, the CPU overhead while playing is reduced as the game no longer has to decompress large files on the fly.

Most noticeable is that the lag which normally happens while transitioning to or from a planet has reduced a lot.

[PSArcTool](https://github.com/periander/PSArcTool) is used to unpack the files. While it's not open source, a VirusTotal scan has indicated that it is unlikely to contain any malicious code.

## FAQ / Troubleshooting
### The terminal window closes instantly
Instead of directly running the script, launch a terminal manually and run `python path/to/main.py` to see the script's output and error message.
Please report it in the [Issues](https://github.com/Swarkin/NMSUnpack/issues) tab!
