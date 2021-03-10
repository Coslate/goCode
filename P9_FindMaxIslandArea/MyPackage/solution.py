from __future__ import print_function
import sys
import math
import queue
from collections import deque

def printList(nums):
    length = len(nums)

    if(length == 1):
        print(f'[{nums[0]}]')
        return

    for i in range(length):
        if(i == 0):
            print(f"[{nums[i]}", end='')
        elif(i == (length-1)):
            print(f" {nums[i]}]")
        else:
            print(f" {nums[i]}", end='')

class Solution:

    # @param grid: List[List[int]]
    # @return int
    def findMaxIslandArea(self, grid):
        # Implement me
        # Calculate the length and width
        width  = len(grid)
        length = len(grid[0])
        max_area = 0
        already_visited = []
        print("length = {}, width = {}".format(length, width))
        for i in range(width):
            list_loc = []
            for j in range(length):
                list_loc.append(0)
                #print("already_visited[{}][{}] = {}".format(i, j, already_visited[i][j]))
            already_visited.append(list_loc)

#        for i in range(width):
#            for j in range(length):
#                print("already_visited[{}][{}] = {}".format(i, j, already_visited[i][j]))

        for i in range(width):
            for j in range(length):
                if(grid[i][j] == 1):
                    cal_area = self.runIterativeDFS(grid, i, j, already_visited, width, length)
                    if(cal_area > max_area):
                        max_area = cal_area

        return max_area

    def runIterativeDFS(self, grid, start_i, start_j, already_visited, width, length):
        if(already_visited[start_i][start_j] == 1):
            return -1

        cal_area = 0
        stack = [(start_i, start_j)]
        while(len(stack) != 0):
            top_pos_i, top_pos_j = stack[-1]
            stack.pop()

            if(already_visited[top_pos_i][top_pos_j] == 0):
                already_visited[top_pos_i][top_pos_j] = 1
                cal_area += 1

            #check neighboor
            up_pos   = (top_pos_i-1, top_pos_j)
            down_pos = (top_pos_i+1, top_pos_j)
            right_pos= (top_pos_i, top_pos_j+1)
            left_pos = (top_pos_i, top_pos_j-1)
            if(up_pos[0] >= 0 and already_visited[up_pos[0]][up_pos[1]]== 0 and grid[up_pos[0]][up_pos[1]] == 1):
                stack.append(up_pos)

            if(down_pos[0] < width and already_visited[down_pos[0]][down_pos[1]]== 0 and grid[down_pos[0]][down_pos[1]] == 1):
                stack.append(down_pos)

            if(right_pos[1] < length and already_visited[right_pos[0]][right_pos[1]]== 0 and grid[right_pos[0]][right_pos[1]] == 1):
                stack.append(right_pos)

            if(left_pos[1] >= 0 and already_visited[left_pos[0]][left_pos[1]]== 0 and grid[left_pos[0]][left_pos[1]] == 1):
                stack.append(left_pos)

        return cal_area







