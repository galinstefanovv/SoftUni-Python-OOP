from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*nums: List[int]) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums: List[int]):
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def divide(*nums: List[int]):
        return reduce(lambda a, b: a / b, nums)

    @staticmethod
    def subtract(*nums: List[int]):
        return reduce(lambda a, b: a - b, nums)
