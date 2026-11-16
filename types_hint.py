from typing import TypedDict


class UserPayload(TypedDict):
    id: int
    username: str


def process_user(user: UserPayload) -> None:
    print(user["username"])


process_user({"id": 2, "username": "Aditya23"})
