import sys
sys.setrecursionlimit(10**6)
tree = []

def postOrder(arr):
    if len(arr) == 1: 
        print(arr[0])
        return
    tmp_left, tmp_right = [], []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]: tmp_left.append(arr[i])
        else: tmp_right.append(arr[i])
    if tmp_left: postOrder(tmp_left)
    if tmp_right: postOrder(tmp_right)
    postOrder([arr[0]])
         
while True:
    try: tree.append(int(sys.stdin.readline()))
    except: break
    
postOrder(tree)
