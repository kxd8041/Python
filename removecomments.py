"""
Given a piece of code, the task is to remove all the comments from the code. The code is given in a single line. Newline characters are used only to end the single line comments starting with //

Comments formats can be " /*...*/ " and " //... \n".

Comments cannot be nested.

Input: The first line of the input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing a piece of code which may or may not have comments.

Output: Corresponding to each test case, output a single line contaning the code without comments.

Note: Single line comments should be removed including the newline character in the end.

Constraints: 4 < |code| < 100000

Example:
INPUT:
2
#include int main(int argc,char *argv){ // First line of code\n printf("Hello World!!! "); return 0; }
#include int main(int argc,char argv){ / First line of code Printing Hello World */ printf("Hello World!!! "); return 0; }

OUTPUT:
#include int main(int argc,char *argv){  printf("Hello World!!! "); return 0; }
#include int main(int argc,char *argv){  printf("Hello World!!! "); return 0; }
"""

def removecomments(s):
    f = ''
    i = 0
    while i < len(s) - 1:
        l = 0
        if (s[i] == '/' and s[i + 1] == '*'):
            while (l == 0):
                if (s[i] == '*'):
                    if (s[i + 1] == '/'):
                        l = 1;
                i = i + 1

            i = i + 1
        l = 0
        if (s[i] == '/' and s[i + 1] == '/'):
            while (l == 0):
                if s[i] == '\\':
                    if (s[i + 1] == 'n'):
                        l = 1
                i = i + 1

        else:
            f = f + s[i]
            i = i + 1
    if (i == len(s) - 1):
        f = f + s[len(s) - 1]
    print f

n = int(raw_input("Please enter the number of Test cases:"))

for i in range(0,n):
    s = str(raw_input("Please enter the code:"))
    removecomments(s)


