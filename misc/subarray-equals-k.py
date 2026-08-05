












import bisect
mylist = [1,2,3,4,5,6,6,8,9,10]



r = bisect.bisect_left(mylist, 5)

print(len(mylist))
print(r)
print(mylist[r])

