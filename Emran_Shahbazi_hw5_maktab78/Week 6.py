import pickle
import dill


class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

        def __repr__(self):
            return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


pickled_file = open('users.pickled', 'rb')
users = pickle.load(pickled_file)

file_1 = open("output-q-3-1.txt", "w")
file_2 = open("output-q-3-2.txt", "w")
dill_file = open("output-q-3-3.dill", "wb")
users.sort(key=lambda x: x.id)

for user in users:
    file_1.write(f"User_Id: {user.id}" + "\t" + str(user) + "\n")
    if user.phone[1:4] == "919":
        file_2.write(f"User_Phone: {user.phone}" + "\t" + str(user) + "\n")

    dill.dump(str(user.fullname()) + '\n', dill_file)

dill_file.close()

