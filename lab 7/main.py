# Розробити програму, яка: а) створює текстовий файл TF19_1 із символьних рядків різної довжини, слова в яких розділені пробілами (одним або декількома);
# б) читає вміст файла TF19_1, вилучає в кожному рядку всі слова з однієї букви та зайві пробіли і записує їх у файл TF19_2;
# в) читає вміст файла TF19_2 і друкує його по рядках.

def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "TF19_1.txt"
file2_name = "TF19_2.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):
    file_1_w.write("Today, a crocodile a bird fell i onto the b plane.")
    print("Information was successfully added to TF19_1.txt!")
    file_1_w.close()
    print("File TF19_1.txt was closed!")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r != None and file_2_w != None:

    original_text = file_2_r.read()
    all_words = original_text.split()

    filtered_words = []

    for word in all_words:
        if len(word) == 1:
            filtered_words.append(word)

    clean_text = " ".join(filtered_words)
    file_2_w.write(clean_text)

    file_2_r.close()
    file_2_w.close()
    print("Files were closed!")

print("New sequence:")
file_3_r = Open(file2_name, "r")

if file_3_r != None:
    for line in file_3_r.read().split():
        print(line)
    print("File TF19_2.txt was closed!")

    file_3_r.close()