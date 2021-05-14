from reader import Reader


def main():
    reader = Reader("apache_logs.txt")
    reader.search_period("17/May/2015:04:00:00", "17/May/2015:21:08:00")
    reader.search_bad_req()

    for i in reader.bad_request:
        print(str(i))


if __name__ == '__main__':
    main()
