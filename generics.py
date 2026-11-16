from typing import TypeVar

T = TypeVar("T")


def get_first(items: list[T]) -> T:
    return items


a = get_first([1, 2, 3])
b = get_first(["x", "y"])
c = get_first([{"name": "aditya", "id": 2}, 2])
print(a)
print(b)
print(c)
