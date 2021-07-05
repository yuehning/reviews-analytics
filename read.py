data = []
count = 0 #count用來記資料數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1 的快寫法
		if count % 1000 == 0: # %用來求餘數 EX 7 % 3 = 1 (7/3=1)
			print(len(data))


