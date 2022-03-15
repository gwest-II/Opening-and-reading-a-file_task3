
with open("1.txt", encoding='utf-8') as f1, open("2.txt", encoding='utf-8') as f2,\
        open("3.txt", encoding='utf-8') as f3:
    file_1 = f1.readlines()
    file_2 = f2.readlines()
    file_3 = f3.readlines()
    files_unsorted = {"1.txt": file_1, "2.txt": file_2, "3.txt": file_3}
    files_sorted = sorted(files_unsorted, key=lambda key: len(files_unsorted[key]))
    print(files_sorted)

with open('result.txt', 'w', encoding='utf-8') as f:
    for item in files_sorted:
        f.write(f"{item}\n{len(files_unsorted[item])}\n {''.join(files_unsorted[item])}\n")
