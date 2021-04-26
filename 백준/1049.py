n , m = map(int, input().split())

min_pack = 1000
min_piece = 1000
for _ in range(m) : # 최소패키지 값과 최소 낱개 값을 찾아준다.
    pack, piece = map(int, input().split())
    if pack < min_pack :
        min_pack = pack
    if piece < min_piece :
        min_piece = piece

price = 0
if min_piece*6 <= min_pack: # 최소낱개6개합이 최소 패키지합보다 작으면 바로 낱개로만
    price = n*min_piece
elif n%6*min_piece >= min_pack : # 위의 경우가 아닐때, 6개묶음으로 다 사고 6개 이하의
                                  # ㄴ 낱개개수*최소낱개가격 > 최소패키지가격일때
    price = (n//6)*min_pack + min_pack
elif n%6*min_piece < min_pack : # 6개이하의 낱개개수*최소 낱개가격 < 최소 패키지 가격
    price = (n//6)*min_pack + (n%6)*min_piece 

print(price)
