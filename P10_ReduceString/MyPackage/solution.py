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

    # @param s: str
    # @return str
    def reduceStringStack(self, s):
        # Implement me
        stack = []
        length = len(s)
        new_s = ""

        for i in range(length):
            if(len(stack) == 0):
                stack.append(s[i])
            elif(self.isNeighbor(s[i], stack[-1])):
                stack.pop()
            else:
                stack.append(s[i])

        for i in range(len(stack)):
            new_s += stack[i]

        return new_s


    def reduceStringNaive(self, s):
        # Implement me
        length = len(s)
        m_i = 0
        m_j = 0
        new_s_list = []
        new_s = ""
        get_change = True
        for i in range(length):
            new_s_list.append(s[i])

        while(get_change):
            get_change = False
            for i in range(length):
                if(new_s_list[i] == '-'):
                    continue
                for j in range(i+1, length):
                    if(new_s_list[j] == '-'):
                        continue
                    if(self.isNeighbor(new_s_list[i], new_s_list[j])):
                        new_s_list[i] = '-'
                        new_s_list[j] = '-'
                        get_change = True
                        break
                    else:
                        break

        for i in range(len(new_s_list)):
            if(new_s_list[i] != '-'):
                new_s += new_s_list[i]

        return new_s

    def isNeighbor(self, char1, char2):
        if((char1 == "A" and char2 == "B") or (char1 == "B" and char2 == "A")):
            return True
        elif((char1 == "C" and char2 == "D") or (char1 == "D" and char2 == "C")):
            return True
        else:
            return False

