from os import listdir

print(Input the path of the music files:)

path = input()

'C:\\GOG Games\Hearts of Iron III\musicmod'

f = open(path + "\songs.txt","w+")

files = listdir(path)

mp3 = [s for s in files if s.endswith('.mp3')]

for file in mp3:
    f= open(path + "\songs.txt","a")
    f.write('song ={ \n name = '+ file +' \n\n chance = { \n      modifier = { \n           factor = 2 \n                 } \n          } \n      }\n \n')
    f.close()
    print(file + ' added')