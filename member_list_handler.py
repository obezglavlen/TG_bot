import json


class TestJsonFileHandler:
    """
    Test class for work with .json, for save users.
    """

    def __init__(self):
        """
        Constructor, create empty 'data' string
        """
        self.data = ""

    # При вызове метода не создавая объект,
    # Оно просит передать в аргументы 'self'
    # Как это убрать я не понимаю, в интернете
    # Такого почемуто нет

    def read_file(self):
        """
        Read a .json file
        It saves in 'data'
        :return: string 'data'
        """
        with open('test.json', 'r') as json_file:
            self.data = json.load(json_file)
        return self.data

    def log_file(self):
        """
        Log current file
        It print an object of file
        :return: Only print
        """
        if self.data is not None:
            print(json.dumps(self.data))

    # Написано по страшному, думаю можно короче
    def write_file(self):
        """
        Write 'data' string to current file
        """
        if self.data is not None:
            with open('test.json', 'w') as json_file:
                json_string = json.dumps(self.data)
                json_file.write(json_string)
