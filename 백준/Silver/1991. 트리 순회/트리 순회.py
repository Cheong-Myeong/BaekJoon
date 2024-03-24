def preorder(key):
    if key == '.':
        return
    print(key, end='')
    preorder(dic[key][0])
    preorder(dic[key][1])

def inorder(key):
    if key == '.':
        return
    inorder(dic[key][0])
    print(key, end='')
    inorder(dic[key][1])

def postorder(key):
    if key == '.':
        return
    postorder(dic[key][0])
    postorder(dic[key][1])
    print(key, end='')


N = int(input())
dic = {}
for _ in range(N):
    node, left, right = map(str, input().split())
    dic[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')