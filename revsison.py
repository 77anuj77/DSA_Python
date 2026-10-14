class Sort:
    def __init__(self):
        pass
    def Selection_sort(self, array: list[int]):
        n=len(array)
        for i in range(0, n):
            minIndex=i
            for j in range(i+1, n):
                if array[j]<array[minIndex]:
                    minIndex=j

            array[i], array[minIndex]= array[minIndex], array[i]

        return array

    def Bubble_sort(self, array: list[int]):

        n=len(array)
        for i in range(n-2, -1,-1):
            for j in range(0, i+1):
                if array[j]>array[j+1]:
                    array[j], array[j+1]= array[j+1], array[j]
        return array

    def Insertion_sort(self, array: list[int]):
        n=len(array)
        for i in range(1,n):
            key=array[i]
            j=i-1
            # while j <= i and array[j]<key:
            #     j += 1

            # del array[i]
            # array = array[:j] + [key] + array[j:]
            while j>=0 and array[j]>key:
                array[j+1]=array[j]
                j-=1

            array[j+1]=key
        return array

class Best_Sort:
    def __init__(self):
        pass


    def Quick_sort(self,array:list[int]):
        def partion(array: list[int], low, high):
            i= low
            j= high
            pivot= array[low]

            while i<j:
                while array[i]<=pivot and i<high-1:
                    i+=1
                while array[j]>pivot and j< low+1:
                    j-=1
                if i< j:
                    array[i], array[j]= array[j], array[i]
            array[pivot], array[j]= array[j], array[pivot]

            return j

        def Quick(array, low , high):
            while low < high:
                partion_index=partion(array, low, high)
                Quick(array, low, partion_index-1)
                Quick(array, partion_index+1, high)

        
    
    def Merge_Sort(self, array: list[int]):
        def merge_sorted(left, right):
            i,j=0,0
            m,n=len(left), len(right)
            result=[]
            while i<m and j<n:
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else :
                    result.append(right[j])
                    j+=1
            if i<m:
                result+=left[i:]
            if j<n:
                result+=right[j:]
            return result
        
        def merge(array: list[int]):
            if len(array)<=1:
                return array
            
            n=len(array)//2
            left= merge(array[:n])
            right= merge(array[n:])
            
            return merge_sorted(left, right)
        
        return merge(array)

obj= Sort()
obj1=Best_Sort()
print(obj.Selection_sort([2,4,1,5,7]))
print(obj.Bubble_sort([2,4,1,5,7]))
print(obj.Insertion_sort([2,4,1,5,7]))
print(obj1.Merge_Sort([2,4,1,5,7]))