import time
import threading


def calc_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)


def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(10):
        value = (i + 1) * 100000
        t = threading.Thread(target=calc_sum_squares, args=(value,))
        t.start()
        current_threads.append(t)

    for i in range(len(current_threads)):
        current_threads[i].join()   # blocks execution until current thread is done

    print('Calculating sum of squares took', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_threads = []
    for i in range(1, 5):
        t = threading.Thread(target=sleep_a_little, args=(i,))
        t.start()
        current_threads.append(t)

    for i in range(len(current_threads)):
        current_threads[i].join()

    print('Sleeping took', round(time.time() - sleep_start_time, 1))


if __name__ == '__main__':
    main()
