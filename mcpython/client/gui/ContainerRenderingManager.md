***ContainerRenderingManager.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class OpenedInventoryStatePart extends  mcpython.common.state.AbstractStatePart.AbstractStatePart 
        
        Class for inventories as state
        todo: more control to the inventories themselves


        function __init__(self)

            variable self.active

            variable self.slot_list

            variable self.moving_itemstack: typing.Optional[ItemStack]

            variable self.mode
                The mode for dragging; Possible: 0 - None, 1: equal on all slots, 2: on every slot one more, 3: fill up slots

            variable self.original_amount: typing.List[int]

                variable self.tool_tip_renderer

        function bind_to_eventbus(self)

                variable player

                variable dimension

                variable itemstack

        function on_draw_2d(self)

                variable shared.inventory_handler.moving_slot.position

        function _get_slot_for(self, x: int, y: int) -> mcpython.client.gui.Slot.Slot | None
            
            Gets slot for position
            :param x: the x position
            :param y: the y position
            :return: the slot or None if none found
            todo: move to InventoryHandler


        function get_inventory_for(self, x: int, y: int)

        function _get_slot_inventory_for(
                self, x: int, y: int
                ) -> typing.Tuple[mcpython.client.gui.Slot.Slot | None, typing.Any]:
            
            Gets inventory of the slot for the position
            :param x: the x position
            :param y: the y position
            :return: the slot and the inventory or None and None if none found
            todo: move to InventoryHandler


            variable self.moving_itemstack

            variable moving_itemstack

            variable slot: mcpython.client.gui.Slot.Slot

                variable player

                variable dimension

                    variable flag

                variable self.mode

                variable amount

                variable self.mode

                variable self.mode

                variable stack_a

                variable self.moving_itemstack

                variable self.mode

            variable player

            variable dimension

                variable self.moving_itemstack

                variable self.mode

                variable self.moving_itemstack

                variable self.mode

                variable self.moving_itemstack

                variable self.mode

            variable slot

                variable slot

                    variable flag

                variable total

                variable per_element

                variable overhead

                    variable x

                    variable count

                    variable off

                variable overhead

            variable slot

    variable inventory_part

    class InventoryHandler
        
        Main class for registration of inventories
        Will handle every inventory created at any time. Will keep track of which inventories are open and to send the
            events to their event bus.
        Please do not mess around with the internal lists as they are representing the state of the inventory system.
        As such, this stuff is not API and may change at any point


        function __init__(self)

            variable self.open_containers

            variable self.always_open_containers

            variable self.containers - todo: can we make this weak?

            variable self.moving_slot: mcpython.client.gui.Slot.Slot

        function tick(self, dt: float)

        function update_shift_container(self)
            
            Adds a new inventory to the internal handling system
            :param inventory: the inventory to add

            
            Shows an inventory by adding it to the corresponding structure
            :param inventory: the inventory to show

            
            Hides an inventory
            :param inventory: the inventory to hide
            :param force: if force hide, skipping flag check for always active

            
            Removes one inventory from stack which can be removed
            :param is_escape: if to handle like it is an escape press, so we skip containers not wanting to be closed that
                way
            :return: the inventory removed or None if no is active


            variable stack

        function close_all_inventories(self)
            
            Close all inventories currently open, excluding inventories marked for always being open


    variable shared.inventory_handler