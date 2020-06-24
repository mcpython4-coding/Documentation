***ShiftContainer.py - documentation - last updated on 24.6.2020 by uuk***
___

    class ShiftContainer
        
        container class holding information on which inventory parts can be shift-clicked


        function __init__(self)

            variable self.container_A

            variable self.container_B

        function get_opposite_item_list_for(self, slot)

        function move_to_opposite(self, slot, count=None) -> bool