# coding=utf-8

VN_STR = ['_', u'a', u'b', u'c', u'd', u'e', u'f', u'g', u'h', u'i', u'j', u'k', u'l', u'm', u'n', u'o', u'p', u'q', u'r',
          u's', u't', u'u', u'v', u'w', u'x', u'y', u'z', u'á', u'à', u'ả', u'ã', u'ạ', u'ă', u'ắ', u'ặ', u'ằ', u'ẳ',
          u'ẵ', u'â', u'ấ', u'ầ', u'ẩ', u'ẫ', u'ậ', u'đ', u'é', u'è', u'ẻ', u'ẽ', u'ẹ', u'ê', u'ế', u'ề', u'ể', u'ễ',
          u'ệ', u'í', u'ì', u'ỉ', u'ĩ', u'ị', u'ó', u'ò', u'ỏ', u'õ', u'ọ', u'ô', u'ố', u'ồ', u'ổ', u'ỗ', u'ộ', u'ơ',
          u'ớ', u'ờ', u'ở', u'ỡ', u'ợ', u'ú', u'ù', u'ủ', u'ũ', u'ụ', u'ư', u'ứ', u'ừ', u'ử', u'ữ', u'ự', u'ý', u'ỳ',
          u'ỷ', u'ỹ', u'ỵ']

def check_valid_character(char):
    if char in VN_STR:
        return True
    return False

def check_valid_token(token):
    for index in range(len(token)):
        char = token[index]
        if not check_valid_character(char):
            return False
    return True

def get_vector(token_dictionary, document):
    pass