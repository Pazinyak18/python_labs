# py lab5

### [1]Task 
- Count the number of failed GET presentation requests (revenge word presentations in the request url and status codes 400-599)
- performed 17 / May / 2015 between 04:00 to 21:28
- log on link
### [2]hOw tO Run
```
$ git clone https://github.com/Pazinyak18/python_labs.git
$ cd python_labs
$ git checkout lab5
$ python Main.py
```
### [3]All realization of methods in class TechniqueManager package manager
<details>
<summary>[3.1]search_period</summary>
<p>

```python
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
```
</p>
</details> 

<details>
<summary>[3.2]search_bad_req</summary>
<p>

```python
def search_bad_req(self):
        bad_req = r'(GET \/presentations).*(\s4\d{2}\s|\s5\d{2}\s)'
        self.bad_request = []
        self.count_bad = 0
        for req in self.period_list:
            if re.findall(bad_req, str(req)):
                self.count_bad += 1
                self.bad_request.append(req)
        print(f"\u001b[31;1m Amount of bad requests of presentation {self.count_bad}")
```
</p>
</details>  

<details>
<summary>[3.3]sort_by_date_and_time</summary>
<p>

```python
def sort_by_date_and_time(self):
        lines = list(fileinput.input(self.file_path))
        file = open(f"copyof{self.file_path}", mode='w')
        for line in sorted(lines, key=lambda l: re.findall(r'\d+/\w+/\d+:\d+:\d+:\d+', str(l))):
            file.write(line)
        file.close()
```
</p>
</details>

<details>
<summary>[3.4]read_file</summary>
<p>

```python
def read_file(self):
        try:
            file = open(self.file_path, mode='rb')
            lines = file.read().splitlines()
            file.close()
        except IOError as e:
            print(f"\u001b[31;1m {e}")
            sys.exit()
        return lines
```
</p>
</details>

## [5]Links
### log file https://github.com/elastic/examples/blob/master/Common%20Data%20Formats/apache_logs/apache_logs


