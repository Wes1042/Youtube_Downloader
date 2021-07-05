import pytube , os 


print("This program will search youtube videos and downlaod them as MP3 files!!")
while True:
    print("Paste your Youtube URL so that it converts to a MP3...")
    url = input()



    youtube = pytube.YouTube(url)
    print("Step 1 Complete!")
    video = youtube.streams.filter(only_audio = True).first()

    print(" Enter the destination path or leave blank to save in the directory this program is located in ")
    destination = input(">> ") or './Music'

    out_file = video.download(output_path=destination)
    print("Step 2 Complete!")
    base ,ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file,new_file)
    print("Step 3 Complete!")
    print(youtube.title + " Has successfully downloaded!!!")


    
    if input("Want to download another song? (Y/N)") == 'n':
        break

    ## Refrence
    ## https://dev.to/seijind/how-to-download-youtube-videos-in-python-44od
    ##https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/
    ##https://stackoverflow.com/questions/41365922/how-do-i-repeat-the-program-in-python