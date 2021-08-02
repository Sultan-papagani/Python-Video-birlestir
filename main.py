import sys, os

if len(sys.argv) != 3:
    print(f"video sayisi iki olmalidir, gelen:{len(sys.argv)}")
    input()
    sys.exit()
    
video1 = sys.argv[1]
video2 = sys.argv[2]
name, extension = os.path.splitext(video1)
output = name + "FINAL" + ".mp4"

#ffmpeg -i %video1% -i %video2% -c:v copy -c:a aac %çıkışAd%
q = chr(34)
os.system(f"ffmpeg -i {q}{video1}{q} -i {q}{video2}{q} -c:v copy -c:a aac {q}{output}{q}")

input()
