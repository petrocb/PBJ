import functions

class TestStrat:

    def __init__(self, account):
        self.account = account
        self.count = 0

    def tick(self):
# win from buy trade from no position 1
        if self.count == 0:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 1:
            functions.order(-1000, self.account, self.account, 0,0,0)
# even from buy trade from no position 1
        elif self.count == 2:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 3:
            functions.order(-1000, self.account, self.account, 0,0,0)
# loss from buy trade from no position 1
        elif self.count == 4:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 5:
            functions.order(-1000, self.account, self.account, 0,0,0)
# win from sell trade from no position 1
        elif self.count == 6:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 7:
            functions.order(1000, self.account, self.account, 0,0,0)
# even from sell trade from no position 1
        elif self.count == 8:
            functions.order(-1000, self.account, self.account, 0,0,0)
# loss from sell trade from no position 1
        elif self.count == 9:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 10:
            functions.order(-1000, self.account, self.account, 0,0,0)
# win buy trade from long position 1
        elif self.count == 11:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 12:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 13:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 14:
            functions.order(-1000, self.account, self.account, 0,0,0)
# even buy trade from long position 1
        elif self.count == 15:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 16:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 17:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 18:
            functions.order(-1000, self.account, self.account, 0,0,0)
# loss buy trade from long position 1
        elif self.count == 19:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 20:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 21:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 22:
            functions.order(-1000, self.account, self.account, 0,0,0)
# win sell trade from short position 1
        elif self.count == 23:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 24:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 25:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 26:
            functions.order(1000, self.account, self.account, 0,0,0)
# even sell trade from short position 1
        elif self.count == 27:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 28:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 29:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 30:
            functions.order(1000, self.account, self.account, 0,0,0)
# loss sell trade from short position
        elif self.count == 31:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 32:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 33:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 34:
            functions.order(1000, self.account, self.account, 0,0,0)
# win buy trade from short position which is equal to the oldest sell trade
        elif self.count == 35:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 36:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 37:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 38:
            functions.order(1000, self.account, self.account, 0,0,0)
# even buy trade from short position which is equal to the oldest sell trade
        elif self.count == 39:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 40:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 41:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 42:
            functions.order(1000, self.account, self.account, 0,0,0)
# loss buy trade from short position which is equal to the oldest sell trade
        elif self.count == 43:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 44:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 45:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 46:
            functions.order(1000, self.account, self.account, 0,0,0)
# win buy trade from short position which is less than the oldest sell trade
        elif self.count == 47:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 48:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 49:
            functions.order(1000, self.account, self.account, 0,0,0)
        elif self.count == 50:
            functions.order(1000, self.account, self.account, 0,0,0)
# even buy trade from short position which is less than the oldest sell trade
# loss buy trade from short position which is less than the oldest sell trade
# win buy trade from short position which is greater than the oldest sell trade
# even buy trade from short position which is greater than the oldest sell trade
# loss buy trade from short position which is greater than the oldest sell trade
# win sell trade from long position which is equal to the oldest buy trade
# even sell trade from long position which is equal to the oldest buy trade
# loss sell trade from long position which is equal to the oldest buy trade
# win sell trade from long position which is less than the oldest buy trade
# even sell trade from long position which is less than the oldest buy trade
# loss sell trade from long position which is less than the oldest buy trade
# win sell trade from long position which is greater than the oldest buy trade
# even sell trade from long position which is greater than the oldest buy trade
# loss sell trade from long position which is greater than the oldest buy trade
# win buy trade from short position which is equal to the whole short position
# even buy trade from short position which is equal to the whole short position
# loss buy trade from short position which is equal to the whole short position
# win sell trade from long position which is equal to the whole long position
# even sell trade from long position which is equal to the whole long position
# loss sell trade from long position which is equal to the whole long position
# win buy trade from short position which is greater than the whole short position
# even buy trade from short position which is greater than the whole short position
# loss buy trade from short position which is greater than the whole short position
# win sell trade from long position which is greater than the whole long position
# even sell trade from long position which is greater than the whole long position
# loss sell trade from long position which is greater than the whole long position
        self.count += 1
        functions.update()

