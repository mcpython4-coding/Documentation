***ItemStack.py - documentation - last updated on 6.6.2020 by uuk***
___

    class ItemStack
        
        base class for item stored somewhere
        todo: add function to copy content from one ItemStack to another


        function __init__(self, item_name_or_instance, amount=1)

                variable self.item

        function copy(self)
            
            copy the itemstack
            :return: copy of itself


        function clean(self)
            
            clean the itemstack


        static
        function get_empty()
            
            get an empty itemstack


        function __eq__(self, other)

        function is_empty(self): return self.amount == 0 or self.item is None
                
                def get_item_name(self): return self.item.NAME if self.item else None
                
                def set_amount(self, amount):

        function get_item_name(self): return self.item.NAME if self.item else None
                
                def set_amount(self, amount):

        function set_amount(self, amount)

        function add_amount(self, amount, check_overflow=True)

        function __str__(self)