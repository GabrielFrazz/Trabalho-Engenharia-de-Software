class Feedback():
    def __init__(self):
        id = 0
        name = ''
        date = ''
        message = ''

    def create_feedback(self,id,name,date,message):
        self.id = id
        self.name = name
        self.date = date
        self.message = message

    def __str__(self):
        return f"{self.id}, {self.name}, {self.date}, {self.message}"