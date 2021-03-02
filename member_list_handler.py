import json


class JsonHandler:

    def __init__(self):
        """
        Read a .json file
        It saves in 'self.data'
        :return: string 'self.data'
        """
        self.data: dict = {}
        self.users: dict = {}

        with open('test.json', 'r') as json_file:
            self.data = json.load(json_file)

        for user in self.data['users']:
            self.users.update(user)

    def write_file(self):
        """
        Write 'self.data' string to current file
        """
        if self.data != []:
            with open('test.json', 'w') as json_file:
                json_string = json.dumps(self.data)
                json_file.write(json_string)
