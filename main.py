from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def name_corrector():
    for item in contacts_list:
        full_name= ' '.join(item[:3]).split(' ')
        #last_name=item[0].split(' ')
        #name=item[1].split(' ')
        #print(last_name[0])
        #print(last_name[1])
        #print(name[0])
        #print(item)
        #print(full_name)
        #out_list=[full_name[0],full_name[1],full_name[2]]
        item[0] = full_name[0]
        item[1] = full_name[1]
        item[2] = full_name[2]
        #print(out_list)
        #print(item[0],item[1],item[2])
        #print(item)
        #print(len(item))
def phone_corrector():
    for item in contacts_list[1:]:
        re_exp=   r'(\+7|8)?\s*?\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})[\s,]?\(?(доб.)?\s?(\d{4})?\)?'
                    #(\+7 | 8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?\(?(доб.\s\d{4})?\)?'
                    #(\+7|8)\s*?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})[\s*-]\(?(доб\.)*\s*(\d{4})?\)?

        sub = r'+7(\2)\3-\4-\5 \6\7'
        item[5] = re.sub(re_exp, sub, item[5])
        #print(item[5])

def data_aggregation():

    contacts_list[2].append('')
    for item in contacts_list:
        #print(item[5])
        first_name = item[0]
        last_name = item[1]
        for other_item in contacts_list:
            other_first_name = other_item[0]
            other_last_name = other_item[1]
            if first_name == other_first_name and last_name == other_last_name:
                if item[2] == '': item[2] = other_item[2]
                if item[3] == '': item[3] = other_item[3]
                if item[4] == '': item[4] = other_item[4]
                if item[5] == '': item[5] = other_item[5]
                if item[6] == '': item[6] = other_item[6]
    new_list = []
    for item in contacts_list:
        #pprint(len(item))
        if item not in new_list:
            new_list.append(item)
    return new_list



with open("phonebook_raw.csv", mode="r", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    #print(list(rows))
    contacts_list = list(rows)
    #pprint(contacts_list)
    #pprint(contacts_list[1][0])
    name_corrector()
    phone_corrector()
    #pprint(contacts_list)
    new_contacts_list=data_aggregation()

    #pprint(new_contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)