from message_handler import start_handing
import member_list_handler as mlist


class test:
    """
    Try to create the setter and getter
    Congratulations!!!
    """
    def __init__(self):
        self._data = "test_data"

    @property
    def data(self):
        """
        Getter for '_data'
        :return: string '_data'
        """
        return self._data

    @data.setter
    def data(self, string):
        """
        Setter for '_data'
        :param string: input string to set
        """
        self._data = string | self._data


start_handing()
