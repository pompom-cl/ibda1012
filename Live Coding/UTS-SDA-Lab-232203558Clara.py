'''
Ujian Tengah Semester
Struktur Data dan Algoritma
Semester Genap 2023/2024

Ujian Lab

NIM : 232203558
Nama: Clara Maria Lie

'''

import csv


def read_txt():
    bookL1 = []
    with open("bible_books.txt", "r", encoding='utf-8') as file:
        for row in file:
            bookL1.append(row.replace('\n', ''))
    return bookL1


def prepare_bible():  # bookL1 dari read_text()
    # bookL2 singkatan alkitab
    bibleD = {}
    bookL2 = []
    with open('lai_tb.csv', 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            book = row[1]
            if book not in bookL2:
                bookL2.append(book)
            chapter = row[2]
            verse = row[3]
            text = row[4]
            key = book + ' ' + chapter + ':' + verse
            valueList = [chapter, verse, text]
            bibleD[key] = valueList
    bookL1 = read_txt()
    tempL = zip(bookL2, bookL1)
    bookL = list(tempL)
    return bibleD, bookL


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[(len(arr) - 1) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def print_books(bookL, sortby):
    if sortby == 'A':
        bookL = quick_sort(bookL)
    else:
        bookL = bookL
    for i in range(0,len(bookL),3):
        line = ''
        for j in range(3):
            line += f"{bookL[i + j][0]} : {bookL[i + j][1]}".ljust(24, ' ')
        print(line)


def search_bible(bibleD, bookL, key):
    book = key[:3]
    colon_pos = key.index(':')
    chapter = key[4:colon_pos]
    verse = key[colon_pos + 1:]
    if key in bibleD:
        chp = bibleD[key][0]
        ver = bibleD[key][1]
        if chp == chapter and ver == verse:
            for short_name, long_name in bookL:
                if book == short_name:
                    full_name = long_name
                    print(f"{full_name} {chapter}:{verse}")
                    print(bibleD[key][2])
                    print()
                    break
        else:
            print(key)
            print('Not found!\n')
    else:
        print(key)
        print('Not found!\n')



def query_demo(bibleD, bookL):
    keyL = ('Kej 1:1', 'Yoh 3:16', 'Yoh 16:1', 'Mat 28:19', 'Mzm 119:1', 'Mzm 119:18', 'Mzm 119:105', 'Kej 100:100', 'Kisah 1:1')
    for key in keyL:
        search_bible(bibleD, bookL, key)
    print()


def bible_query(bibleD, bookL):
    while True:
        print("Search Bible")
        print('-' * 12)
        while True:
            sortby = input("Sort by (A)bjad atau (K)itab: ").upper()
            if sortby == 'A' or sortby == 'K':
                break
        print_books(bookL, sortby)
        print("\nMasukkan nama kitab, pasal dan ayat.")
        print("Contoh: Kej 1:1, Mzm 119:105")
        while True:
            print("\nKetik: 'x' untuk kembali ke menu utama.")
            query = input(">> ")
            if query == 'x':
                return
            elif ':' in query:
                search_bible(bibleD, bookL, query)
                input('Tekan Enter untuk melanjutkan ...')
            else:
                print('Masukkan ayat Alkitab')

def print_menu():
    print("CIT Simple Bible")
    print("-" * 16)
    print("1. QueryDemo    ")
    print("2. BibleQuery   ")
    print("0. Quit         ")

# main
bibleD, bookL = prepare_bible()
while True:
    print_menu()
    choice = input("\nEnter choice (0-2): ")
    if (choice == '1'):
        query_demo(bibleD, bookL)
    elif (choice == '2'):
        bible_query(bibleD, bookL)
    elif (choice == '0'):
        print("Thank you")
        break
    else:
        print("Invalid choice")