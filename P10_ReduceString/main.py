#! /usr/bin/env python3.6

from MyPackage import solution
import argparse

#Q.
'''
這道題目曾出現在 DRW 的面試中。

將 input string 根據以下 transition rules 轉態，直到無法再轉態為止。此 string 只會存在 "A"，"B"，"C" 或 "D" 四種字元。

Rule 1：若 "A" 和 "B" 相鄰，轉態為 empty string
Rule 2：若 "C" 和 "D" 相鄰，轉態為 empty string
時間複雜度要求為 O(n)

Example 1:
Input: "CABADCBD"
Output: ""
Explanation: "CABADCBD" -> "CADCBD" -> "CABD" -> "CD" -> ""

Example 2:
Input: "ACBD"
Output: "ACBD"
Explanation: "A" 和 "B" 以及 "C" 和 "D" 均沒有相鄰，無法轉態
'''

#########################
#     Main-Routine      #
#########################
def main():
    method = ArgumentParser()
    sol = solution.Solution()

#Example1
    input_str = "CABADCBD"
    print("input_str = {}".format(input_str))

    if(method == 1):
        print("> Use naive method...")
        ans = sol.reduceStringNaive(input_str)
    else:
        print("> Use stack method...")
        ans = sol.reduceStringStack(input_str)

    print(f'Example1 answer : {ans}')
    print(f'------------------------------------------------------')

#Example1
    input_str = "ACBD"
    print("input_str = {}".format(input_str))

    if(method == 1):
        print("> Use naive method...")
        ans = sol.reduceStringNaive(input_str)
    else:
        print("> Use stack method...")
        ans = sol.reduceStringStack(input_str)

    print(f'Example1 answer : {ans}')
    print(f'------------------------------------------------------')

#########################
#     Sub-Routine       #
#########################
def ArgumentParser():
    method                 = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", "-method", help="1: Use naive method, O(n^2). 0: Use stack method, O(n). Default is 0.")

    args = parser.parse_args()
    if args.method:
        method = int(args.method)

    return method

#-----------------Execution------------------#
if __name__ == '__main__':
    main()
