import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    datas = [next(reader)]
    for row in reader:
        if row:
            print(row)
            datas.append(row)

    datas.append(['jack', 'python', 100])
    with open('new_data.csv', 'w', encoding='utf-8', newline='') as f2:
        writer = csv.writer(f2)
        for row in datas:
            writer.writerow(row)
