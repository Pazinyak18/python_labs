class Student:
    # static var
    is_commerce = True

    # constructor
    def __init__(self, first_name="", last_name="", rank="", height="", group="", type_of_studying=""):
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.height = height
        self.group = group
        self.type_of_studying = type_of_studying

    # destructor
    def __del__(self):
        pass

    def __str__(self):
        return f"\nFirst Name: {self.first_name}\n " \
               f"Last Name: {self.last_name}\n " \
               f"Rank: {self.rank}\n " \
               f"Height: {self.height}\n " \
               f"Group: {self.group}\n " \
               f"Type of studying: {self.type_of_studying}\n " \
               f"Is commerce: {Student.is_commerce}\n"

    # methods
    @staticmethod
    def show_commerce_status():
        return Student.is_commerce


def main():
    Student.is_commerce = False
    students = [Student("Victor", "Mikituk", "mid", 1.80, "13", "daily"),
                Student("Kilun", "Fabr", "exel", 2.00, "11", "remote"),
                Student("Balik", "Kalik", "low", 1.90, "13", "daily")]
    for i in students:
        print(i)


if __name__ == '__main__':
    main()
