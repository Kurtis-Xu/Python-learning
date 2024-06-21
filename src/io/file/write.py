f = open('write.txt', 'w', encoding='utf-8')
for i in range(10): f.write(f'行 {i}\n')
f.close()
