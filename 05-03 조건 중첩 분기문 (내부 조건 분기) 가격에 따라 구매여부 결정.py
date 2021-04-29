# 값 입력
flag = input('마음에 드는 옷을 찾았나요?(예/아니요):')

# 조건 분기
if flag == '예':
    print(':) 축하합니다!!')

    #가격 입력
    price = input('가격이 얼마인가요?:')

    #내부 조건 분기
    if int(price) <= 100000:  #정수형으로 형변환 시켜주기
        print(':) 구매합니다.')
    else: 
        print(':( 포기합니다.')


elif flag == '아니요':
    print(':( 아쉽군요.')
else:
    print("'예' 또는 '아니요'로만 입력하세요.")
