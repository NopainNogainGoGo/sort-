
# 氣泡排序（Bubble Sort）
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] > list[j+1]: 
                list[j], list[j+1] = list[j+1], list[j]
    return list


# 選擇排序（Selection Sort）
def selection_sort(list):
    n =len(list)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if list[j]<list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]
    return list
    

# 插入排序（Insertion Sort）
def insertion_sort(list):
    n = len(list)
    for i in range(1,n):
        j = i
        while j > 0 and list[j-1] > list[j]:  
            list[j], list[j-1] = list[j-1], list[j]
            j = j-1
    return list
    
    
# 主程式：測試三種排序演算法
def main():
    list = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    print("Insertion Sort")
    print("Before:", list)
    print("After: ", insertion_sort(list[:]))   # 用 list[:] 可以避免改到原始陣列
    print("list", list)
    print()

    list = [3, 9, 2, 1]
    print("Selection Sort")
    print("Before:", list)
    print("After: ", selection_sort(list))
    print("list", list)
    print()

    list = [-93, 99, -2, -1]
    print("Bubble Sort")
    print("Before:", list)
    print("After: ", bubble_sort(list[:]))
    print()


main()