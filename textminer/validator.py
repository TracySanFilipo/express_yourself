import re


def binary(list_numbers):
    return re.search(r"^[01]+$", list_numbers)


def binary_even(list_n):
    return re.search(r"^[01]+0$", list_n)


def hex(list_letternumber):
    return re.search(r"^[0-9A-Fa-f]+$", list_letternumber)


def word(check_word):
    return re.search(r"^[0-9a-zA-Z]+\-?[a-zA-Z]+$|^[a-zA-Z]+$", check_word)


def words(wordm, **kwargs):
    if len(kwargs) == 0:
        return re.findall(r"\b[0-9a-zA-Z]+\-?[a-zA-Z]+\b|\b[a-zA-Z]+\b", wordm)
    else:
        allw = re.findall(r"\b[0-9a-zA-Z]+\-?[a-zA-Z]+\b|\b[a-zA-Z]+\b", wordm)
        if len(allw) == kwargs['count']:
            return allw
        else:
            return None


def phone_number(phnum):
    return re.findall(r"^\(?\d{3}\)?\s?\-?\.?\d{3}\s?\-?\.?\d{4}$", phnum)


def money(mon):
    return re.search(r"^\$\d+$|^\$\d+\.\d\d$|^\$\d+\,\d{3}$|^\$\d+\,\d{3}\.\d\d$|^\$\d+\,\d{3}\,\d{3}$|^\$\d+\,\d{3}\,\d{3}\.\d\d$", mon)


def zipcode(zippy):
    return re.findall(r"^\d{5}$|^\d{5}\-\d{4}$", zippy)


def date(dates):
    return re.findall(r"^\d\d?\/\d\d?\/\d{4}$|^\d{4}\-\d\d?\-\d\d?$", dates)


def email(document_to_search):
    return re.findall(r"", document_to_search)


def address(document_to_search):
    return re.findall(r"", document_to_search)
