from collections import deque

def bfs(start):
    q = deque()
    deque.append(q, start)

    while q:
        now = deque.popleft(q)
        visited[now] = 1

        for i in adjl[now]:  # 현재 노드와 연결된 노드 모두 뽑기
            if visited[i] == 0:
                dic[i] = now  # 연결된 노드의 부모는 현재 노드임
                deque.append(q, i)

N = int(input())
adjl = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    adjl[s].append(e)  # 무방향이라서
    adjl[e].append(s)  # 양쪽에서 입력
visited = [0] * (N+1)
dic = {}  # key: 노드, value: 루트
bfs(1)    # 루트 1부터 시작
for num in range(2, N+1):
    print(dic[num])