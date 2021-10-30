***Slot.py - documentation - last updated on 30.10.2021 by uuk***
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

        function __init__(self)

            variable self.assigned_inventory

        function get_capacity(self) -> int

        function get_itemstack(self) -> mcpython.common.container.ResourceStack.ItemStack

        function set_itemstack(
                self,
                stack: mcpython.common.container.ResourceStack.ItemStack,
                update=True,
                player=False,
                ):

        function call_update(self, player=False)

        function copy(self, position=(0, 0))

        function deepCopy(self)

        function draw(self, dx=0, dy=0, hovering=False, center_position=None)

        function draw_label(self, x=None, y=None)

        function is_item_allowed(
                self, itemstack: mcpython.common.container.ResourceStack.ItemStack
                ) -> bool:

        function save(self)

        function load(self, data)

        function getParent(self) -> "ISlot"

        function clean_itemstack(self)

    class Slot extends ISlot
        
        slot class


        function __init__(
                self,
                itemstack=None,
                position=(0, 0),
                allow_player_remove=True,
                allow_player_insert=True,
                allow_player_add_to_free_place=True,
                on_update=None,
                allow_half_getting=True,
                on_shift_click=None,
                empty_image=None,
                allowed_item_tags=None,
                disallowed_item_tags=None,
                allowed_item_test=None,
                on_button_press=None,
                capacity=None,
                check_function=None,
                ):
            
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
            :param check_function: an function to check if the item is valid, signature: (Slot, ItemStack) -> bool


            variable self.__itemstack

            variable self.position

                variable image

                variable self.sprite: pyglet.sprite.Sprite

                variable self.sprite

            variable self.amount_label

            variable self.__last_item_file

            variable self.interaction_mode
                todo: make separated attributes

            variable self.on_update

            variable self.allow_half_getting

            variable self.on_shift_click

            variable self.amount_label

            variable self.children

            variable self.empty_image

            variable self.allowed_item_tags

            variable self.disallowed_item_tags

            variable self.allowed_item_func

            variable self.on_button_press

            variable self.__capacity

            variable self.check_function

        function read_from_network_buffer(self, buffer: ReadBuffer)

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function get_capacity(self) -> int

        function get_itemstack(self) -> mcpython.common.container.ResourceStack.ItemStack

        function set_itemstack(
                self,
                stack: mcpython.common.container.ResourceStack.ItemStack,
                update=True,
                player=False,
                ):

            variable self.__itemstack

        function call_update(self, player=False)

        variable itemstack

        function copy(self, position=(0, 0))
            
            creates an copy of self
            :param position: the position to create at
            :return: a slotcopy pointing to this


        function deepCopy(self)
            
            This will copy the content of the slot into an Slot-object


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

        function is_item_allowed(
                self, itemstack: mcpython.common.container.ResourceStack.ItemStack
                ) -> bool:

            variable any_tag_set

            variable has_correct_tag

            variable has_allowed_func

            variable check_allowed_func

        function save(self)

                variable d["data"]

        function load(self, data)

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

            variable self.allow_half_getting

            variable self.on_shift_click

            variable self.amount_label

            variable self.on_button_press

            variable self.slot_position

        function get_allowed_item_tags(self)

        function set_allowed_item_tags(self, tags: list)

        variable allowed_item_tags

        function get_itemstack(self)

        function set_itemstack(self, stack, **kwargs)

        function call_update(self, player=False)

        variable itemstack

        function copy(self, position=(0, 0))

        function draw(self, dx=0, dy=0, hovering=False, center_position=None)

        function draw_label(self, x=None, y=None)

        function is_item_allowed(self, itemstack) -> bool

        function save(self)

        function load(self, data)

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

        variable itemstack

        function __repr__(self)

        function __str__(self)

        function is_item_allowed(
                self, itemstack: mcpython.common.container.ResourceStack.ItemStack
                ) -> bool:

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
                stack: mcpython.common.container.ResourceStack.ItemStack,
                update=True,
                player=False,
                ):

            variable self.__itemstack

                variable self.reference_stack

        function call_update(self, player=False)

        variable itemstack

    class SlotTrashCan extends Slot

        function set_itemstack(self, stack, update=True, player=False)