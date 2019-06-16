#!python 3.7

import re
import win32clipboard

def get_clipboard_date():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def extract_phone_numbers(data):
    print(data)
    numbers_regex = re.compile(r'((Dr\.)? (\w*\s\w* (\d{3}-\d{3}-\d{4})))',re.IGNORECASE)
    # numbers_regex = re.compile(r'Dr.(\w+\s\w)',re.IGNORECASE)
    # numbers_regex = re.compile(r'Dr. ', re.IGNORECASE)
    print(numbers_regex.findall(data))
    # print(numbers_regex.search(data))

raw_data = get_clipboard_date()
extract_phone_numbers(raw_data)
