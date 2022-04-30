import datetime


class TimeoutException(Exception):
    message = ""

    def __init__(self, last_update, delta=datetime.timedelta(hours=1)):
        timeout_remaining: datetime.timedelta = (
            last_update + delta - datetime.datetime.now()
        )
        self.message = f"""Твой дик устал, дай ему отдохнуть, \
спермотоксикозник.\nОсталось {timeout_remaining.seconds // 60} \
минут {timeout_remaining.seconds - (timeout_remaining.seconds // 60) * 60} \
секунд(ыЫы)."""
        super().__init__(self.message)


class UserNotFoundException(Exception):
    message = "Ты не зарегистрирован в боте"

    def __init__(self):
        super().__init__(self.message)
