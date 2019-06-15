from multiprocessing import Pool
import os


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(os.cpu_count()) as p:
        print(p.map(f, [1, 2, 3]))
