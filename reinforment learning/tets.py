def playlist(songs):

    res = []

    palylistUtil(songs, 0, [], res)
    return res


def palylistUtil(songs, count, path, res):
    if  < 0:
        return  # backtracking
    if target % 60 == 0:
        res.append(path)
        return
    for i in range(index, len(songs)):
        palylistUtil(songs, i, path + [songs[i]], res)


songs = [10, 50, 90, 30]
playlist(songs, 60)
