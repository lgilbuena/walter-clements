def sorting(L):
    sortedList = list()

    for x in L:
        highest = L[0]
        for y in L:
            if int(y[1]) > int(highest[1]):
                highest = y
        sortedList.append(highest)
        L.remove(highest)
        if len(L) == 1:
            sortedList.append(L[0])
            pass
 
    return sortedList
def formats(L):
    textForm = "Uwucoin leaderboard\n"
    numUsers = len(L)
    count = 1
    rank = 1
    for x in range(len(L)):
        if count == 1:
            textForm += "{}. {} ({} uwucoins)\n".format(rank,L[x][0],L[x][1])
        else:
            if int(L[x][1]) == int(L[x-1][1]):
                textForm += "{}. {} ({} uwucoins)\n".format(rank,L[x][0],L[x][1])
                rank += 1
            else:
                rank += 1
                textForm += "{}. {} ({} uwucoins)\n".format(rank,L[x][0],L[x][1])
        count += 1

    return textForm

