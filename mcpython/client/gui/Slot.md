***Slot.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable SLOT_WIDTH

        variable PYGLET_IMAGE_HOVERING

        variable PYGLET_IMAGE_HOVERING

    class ISlot extends IBufferSerializeAble,  ABC
        
        Base class for everything slot-like
        Provides some API for interaction with the user


        function __init__(self)

            variable self.on_update

            variable self.assigned_inventory

        function get_capacity(self) -> int

        function get_itemstack(self) -> ItemStack

        function set_itemstack(
                self,
                stack: ItemStack,
                update=True,
                player=False,
                ):

        function set_itemstack_force(self, *args, **kwargs)

        function call_update(self, player=False)

        function copy(self, position=(0, 0))

        function deepCopy(self)

        function draw(self, dx=0, dy=0, hovering=False, center_position=None)

        function draw_label(self, x=None, y=None)

        function is_item_allowed(self, itemstack: ItemStack) -> bool

        function getParent(self) -> "ISlot"

        function clean_itemstack(self)

        function invalidate(self)

    class Slot extends ISlot
        
        Basic slot class


        function __init__(
                self,
                itemstack: ItemStack = None,
                position: typing.Tuple[int, int] = (0, 0),
                allow_player_remove=True,
                allow_player_insert=True,
                allow_player_add_to_free_place=True,
                allow_half_getting=True,
                allowed_item_tags: typing.Optional[typing.List[str]] = None,
                disallowed_item_tags: typing.Optional[typing.List[str]] = None,
                allowed_item_test: typing.Optional[typing.Callable] = None,
                on_update: typing.Optional[typing.Callable] = None,
                on_shift_click: typing.Optional[typing.Callable] = None,
                on_button_press: typing.Optional[typing.Callable] = None,
                on_click_on_slot: typing.Optional[typing.Callable] = None,
                empty_image: typing.Optional = None,
                enable_hovering_background=True,
                capacity: typing.Optional[int] = None,
                check_function=None,
                ):

            variable itemstack: ItemStack

            variable allowed_item_tags: typing.Optional[typing.List[str]]

            variable disallowed_item_tags: typing.Optional[typing.List[str]]

            variable allowed_item_test: typing.Optional[typing.Callable]

            variable on_update: typing.Optional[typing.Callable]

            variable on_shift_click: typing.Optional[typing.Callable]

            variable on_button_press: typing.Optional[typing.Callable]

            variable on_click_on_slot: typing.Optional[typing.Callable]

            variable empty_image: typing.Optional

            variable capacity: typing.Optional[int]
            
            Creates a new slot
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
            :param check_function: a function to check if the item is valid, signature: (Slot, ItemStack) -> bool
            :param on_click_on_slot: a function invoked with button & modifiers when the player pressed on the slot


            variable self.__itemstack

            variable self.position

                variable image

                variable self.sprite: pyglet.sprite.Sprite

                variable self.sprite

                variable self.amount_label

                variable self.__last_item_file

                variable self.amount_label

            variable self.interaction_mode
                todo: make separated attributes

            variable self.on_update

            variable self.allow_half_getting

            variable self.on_shift_click

            variable self.children

                variable self.empty_image

            variable self.on_click_on_slot

            variable self.allowed_item_tags

            variable self.disallowed_item_tags

            variable self.allowed_item_func

            variable self.enable_hovering_background

            variable self.on_button_press

            variable self.__capacity

            variable self.check_function

                variable result

        function get_capacity(self) -> int

        function get_itemstack(self) -> ItemStack

        function get_linked_itemstack_for_sift_clicking(self)

        function set_itemstack(
                self,
                stack: ItemStack,
                update=True,
                player=False,
                ):

            variable self.__itemstack

        function call_update(self, player=False)

                    variable result

        variable itemstack

        function copy(self, position=(0, 0))
            
            creates an copy of self
            :param position: the position to create at
            :return: a slotcopy pointing to this


        function deepCopy(self)
            
            This will copy the content of the slot into a Slot-object


        function draw(self, dx=0, dy=0, hovering=False, center_position=None)
            
            Draws the slot


                variable PYGLET_IMAGE_HOVERING.position

                variable image

                variable self.sprite: pyglet.sprite.Sprite

                variable self.sprite

                    variable self.empty_image.position

                variable self.sprite.position

            variable self.__last_item_file

        function draw_label(self, x=None, y=None)
            
            these code draws only the label, before, normal draw should be executed for correct setup


                variable self.amount_label.text

                variable self.amount_label.x

                variable self.amount_label.y

        function is_item_allowed(self, itemstack: ItemStack) -> bool

            variable any_tag_set

            variable has_correct_tag

            variable has_allowed_func

            variable check_allowed_func

        function __str__(self)

        function __repr__(self)

        function getParent(self)

    class SlotCopy extends ISlot

        function get_capacity(self) -> int

        function deepCopy(self)

        function __init__(
                self,
                master,
                position=(0, 0),
                allow_player_remove=True,
                allow_player_insert=True,
                allow_player_add_to_free_place=True,
                on_update=None,
                allow_half_getting=True,
                on_shift_click=None,
                on_button_press=None,
                on_click_on_slot=None,
                ):

            variable self.master: Slot
                todo: add empty image
                todo: add options for item allowing

            variable self.position

                variable image

                variable self.sprite: pyglet.sprite.Sprite

                variable self.sprite

            variable self.__last_item_file

            variable self.interaction_mode

            variable self.on_update

            variable self.on_click_on_slot

            variable self.allow_half_getting

            variable self.on_shift_click

                variable self.amount_label

            variable self.on_button_press

            variable self.slot_position

        function get_linked_itemstack_for_sift_clicking(self)

        function get_allowed_item_tags(self)

        function set_allowed_item_tags(self, tags: list)

        variable allowed_item_tags

        function get_itemstack(self) -> ItemStack

        function set_itemstack(self, stack, **kwargs)

        function call_update(self, player=False)

        variable itemstack

        function copy(self, position=(0, 0))

        function draw(self, dx=0, dy=0, hovering=False, center_position=None)

        function draw_label(self, x=None, y=None)

        function is_item_allowed(self, itemstack) -> bool

        function __str__(self)

        function __repr__(self)

        function getParent(self)

    class SlotCopyWithDynamicTarget extends SlotCopy

        function __init__(
                self,
                getter: typing.Callable[[], ISlot],
                position=(0, 0),
                allow_player_remove=True,
                allow_player_insert=True,
                allow_player_add_to_free_place=True,
                on_update=None,
                on_click_on_slot=None,
                allow_half_getting=True,
                on_shift_click=None,
                on_button_press=None,
                ):

            variable self.slot_position

            variable self.getter

            variable self.valid

            variable self.cached_master

            variable self.position

            variable self.__last_item_file

            variable self.interaction_mode

            variable self.on_update

            variable self.on_click_on_slot

            variable self.allow_half_getting

            variable self.on_shift_click

                variable self.amount_label

            variable self.on_button_press

        function invalidate(self)

        function get_master(self)

        variable master

    class SlotInfiniteStack extends Slot

        function __init__(
                self,
                itemstack,
                position=(0, 0),
                allow_player_remove=True,
                on_button_press=None,
                allow_player_add_to_free_place=True,
                on_update=None,
                allow_half_getting=True,
                on_shift_click=None,
                allow_player_override_delete=True,
                ):

            variable self.reference_stack

        function set_itemstack(self, stack, update=True, player=False)

        function clean_itemstack(self)

        function set_itemstack_force(self, stack)

        function call_update(self, player=False)

        function get_linked_itemstack_for_sift_clicking(self)

        variable itemstack

        function __repr__(self)

        function __str__(self)

        function is_item_allowed(self, itemstack: ItemStack) -> bool

    class SlotInfiniteStackExchangeable extends Slot

        function __init__(
                self,
                itemstack,
                position=(0, 0),
                allow_player_remove=True,
                on_button_press=None,
                allow_player_add_to_free_place=True,
                on_update=None,
                allow_half_getting=True,
                on_shift_click=None,
                ):

            variable self.reference_stack

        function set_itemstack(
                self,
                stack: ItemStack,
                update=True,
                player=False,
                ):

            variable self.__itemstack

                variable self.reference_stack

        function call_update(self, player=False)

        variable itemstack

    class SlotTrashCan extends Slot

        function set_itemstack(self, stack, update=True, player=False)