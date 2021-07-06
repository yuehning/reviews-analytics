data = []
count = 0 #count用來記資料數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1 的快寫法
		if count % 1000 == 0: # %用來求餘數 EX 7 % 3 = 1 (7/3=1)
			print(len(data))
print('檔案讀取完畢, 總共有', len(data),'筆資料' )

sum_len = 0 #預設留言總字數為0
for d in data: # d 表示每筆留言
	sum_len = sum_len + len(d) 
	# EX: 總數(10) = 總數(0)[預設0] + Len(0) [第零筆留言有10個字]
	#     總數(30) = 總數(10) + Len(1) [第一筆留言有20個字]..............以此類推算全部留言的字數
print('每筆留言的平均字數為', sum_len/len(data))	

new = [] # 新清單，裝字數小於100的留言
for d in data:
	if len(d) < 100: # 如果該筆留言自小於100
		new.append(d) # 就裝入新的清單內
print('字數小於100的留言共有', len(new), '筆')
print(new[0])