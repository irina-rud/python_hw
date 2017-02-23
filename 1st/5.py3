import no_standard_sort
import sys

def quick_sort(l):
    quick_sort_r(l, 0, len(l) - 1)

def quick_sort_r(l , first, last):
    if last > first:
        pivot = partition(l, first, last)
        quick_sort_r(l, first, pivot - 1)
        quick_sort_r(l, pivot + 1, last)
        
def partition(l, first, last):
    mid = (first + last)//2
    if l[first] > l[mid]:
        l[first], l[mid] = l[mid], l[first]  
    if l[first] > l[last]:
        l[first], l[last] = l[last], l[first]  
    if l[mid] > l[last]:
        l[mid], l[last] = l[last], l[mid]    
    l[mid], l[first] = l[first], l[mid]    
    pivot = first
    i = first + 1
    j = last
  
    while True:
        while i <= last and l[i] <= l[pivot]:
            i += 1
        while j >= first and l[j] > l[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            l[i], l[j] = l[j], l[i] 
    l[j], l[pivot] = l[pivot], l[j] 
    return j
        
line  = sys.stdin.readline()
vector = list(map(int, line.split()))
        
if len(vector) == 0:
    print("")
else:
    quick_sort(vector)
    s = ''
    for el in vector:
        s += str(el) +" "
    print(s[:-1])
