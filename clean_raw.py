import glob, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= 'path to a JPG/JPEG directory')
args = parser.parse_args()

if args.path is not None:
    os.chdir(args.path)

cwd = os.getcwd()
print("Working directory: {}".format(cwd))

jpgs = set()
for file in glob.glob("*"):
    if (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg")):
        jpgs.add(file.split('.')[0])

if (len(jpgs) == 0):
    print("No images (JPG, JPEG) were found. Please run on a different directory or specify --path as an argument.")
    raise SystemExit

print("{} JPG/JPEG images found".format(len(jpgs)))
# print(", ".join(str(e) for e in jpgs))

del_cnt = 0
size_cnt = 0
for file in glob.glob("*"):
    if (file.lower().endswith(".cr2") and file.split('.')[0] not in jpgs):
        del_cnt += 1
        size_cnt += os.stat(file).st_size >> 20
        os.remove(file)

print("{} raw files removed. {}MB freed up.".format(del_cnt, size_cnt))