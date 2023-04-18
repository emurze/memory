import itertools
import random as rand
from collections import ChainMap


def best() -> None:
    for idx, item in enumerate(general_list, start=5):
        print(f"{idx}-index, item - {item}")
    print(
        *(x for x in itertools.takewhile(lambda x: x < 9, iter(general_list)))
    )
    print(*itertools.accumulate(general_list, max))


def chain() -> None:
    map1 = ChainMap({"a": 3, "b": 5}, {"a": 4})  # doesn't return iterator
    print(map1.get("a"))
    print(*itertools.chain(iter(general_list), range(5, 30)))
    print(*itertools.chain.from_iterable([[1, [2], [3]], [2], [3]]))


def r_zip() -> None:
    print(*((i1, i2) for i1, i2 in
            itertools.zip_longest(range(1, 50), range(50, 105), fillvalue=0)))
    try:
        list(zip(range(10), range(11), strict=True))  # doesn't return iterator
    except ValueError:
        pass


def grouping() -> None:
    print(*itertools.pairwise(range(10)))
    for char, items in itertools.groupby(
            sorted(map(str, general_list), key=len), len):
        print(f"len - {char}:", *items)


def features() -> None:
    l1 = [[1, 2], [2, 4], [3, 4]]
    print(*itertools.starmap(round, l1))
    print(*itertools.takewhile(lambda args: args[0] < 10,
                               enumerate(itertools.cycle('ABC'))))


if __name__ == '__main__':
    general_list: list[int] = [rand.randrange(105) for _ in range(50)]
    best(), chain(), r_zip(), grouping(), features()
