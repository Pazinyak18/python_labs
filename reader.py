import fileinput
import re
import sys


class Reader:
    def __init__(self, file_path: str = ""):
        self.file_path = file_path
        self.period_list = []
        self.bad_request = []
        self.count_req = 0
        self.count_bad = 0

    def read_file(self):
        try:
            file = open(self.file_path, mode='rb')
            lines = file.read().splitlines()
            file.close()
        except IOError as e:
            print(f"\u001b[31;1m {e}")
            sys.exit()
        return lines

    def search_period(self, start_date: str = " ", end_date: str = " "):
        time_re = r'\d+/\w+/\d+:\d+:\d+:\d+'
        self.count_req = 0
        period = False
        self.sort_by_date_and_time()
        file = open(f"copyof{self.file_path}", mode='r')
        lines = file.read().splitlines()

        for line in lines:
            found_start_time = re.findall(time_re, str(line))
            self.count_req += 1
            if period:
                break
            for time in found_start_time:
                if time > f"{end_date}":
                    period = True
                    break
                else:
                    pass
                if time >= f"{start_date}":
                    self.period_list.append(line)

    def search_bad_req(self):
        bad_req = r'(GET \/presentations).*(\s4\d{2}\s|\s5\d{2}\s)'
        self.bad_request = []
        self.count_bad = 0
        for req in self.period_list:
            if re.findall(bad_req, str(req)):
                self.count_bad += 1
                self.bad_request.append(req)
        print(f"\u001b[31;1m Amount of bad requests of presentation {self.count_bad}")

    def sort_by_date_and_time(self):
        lines = list(fileinput.input(self.file_path))
        file = open(f"copyof{self.file_path}", mode='w')
        for line in sorted(lines, key=lambda l: re.findall(r'\d+/\w+/\d+:\d+:\d+:\d+', str(l))):
            file.write(line)
        file.close()
