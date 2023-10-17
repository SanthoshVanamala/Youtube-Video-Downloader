from pytube import YouTube, Playlist
import os


def download_video(video, download_folder, download_as):
    video_title = video.title
    filename = video_title + download_as

    # Check if file already exists
    if filename in set(os.listdir(download_folder)):
        print("File already downloaded.")
        return

    try:
        if download_as == '.mp3':
            stream = video.streams.get_audio_only()
        elif download_as == '.mp4':
            stream = video.streams.get_highest_resolution()

        stream.download(output_path=download_folder, filename=filename)
        print(f"Downloaded {download_as}: {video_title}")
    except Exception as e:
        print(f"Error downloading {download_as} {video_title}: {str(e)}")


def main():
    url = input("Enter the URL of the video or playlist you want to download:")
    download_folder = input("Specify the directory path you'd like to use:")
    while not is_valid_directory(download_folder):
        print("The directory path you entered is not valid. Please try again.")
        download_folder = input("Specify the directory path you'd like to use:")
    download_as = input("You want to download as (.mp3) or (.mp4):")

    while True:
        if download_as != '.mp3' and download_as != '.mp4':
            print("Please enter the correct file extension")
            download_as = input("You want to download as (.mp3) or (.mp4):")
        else:
            break

    if 'playlist' in url:
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            video = YouTube(video_url)
            download_video(video, download_folder, download_as)
    else:
        video = YouTube(url)
        download_video(video, download_folder, download_as)

    print("Download complete")


def is_valid_directory(path):
    return os.path.isdir(path)


if __name__ == "__main__":
    main()
