***ItemStack.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ItemStack
        
        base class for item stored somewhere
        todo: add function to copy content from one ItemStack to another


        function __init__(self, item_name_or_instance, amount=1)

                variable self.item

                    variable self.item

                    variable self.item

                variable self.item

            variable self.amount

        function copy(self)
            
            copy the itemstack
            :return: copy of itself


        function clean(self)
            
            clean the itemstack


            variable self.item

            variable self.amount

        static function get_empty()
            
            get an empty itemstack


        function __eq__(self, other)

        function is_empty(self)

        function get_item_name(self)

        function set_amount(self, amount)

            variable self.amount

        function add_amount(self, amount)

        function __str__(self)