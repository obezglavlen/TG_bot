class Antimat:

    def __init__(self):
        """
        Initialisation method.
        Opens file, save text into list
        """
        self._mat_list: list = []

        # Exception block
        try:
            open('mat_list_filter.txt', 'r')

        except FileNotFoundError as e:
            # If can't open file - print error in console
            print(e)
            # And print error in log file
            with open('logs.txt', 'a') as log_file:
                log_file.write(f'{str(e)}, file was recreate')
            # And create empty mat_list_filter file
            with open('mat_list_filter.txt',
                      'a',
                      encoding='windows-1251'):
                pass

        # If file opens normally, work with it
        else:
            with open('mat_list_filter.txt', 'r') as input_file:
                self._mat_list = input_file.read().split('\n')

        finally:
            if len(self._mat_list) > 0:
                # Remove repeats
                self._mat_list = [x.lower() for x in set(self._mat_list)]

                # If empty string - remove
                if '' in self._mat_list:
                    self._mat_list.remove('')

    def check(self, message: str) -> bool:
        return message.lower() in self._mat_list
