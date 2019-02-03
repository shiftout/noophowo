import glob, os, argparse

def get_jpg_files(directory):
    jpgs = set()
    
    for file in glob.glob(os.path.join(directory,"*")):
        if (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg")):
            jpgs.add(file)
    
    return jpgs

def get_cr2_files(directory):
    cr2s = set()
    
    for file in glob.glob(os.path.join(directory,"*")):
        if (file.lower().endswith(".cr2")):
            cr2s.add(file)
    
    return cr2s

def move_raw_files(src_dir, dest_dir):
    cnt = 0
    for file in get_cr2_files(src_dir):
        base = os.path.basename(file)
        
        dest_file = os.path.join(dest_dir, base)
        if os.path.exists(dest_file):
            os.remove(dest_file)
        
        os.rename(file, dest_file)
        cnt += 1

    return cnt

def remove_orphan_raw_files(jpg_dir, raw_dir):
    
    jpgnames = set()
    for file in get_jpg_files(jpg_dir):
        base = os.path.basename(file)
        jpgnames.add(base.split('.')[0])

    cnt = 0
    for file in get_cr2_files(raw_dir):
        base = os.path.basename(file)
        if base.split('.')[0] not in jpgnames:
            os.remove(file)
            cnt += 1
    
    return cnt  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help= 'path to a JPG/JPEG directory')
    args = parser.parse_args()

    if args.path is not None:
        os.chdir(args.path)

    cwd = os.getcwd()
    print("Working directory: {}".format(cwd))

    jpgs = get_jpg_files(cwd)
    if (len(jpgs) == 0):
        print("No images (JPG, JPEG) were found. Please run on a different directory or specify --path as an argument. Exiting.")
        raise SystemExit
    print("{} JPG/JPEG files found".format(len(jpgs)))

    raw_dir = os.path.join(cwd, "raw")
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)
        print("Directory created {}".format(raw_dir))
    
    print("{} raw files moved".format(move_raw_files(cwd, raw_dir)))
    print("{} orphan raw files removed".format(remove_orphan_raw_files(cwd, raw_dir)))

if __name__ == "__main__":
    main()