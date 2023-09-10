import sys
for arg in ['--help', 'help', '/?']:
	if arg in sys.argv:
		print('This experimental script extracts all .pak archives to reduce stutter and CPU overhead while playing No Man\'s Sky.')
		print('--help            | Display help message')
		print("--nms-path \"<path>\" | Override the No Man's Sky install directory (Default: C:\\Program Files (x86)\\Steam\\steamapps\\common\\No Man's Sky)")
		exit()

import requests
import subprocess
import tempfile
import zipfile
import shutil
import time
import os


NMS_DIR = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\No Man's Sky"
if '--nms-path' in sys.argv:
	try:
		NMS_DIR = sys.argv[sys.argv.index('--nms-path')+1]
	except:
		print('No path specified. See --help')
		exit(1)


def is_game_dir_valid(path: str) -> bool:
	return True if os.path.exists(os.path.join(path, 'GAMEDATA\\PCBANKS')) else False


while not is_game_dir_valid(NMS_DIR):
	print('Couldn\'t verify directory.')
	NMS_DIR = input('Paste the game directory here. (Example: C:\\Program Files (x86)\\Steam\\steamapps\\common\\No Man\'s Sky)\n')
else:
	print('Directory appears to be valid.')
print(NMS_DIR)

NMS_GAMEDATA_DIR = os.path.join(NMS_DIR, 'GAMEDATA')
NMS_PCBANKS_DIR = os.path.join(NMS_DIR, 'GAMEDATA\\PCBANKS')

input(f'\nNMS_DIR: {NMS_DIR}'
			f'\nNMS_GAMEDATA_DIR: {NMS_GAMEDATA_DIR}'
			f'\nNMS_PCBANKS_DIR: {NMS_PCBANKS_DIR}'
			'\n'
			'\nBe aware that this script might break.'
			'\n This will use up to 30 GB of additional storage space.'
			'\n Close the game and avoid touching any folders in the installation directory.'
			'\n'
			'\nPress ENTER to start.')


def download_psarctool(url: str, directory: str) -> str:
	r = requests.get(url)
	print(f'{r.status_code}')

	zip_path = os.path.join(directory, 'PSArcTool.zip')
	with open(zip_path, 'wb') as f:
		f.write(r.content)

	with zipfile.ZipFile(zip_path) as z:
		z.extract('PSArcTool.exe', directory)

	exe_path = os.path.join(directory, 'PSArcTool.exe')
	return exe_path


with tempfile.TemporaryDirectory(prefix='psarctool-') as temp_dir:
	paks = []
	for file in os.scandir(NMS_PCBANKS_DIR):
		if file.is_file() and file.name.endswith('.pak'):
			paks.append(file.path)

	if paks:
		print(f'Found .pak files: {paks}')
	else:
		print('No .pak files found!')
		exit(1)

	print(f'Downloading PSArcTool to {temp_dir}...')
	try:
		psarctool_path = download_psarctool('https://github.com/periander/PSArcTool/raw/master/PSArcTool.zip', temp_dir)
	except Exception as e:
		print(f'Failed: {e}')
		exit(1)

	for file in paks:
		print(f'Unpacking {file}...')
		subprocess.Popen([psarctool_path, file], stdout=subprocess.DEVNULL)

	wait_time = 60
	print(f'Waiting {wait_time}s to allow all PSArcTool instances to open...')
	time.sleep(wait_time)

	for file in paks:
		print(f'Removing {file}')
		while True:
			try:
				os.remove(file)
				break
			except PermissionError as e:
				time.sleep(3)

	for v in os.scandir(NMS_PCBANKS_DIR):
		if v.is_dir() or v.name.endswith('.MBIN') or v.name.endswith('.CSV'):
			print(f'Moving {v.path} to {os.path.join(NMS_GAMEDATA_DIR, v.name)}')
			shutil.move(v, os.path.join(NMS_GAMEDATA_DIR, v.name))
		elif v.name.lower().endswith('.txt') and not v.name.lower().endswith('disablemods.txt'):
			print(f'Moving {v.path} to {os.path.join(NMS_GAMEDATA_DIR, v.name)}')
			shutil.move(v, os.path.join(NMS_GAMEDATA_DIR, v.name))
		else:
			print(f'Skipping {v.path}')

	print('\nDone!')
