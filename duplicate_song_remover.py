import hashlib
import argparse
import os

def files_in_directory(directory):
	file_paths=[]
	for folder,temp,files in os.walk(directory):
		for file in files:
			file_paths.append(os.path.abspath(os.path.join(folder,file)))

	delete_duplicate_files(file_paths)

def delete_duplicate_files(file_paths):
	for file in file_paths:
		if os.path.isdir(file):
			files_in_directory(file)
		elif file.endswith('mp3'):
			if is_duplicate_song(file):
				os.remove(file)

def get_file_hash(file):
	readsize=64*1024
	with open(file,'rb') as f:
		data=f.read(readsize)
		f.seek(-readsize,os.SEEK_END)
		data+=f.read(readsize)
	return(hashlib.md5(data).hexdigest)

def is_duplicate_song(file):
	md5=get_file_hash(file)
	if md5 in song_file:
		return True
	else:
		song_file.add(md5)
		return True

parser=argparse.ArgumentParser()
parser.add_argument('filename',type=str)
args=parser.parse_args()
if len(args.filename)>0:
	files_in_directory(args.filename)
	song_file=set()




