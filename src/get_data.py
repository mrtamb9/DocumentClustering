import my_connection, parameter, my_util
import pickle
from gensim.corpora import Dictionary


# query tokenizer from news table
# remove invalid token in a document
# save Dictionary (gensim) into text file
def get_data_tokenizer(fromdate, todate):
    print 'Starting get and save data from mysql-server ....'

    fromdate = fromdate + ' 00:00:00'
    todate = todate + ' 03:59:59'

    connection = my_connection.getConnection()
    cursor = connection.cursor()

    query = 'SELECT id, vntokenizer FROM news WHERE create_time BETWEEN ' + '\'' + fromdate + '\' AND \'' + todate + '\';'
    print query

    cursor.execute(query)
    rows = cursor.fetchall()
    count = 0

    token_dictionary = Dictionary()
    data = dict()

    for row in rows:
        id = row[0]
        tokenizer = row[1]
        tokenizer = tokenizer.lower()
        count += 1
        print count
        print tokenizer
        token_list = tokenizer.split(' ')
        valid_token_list = list()
        for token in token_list:
            if my_util.check_valid_token(token):
                valid_token_list.append(token)
        token_dictionary.add_documents([valid_token_list])
        data[id] = valid_token_list

    my_connection.closeConnection(connection)

    # save dictionary and data into text file
    token_dictionary.save_as_text('..' + parameter.FILE_DICTIONARY)
    fb = open('..' + parameter.FILE_DATA, 'wb')
    pickle.dump(data, fb)
    fb.close()

    print 'Done get and save data from mysql-server!'


def main():
    fromdate = '2016-09-07'
    todate = '2016-09-07'
    get_data_tokenizer(fromdate, todate)


if __name__ == '__main__':
    main()
