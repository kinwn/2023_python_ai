import numpy as np

sale = open('sales.txt','r', encoding= 'utf-8')
total = 0
a = sale.readlines()

for i in a:
    i = i.strip("\n")     # \n까지 넣어서 저장할 수는 없으므로 strip써서 삭재
    total +=int(i)

b = open("summary.txt","w",encoding="utf-8")
b.write("총 매출: %d \n" %total)
b.write("평균 일 매출: %.1f" %(total/5))  # 0.1f로 소수점 줄이기 이거 유의하기



