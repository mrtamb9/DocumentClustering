# coding=utf-8
# load dictionary and news that saved in local folder ../data/
import parameter
import pickle
from gensim.corpora import Dictionary


def read_token_dictionary():
    token_dictionary = Dictionary.load_from_text('..' + parameter.FILE_DICTIONARY)
    return token_dictionary


def read_content():
    rb = open('..' + parameter.FILE_DATA, 'rb')
    data = pickle.load(rb)
    rb.close()
    return data


def read_data():
    print 'Starting reload data from local folder ....'

    id_df_dict = dict()
    newsid_content_dict = dict()

    token_dictionary = read_token_dictionary()
    token_id_dict = token_dictionary.token2id
    token_df_dict = token_dictionary.dfs
    for token in token_id_dict:
        id = token_id_dict[token]
        df = token_df_dict[id]
        id_df_dict[id] = df

    ids_contents_dict = read_content()
    for newsid in ids_contents_dict:
        content = ids_contents_dict[newsid]
        temp_dict = dict()
        for token in content:
            id = token_id_dict[token]
            if id in temp_dict:
                temp_dict[id] += 1
            else:
                temp_dict[id] = 1
        newsid_content_dict[newsid] = temp_dict

    print 'Done reload data!'
    return (id_df_dict, newsid_content_dict)


def main():
    read_data()


if __name__ == '__main__':
    main()
