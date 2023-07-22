def leaderboard_sort(commits, data):
    for i in range(len(commits)):
        for j in range(len(commits) - 1):
            if commits[j] < commits[j + 1]:
                commits[j], commits[j + 1] = commits[j + 1], commits[j]
                data[j], data[j + 1] = data[j + 1], data[j]

    return data
