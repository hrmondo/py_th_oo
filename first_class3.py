class Student:
    name = "Your Name"

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
        #if self.grade > 50:
        # Instance of 'Student' has no 'grade' member.
         
            return self.praise()
        else:
            return self.reassurance()