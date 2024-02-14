N, K = map(int, input().split()) # N 전체 학생 수, K 방 수용인원
arr = [list(map(int, input().split())) for _ in range(N)] # 성별 / 학생 수

girl_cnt = [0] * 6
boy_cnt = [0] * 6

# 학년 별 cnt
for lst in arr:
    # 남학생인 경우
    if lst[0]:
        boy_cnt[lst[1]-1] += 1
    # 여학생인 경우
    else:
        girl_cnt[lst[1]-1] += 1

room_cnt = 0

# 성별 / 학년 별 방 개수 cnt
# 여학생
for num in girl_cnt:
    # 학생 수가 방 수용인원보다 많고 배수가 아닌 경우
    if num > K and num % K != 0:
        room_cnt += num // K + 1
    # 학생 수가 방 수용인원보다 많거나 같고 배수인 경우
    elif num >= K and num % K == 0:
        room_cnt += num // K
    # 학생 수가 0보다 크지만 방 수용인원보다 적은 경우
    elif 0 < num < K:
        room_cnt += 1
    # 학생 수가 0일 때
    else:
        pass

# 남학생
for num in boy_cnt:
    # 학생 수가 방 수용인원보다 많고 배수가 아닌 경우
    if num > K and num % K != 0:
        room_cnt += num // K + 1
    # 학생 수가 방 수용인원보다 많거나 같고 배수인 경우
    elif num >= K and num % K == 0:
        room_cnt += num // K
    # 학생 수가 0보다 크지만 방 수용인원보다 적은 경우
    elif 0 < num < K:
        room_cnt += 1
    # 학생 수가 0일 때
    else:
        pass

print(room_cnt)