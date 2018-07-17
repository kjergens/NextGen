from show import Show
from operator import attrgetter
from video import Video

show_list = list()

f = open("shows.txt", "r")

for line in f:
    data = line.split(",")
    v = Video()
    v.title = data[0]
    v.genre = data[1]
    v.year = int(data[2])
    #s = Show(data[0], data[1], int(data[2]))
    show_list.append(v)

f.close()

# 4 ways to sort
#show_list = sorted(show_list, key=repr)
#show_list.sort(key=repr)
#show_list.sort(key=lambda show: show.title)
show_list.sort(key=attrgetter('year', 'title', 'genre'), reverse=False)

for s in show_list:
    print(s)


