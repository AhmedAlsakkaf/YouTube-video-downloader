from pytube import YouTube

def on_complete(stream, filepath):
    print('download complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100), 2)}%'
    print(progress_string)

link = input("Youtube link: ")
video_object = YouTube(link)

# The information of the video
print(f'title:      {video_object.title}')
print(f'length:    {round(video_object.length / 60, 2)} minutes')
print(f'views:     {video_object.views / 1000000} millions')
print(f'author:    {video_object.author}')

# download
print('download: (b)est | (w)orst | (a)udio | (e)xit')
download_choice = input('choice: ')

if download_choice == 'b':
    video_object.streams.get_highest_resolution().download(r'D:\downloads\Myvedios')
elif download_choice == 'w':
    video_object.streams.get_lowest_resolution().download(r'D:\downloads')
elif download_choice == 'a':
    video_object.streams.get_audio_only().download(r'D:\downloads\Audio')
else:
    print('Invalid choice')
