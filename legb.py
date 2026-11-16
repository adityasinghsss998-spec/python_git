def make_retry_handler(max_retries: int):
    # enclosing scope
    attempts = 0  # now it lives in closure in hidden attribute my_runner.__closure__

    def execute(task):
        nonlocal attempts
        if attempts >= max_retries:
            raise Exception("Max retries exceeded")
        attempts += 1
        return task()

    return execute


def fetch_user_data():
    return {"user_id": 2, "name": "aditya"}


if __name__ == "__main__":
    my_runner = make_retry_handler(max_retries=3)
    res1 = my_runner(fetch_user_data)
    print("result1 :", res1)
    res2 = my_runner(fetch_user_data)
    print("result2 :", res2)
    res3 = my_runner(fetch_user_data)
    print("result1 :", res3)


# we code like this because of seperation of concern
