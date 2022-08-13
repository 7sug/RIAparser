from database import get_connection


def data_correcting(data):
    temp = []
    data_to_insert = []
    for title, values in data.items():
        temp.clear()
        temp.append(title)
        temp += values
        data_to_insert.append(tuple(temp))
    print(data_to_insert)
    data_inserting(data_to_insert)


def data_inserting(data_to_insert):
    request = """insert into ria_parse (title, link, description, img) values (%s, %s, %s, %s)"""
    connection = get_connection.config_reader("D:\RIAparser\database\config.json")
    cursor = connection.cursor()
    for news in data_to_insert:
        print(news)
        cursor.execute(request, news)
    connection.commit()
    connection.close()
    print("Готово!")
