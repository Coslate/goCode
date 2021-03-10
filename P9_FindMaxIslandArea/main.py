#! /usr/bin/env python3.6

from MyPackage import solution
import argparse

#Q.
'''
這道題目曾出現在 Google 的面試中。

給定一個海盜地圖 grid，地圖中有海洋和島嶼，找出該地圖中面積最大的島嶼，並 return 其面積。若地圖中沒有島嶼，則 return 0。

海盜地圖 grid 是一個只存在 0 或 1 的 2D array，其中 0 代表海洋，1 代表陸地
島嶼是由相鄰陸地所組成的區塊，相鄰陸地的定義為兩陸地接壤於 "上下左右" 其中一個方向
島嶼的面積定義為該島嶼擁有的陸地個數
假設 grid 的邊界均為海洋
Example 1:

Input: grid = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 1]]
Output: 4
Explanation: 地圖中存在 3 個島嶼，其面積分別為 4，2，及 1。最大面積為 4，因此 return 4。
Example 2:

Input: grid = [
    [0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0]]
Output: 10
Explanation: 地圖中存在 2 個島嶼，其面積均為 10，因此 return 10。
'''

#########################
#     Main-Routine      #
#########################
def main():
    method = ArgumentParser()
    sol = solution.Solution()
#Example1
    grid = [
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [1, 0, 1, 1]]

    print("grid = ")
    for i in grid:
        for x in i:
            print(" {}".format(x), end = '')
        print("")

    sum_ans = sol.findMaxIslandArea(grid)
    print(f'Example1 answer : {sum_ans}')
    print(f'------------------------------------------------------')

#Example2
    grid = [
        [0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0]]

    print("grid = ")
    for i in grid:
        for x in i:
            print(" {}".format(x), end = '')
        print("")

    sum_ans = sol.findMaxIslandArea(grid)
    print(f'Example1 answer : {sum_ans}')
    print(f'------------------------------------------------------')

#########################
#     Sub-Routine       #
#########################
def ArgumentParser():
    method                 = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", "-method", help="1: Use DP method, O(n^2). 0: Use prefix method, O(n). Default is 0.")

    args = parser.parse_args()
    if args.method:
        method = int(args.method)

    return method

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
