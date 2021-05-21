



audio_ext = ['mp3']
video_ext = ['mp4']
img_ext = ['jpg']

user_filename = input('enter file name:').lower()
user_filename_splited = user_filename.split('.')

ufs = user_filename_splited[-1]

if ufs in audio_ext :
	print ('it\'s audio file')
elif ufs in video_ext :
	print ('it\'s video file')
elif ufs in img_ext :
	print (' it\'s img')
else:
	print('it\'s unknown file')