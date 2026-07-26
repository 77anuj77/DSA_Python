names=["anuj", "anuj", "anuj", "rushikesh", "rushikesh" , "chirayu", "anadi","anadi"]
def clean(names):
    left=0
    for right in range(1, len(names)):
        if (names[left]!=names[right]):
            left+=1
            names[left]=names[right]
    return left + 1
count=clean(names)
print(names[:count])

'''
same name? right moves, left stays, Register chanfe does not
different name? left forward, new name copy left new spot'''