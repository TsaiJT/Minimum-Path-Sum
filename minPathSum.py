def minPathSum(grid):

# calculate top row min path cost.
    for i in range(1, len(grid[0])):
        grid[0][i] = grid[0][i-1] + grid[0][i]

# calculate left col min path cost.
    for i in range(1, len(grid)):
        grid[i][0] = grid[i-1][0] + grid[i][0]

# find the minimum path according to the DP algorithm.
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[len(grid)-1][len(grid[0])-1]


def main():

    s = [[1,3,1],
         [1,5,1],
         [4,2,1]]       
    result = minPathSum(s)
    print(result)

if __name__ == '__main__':
    main()