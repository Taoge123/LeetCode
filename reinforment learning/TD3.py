# Complete the playlist function below.
def playlist(songs):
    if not songs:
        return 0

    if len(songs) == 1:
        return 0

    curr = 0
    count = 0
    res = []

    return palylistUtil(songs, curr, count, res)


def palylistUtil(songs, curr, count, res):
    if curr > 0 and curr % 60 == 0:
        count += 1
        res.append(count)
        return count

    for i in range(len(songs)):
        curr += songs[i]

        palylistUtil(songs[1:], curr, count, res)

        curr -= songs[i]

    return len(res)

