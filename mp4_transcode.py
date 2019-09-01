import glob, os, argparse, subprocess

def get_mp4_files(directory):
    mp4s = set()
    
    for file in glob.glob(os.path.join(directory,"*")):
        if (file.lower().endswith(".mp4") and "converted" not in file.lower()):
            mp4s.add(file)
    
    return mp4s

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help= 'path to a MP4 directory')
    args = parser.parse_args()

    if args.path is not None:
        os.chdir(args.path)

    cwd = os.getcwd()
    print("Working directory: {}".format(cwd))

    mp4s = get_mp4_files(cwd)
    if (len(mp4s) == 0):
        print("No MP4 vids were found. Please run on a different directory or specify --path as an argument. Exiting.")
        raise SystemExit
    print("{} MP4 files found".format(len(mp4s)))

    # subprocess.call(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", "-I", "dummy", "--sout=#transcode{vcodec=h264,vb=1024,acodec=mp4a,ab=192,channels=2,deinterlace}:standard{access=file,mux=ts,dst=MyVid.mp4}", "vlc://quit"])

if __name__ == "__main__":
    main()