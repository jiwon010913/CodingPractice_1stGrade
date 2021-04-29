hap, i = 0, 0 #변수 초기화

for i in range(1, 101, 2):      #1부터 101까지 2칸씩 증가
    hap += i                    #hap= hap + i

    if hap >= 1000:
        break

print("1~100의 홀수의 합에서 최초로 1000이 넘는 위치: %d" %(i))
