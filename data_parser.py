import re
import numpy as np



class RandomDataParser:
    def __init__(self) -> None:
        pass

    def read_to_np_arr(self, filename: str = "./output.txt") -> np.ndarray:
        np_arr = np.genfromtxt(filename, dtype="<U15", delimiter=", ")
        return np_arr

    def regex_check(self, item) -> list:
        if re.findall(r"(^\d+$)", item) != []:
            return f"{item} - integer"
        elif re.findall(r"(^\d+\.\d+$)", item) != []:
            return f"{item} - real numbers"
        elif re.findall(r"(\b\w{10}\b)", item) != []:
            return f"{item} - alphabetical strings"
        elif re.findall(r"(\b\w{13}\b)", item) != []:
            return f"{item} - alphanumeric"

        return []

    def get_items_type(self, np_arr: np.ndarray) -> None:
        for index, item in enumerate(np.nditer(np_arr)):
            print(self.regex_check(str(item)))


if __name__ == "__main__":
    parser = RandomDataParser()
    np_arr = parser.read_to_np_arr()
    parser.get_items_type(np_arr)
