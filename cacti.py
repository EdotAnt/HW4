def cacti_number(plot):
    n = len(plot)
    m = len(plot[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if plot[i][j] == 0:
                if (i == 0 or plot[i-1][j] != 1) and \
                   (j == 0 or plot[i][j-1] != 1) and \
                   (i == n-1 or plot[i+1][j] != 1) and \
                   (j == m-1 or plot[i][j+1] != 1) and \
                   (i == 0 or j == 0 or plot[i-1][j-1] != 1) and \
                   (i == 0 or j == m-1 or plot[i-1][j+1] != 1) and \
                   (i == n-1 or j == 0 or plot[i+1][j-1] != 1) and \
                   (i == n-1 or j == m-1 or plot[i+1][j+1] != 1):
                    count += 1
    return count
