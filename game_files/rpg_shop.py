import random

class shop():
    items = {
        "apple": 10,
        "potion": 20,
    }

    player_money = 0
    player_backpack = {}

    def __init__(self, player:object):
        self.player_money = player.player_money
        self.player_backpack = player.player_backpack

    def buy_item(self, buy_item: str):
        #TODO add money system to reduce money
        #TODO Add amt arg to buy and sell
        if buy_item in self.items:
            if buy_item in self.player_backpack:
                self.player_backpack[buy_item] += 1
            else:
                self.player_backpack[buy_item] = 1
                return f"Item Bought! You now have {self.player_backpack[buy_item]} {buy_item}(s)!"
        else:
            return "Item doesn't exist"

    def sell_item(self, sell_item: str):
        if sell_item in self.items:
            if sell_item in self.player_backpack and self.player_backpack[sell_item] != 0:
                self.player_backpack[sell_item] -= 1
                return f"Item is gon! You now haz {self.player_backpack[sell_item]} {sell_item}(s)!"
            else:
                return f"Y u try trick shop. Yuo not have enuf item. kil monsta."
        else:
            return "Item doesn't exist"

    
    #TODO Add save system, that exports - Player_backpack and player_money :D
    def ret_money_backpack(self):
        return self.player_money, self.player_backpack
    