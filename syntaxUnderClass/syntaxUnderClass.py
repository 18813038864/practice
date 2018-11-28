# -*- coding: utf-8 -*-

def printNum():
    i = 0
    # num = []
    # while i< len(range(10)):
    #     if i%2==0:
    #         num.append(i)
    #     i+=1

    num = [i for i in range(10) if i%2==0]
    print num


# printNum()

def printIndexAndEle():
    eles = ["asd","qeq","alice"]
    # i = 0
    # sed = {}
    # for ele in eles:
    #     sed[i] = ele
    #     i+=1
    sed = {}
    for i ,ele in enumerate(eles):
        sed[i] = ele

    print sed
#
# printIndexAndEle()
#
# from MyIterator import MyIterator
#
# for ele in MyIterator(4):
#     print ele

import generatorDemo

lis = [x*x for x in range(10)]
print(lis)
print next(generatorDemo.generator_ex)

for i in generatorDemo.generator_ex:
    print(i)

for i in generatorDemo.fib(6):
    print i

