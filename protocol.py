class Savable:
    def save(self) -> None: ...


class DatabaseRecord:
    def save(self) -> None:
        print("Saving to DB")


class User: ...


class LogFile:
    def save(self) -> None:
        print("writing to file")


def commit_data(item: Savable) -> None:
    item.save()


db_obj = DatabaseRecord()
commit_data(db_obj)

log_obj = LogFile()
commit_data(log_obj)
commit_data(User())
