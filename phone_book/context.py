from contextlib import contextmanager
from colorama import Fore
from .entities import AddressBook
import sys
import pickle
from logger.logger import log_error

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError as error:
        log_error(f"File {filename} not found. New book was created, please proceed. All changes would be saved.")
        return AddressBook()

@contextmanager
def book_cxt_mngr():
    try:
        book = load_data()
        yield book
    except Exception as error:
        raise error
    finally:
        save_data(book)
        sys.exit(0)