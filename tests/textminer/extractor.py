import re


def phone_numbers(document_to_search):
    return re.findall(r"\(?\d{3}\)?\s?\-?\d{3}\s?\-?\d{4}", document_to_search)


def emails(document_to_search):
    return re.findall(r"\w+\.*\w*\@\w+\.\w+", document_to_search)
