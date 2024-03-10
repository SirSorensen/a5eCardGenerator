


from json import JSONEncoder


class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__