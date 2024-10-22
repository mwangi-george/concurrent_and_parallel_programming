import time


def calc_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()

    for i in range(10):
        calc_sum_squares((i + 1) * 1000000)

    print('Calculating sum of squares took', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    for i in range(1, 5):
        sleep_a_little(i)

    print('Sleeping took', round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()
