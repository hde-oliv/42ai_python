from time import sleep, perf_counter


def calculate_eta(start, now, pos, end):
    diff = now - start
    rem = end - pos

    return 0.0 if not pos else (rem / pos) * diff


def ft_progress(l):
    start = perf_counter()

    for i, v in enumerate(l):
        now = perf_counter()
        eta = calculate_eta(start, now, i, len(l))
        percentage = (i + 1) * 100 / len(l)
        bar = "=" * int((percentage * 20) / 100)

        bar = bar + ">" if int(percentage) < 100 else bar

        print("\r", end="")
        print(f"ETA: {eta: >5.2f}s", end=" ")
        print(f"[{percentage: >3.0f}%]", end=" ")
        print(f"[{bar: <20}]", end=" ")
        print(f"{i+1: >4}/{len(l): <4}", end=" ")
        print(f"| elapsed time {now-start: >2.2f}s", end="")

        yield v


def test_one():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


def test_two():
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)


def main():
    test_one()
    test_two()


if __name__ == "__main__":
    main()
