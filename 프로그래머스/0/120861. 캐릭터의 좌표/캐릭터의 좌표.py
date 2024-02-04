def solution(keyinput, board):
       # 왼, 오, 위, 아래
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    answer = [0, 0]
    
    for key in keyinput:
        if key == 'left':
            if -(board[0]//2) <= answer[0] + di[0] <= (board[0]//2):
                answer[0] += di[0]
        if key == 'right':
            if -(board[0]//2) <= answer[0] + di[1] <= (board[0]//2):
                answer[0] += di[1]
        if key == 'up':
            if -(board[1]//2) <= answer[1] + dj[2] <= (board[1]//2):
                answer[1] += dj[2]
        if key == 'down':
            if -(board[1]//2) <= answer[1] + dj[3] <= (board[1]//2):
                answer[1] += dj[3]
    return answer        