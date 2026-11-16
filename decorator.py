from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_dict, *args, **kwargs):
        if user_dict.get("role") != "admin":
            raise PermissionError("Access denied")

        return func(user_dict, *args, **kwargs)

    return wrapper


@require_admin
def delete_database_table(user):
    print("table deleted")


@require_admin
def update_user_email(user, new_email, send_notification=True):
    print(f"Updating email to {new_email}")


delete_database_table({"name": "aditya", "role": "admin"})
update_user_email({"name": "adi", "role": "admin"}, "adityakumar@gmail.com")

# What you write:
# @timer
# def fetch(): pass

# # What Python actually executes:
# fetch = timer(fetch)


# What you write:
# @retry(3)
# def fetch(): pass

# # What Python actually executes:
# # Step 1: Execute retry(3). This must return a decorator!
# temp_decorator = retry(3)


# # Step 2: Now use that returned decorator to wrap the function
# fetch = temp_decorator(fetch)
# Level 1: Catches the '3'
def retry(max_attempts):

    # Level 2: Catches the 'connect' function
    def decorator(func):

        # Level 3: Runs the code using both the '3' and the 'func'
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                func(*args, **kwargs)

        return wrapper

    return decorator


@retry(3)
def connect():
    pass
