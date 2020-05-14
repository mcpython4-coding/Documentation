***ItemFood.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ItemFood extends item.Item.Item
        function on_eat(self)
            
            called when the player eats the item
            :return: if the item was eaten or not
            


        variable HUNGER_ADDITION

        function get_eat_hunger_addition(self) -> int