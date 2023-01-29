def print_data(data):
    if len(data) > 0:
        print("ID".center(5), "Имя".center(10), "Фамилия".center(10), "Телефон".center(15), "Комментарий".center(20))
        print("-"*130)
        for item in data:
            print(item[0].center(5), item[1].center(10), item[2].center(10), item[3].center(15), item[4].center(20))
    else:
        print("Справочник пуст!")