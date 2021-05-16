import termtables as tt
from settings import NUMBERS_MAP

if __name__ == "__main__":
    string = tt.to_string(NUMBERS_MAP, padding=(1, 3))
    print(string)

