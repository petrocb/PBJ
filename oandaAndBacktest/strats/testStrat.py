import functions

class TestStrat:

    def __init__(self, account):
        self.account = account
        self.count = 0

    def tick(self):
# win from buy trade from no position 1
        if self.count == 0:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 1:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# even from buy trade from no position 1
        elif self.count == 2:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 3:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# loss from buy trade from no position 1
        elif self.count == 4:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 5:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# win from sell trade from no position 1
        elif self.count == 6:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 7:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# even from sell trade from no position 1
        elif self.count == 8:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# loss from sell trade from no position 1
        elif self.count == 9:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 10:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# win buy trade from long position 1
        elif self.count == 11:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 12:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 13:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 14:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# even buy trade from long position 1
        elif self.count == 15:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 16:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 17:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 18:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# loss buy trade from long position 1
        elif self.count == 19:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 20:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 21:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 22:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
# win sell trade from short position 1
        elif self.count == 23:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 24:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 25:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 26:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# even sell trade from short position 1
        elif self.count == 27:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 28:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 29:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 30:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# loss sell trade from short position
        elif self.count == 31:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 32:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 33:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 34:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# win buy trade from short position which is equal to the oldest sell trade
        elif self.count == 35:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 36:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 37:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 38:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# even buy trade from short position which is equal to the oldest sell trade
        elif self.count == 39:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 40:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 41:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 42:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# loss buy trade from short position which is equal to the oldest sell trade
        elif self.count == 43:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 44:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 45:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 46:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
# win buy trade from short position which is less than the oldest sell trade
        elif self.count == 47:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 48:
            functions.marketOrder(-1000, self.account, self.account, 0, 0, 0)
        elif self.count == 49:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
        elif self.count == 50:
            functions.marketOrder(1000, self.account, self.account, 0, 0, 0)
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

