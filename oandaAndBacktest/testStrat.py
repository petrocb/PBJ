import functions

class TestStrat:

    def __init__(self, account):
        self.account = account
        self.count = 0

    def tick(self):
        if self.count % 2 == 0:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count % 2 == 1:
            functions.order(-1000, self.account, self.account, 0,0,0)
        self.count += 1
        functions.update()

