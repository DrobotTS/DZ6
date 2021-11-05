# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)

# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt) и
# возвращает их в виде списка строк (названия возвращать без точки).

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt) и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает списоксловарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]

import os
from datetime import datetime

def dom_par():
    with open("/Users/mazzhura/Desktop/domains.txt", "r") as domains:
        data = domains.read().replace(".", "").splitlines()
    return data

print(dom_par())

def name_par():
    with open("/Users/mazzhura/Desktop/names.txt", "r") as names:
        surname = [name.split("\t")[1] for name in names.readlines()]
    return surname

print(name_par())

def authors_par():
    context = open("/Users/mazzhura/Desktop/authors.txt", "r").read();
    dates = context.split("\n");
    num = 0;
    while (num < len(dates)):
        if (" - " in dates[num]):
            dates[num] = dates[num].split(" - ")[0].split(' ');
            dates[num][0] = dates[num][0].replace("th", "").replace("st", "").replace("nd", "").replace("rd", "");
            dates[num] = " ".join(dates[num]);
            num += 1;
        else:
            dates.pop(num);

    return [{"date_original": date, "date_modified": datetime.strptime(date, "%d %B %Y").strftime("%d/%m/%Y")} for date
            in dates];

print(authors_par())
