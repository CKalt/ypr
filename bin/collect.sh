!/bin/bash
rm all.ydl
for i in *.ydl; do echo ---------- >> all.ydl; echo $i >> all.ydl; echo ---------- >> all.ydl; cat $i >> all.ydl; done
