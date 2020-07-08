***Slot.py - documentation - last updated on 24.6.2020 by uuk***
___

    variable SLOT_WIDTH

    variable PYGLET_IMAGE_HOVERING

    class Slot
        
        slot class


        function __init__(self, itemstack=None, position=(0, 0), allow_player_remove=True, allow_player_insert=True,
                allow_player_add_to_free_place=True, on_update=None, allow_half_getting=True, on_shift_click=None,
                empty_image=None, allowed_item_tags=None, allowed_item_test=None, on_button_press=None, capacity=None):
            
            creates an new slot
            :param itemstack: the itemstack to use
            :param position: the position to create at
            :param allow_player_remove: if the player is allowed to remove items out of it
            :param allow_player_insert: if the player is allowed to insert items into it
            :param allow_player_add_to_free_place: if items can be added direct to system
            :param on_update: called when the slot is updated
            :param allow_half_getting: can the player get only the half of the items out of the slot?
            :param on_shift_click: called when shift-clicked on the block, should return if normal logic should go on or not
            :param on_button_press: called when an button is pressed when hovering above the slot
            :param capacity: the max item count for the slot


        function get_capacity(self)

        function get_itemstack(self)

        function set_itemstack(self, stack, update=True, player=False)

        function call_update(self, player=False)

        variable itemstack

        function copy(self, position=(0, 0))
            
            creates an copy of self
            :param position: the position to create at
            :return: a slotcopy pointing to this


        function draw(self, dx=0, dy=0, hovering=False)
            
            draws the slot


        function draw_lable(self, x, y)
            
            these code draws only the lable, before, normal draw should be executed for correcrt setup


                variable self.amount_label.text

                variable self.amount_label.x

                variable self.amount_label.y

        function can_set_item(self, itemstack) -> bool

        function save(self)

        function load(self, data)

        function __str__(self)

        function __repr__(self)

    class SlotCopy

        function __init__(self, master, position=(0, 0), allow_player_remove=True, allow_player_insert=True,
                allow_player_add_to_free_place=True, on_update=None, allow_half_getting=True, on_shift_click=None,
                on_button_press=None):

        function get_allowed_item_tags(self)

        function set_allowed_item_tags(self, tags: list)

        variable allowed_item_tags

        function get_itemstack(self)

        function set_itemstack(self, stack, **kwargs)

        function call_update(self, player=False)

        variable itemstack

        function copy(self, position=(0, 0))

        function draw(self, dx=0, dy=0, hovering=False)
            
            draws the slot


        function draw_lable(self, x, y)

        function can_set_item(self, itemstack) -> bool: return self.master.can_set_item(itemstack)
                
                def save(self):

        function save(self)

        function load(self, data)

        function __str__(self)

        function __repr__(self)

    class SlotInfiniteStack extends Slot

        function __init__(self, itemstack, position=(0, 0), allow_player_remove=True, on_button_press=None,
                allow_player_add_to_free_place=True, on_update=None, allow_half_getting=True, on_shift_click=None):

        function set_itemstack(self, stack, update=True, player=False)

        function call_update(self, player=False)

        variable itemstack

    class SlotInfiniteStackExchangeable extends Slot

        function __init__(self, itemstack, position=(0, 0), allow_player_remove=True, on_button_press=None,
                allow_player_add_to_free_place=True, on_update=None, allow_half_getting=True, on_shift_click=None):

        function set_itemstack(self, stack, update=True, player=False)

        function call_update(self, player=False)

        variable itemstack

    class SlotTrashCan extends Slot

        function set_itemstack(self, stack, update=True, player=False)