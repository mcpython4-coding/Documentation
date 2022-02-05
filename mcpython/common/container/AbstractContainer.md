***AbstractContainer.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractContainer extends IBufferSerializeAble,  ABC
        
        Base class for containers
        Can assign a certain ContainerRenderer to render stuff here


        function __init__(self)

            variable self.slots

            variable self.custom_name

            variable self.uuid

                variable slot.assigned_inventory

                variable self.renderer

                variable self.renderer

        function create_slots(self)
            
            Invoked during construction of the object; should fill the slots array with slot instances


            variable self.custom_name

            variable self.uuid

        function create_renderer(self) -> typing.Any
            
            Called when loading a client to create the renderer; this is the only part which should interact
            with client-only code in this class
            :return: A ContainerRenderer instance


        function tick(self, dt: float)

        function is_closable_by_escape(self) -> bool

        function is_always_open(self) -> bool

        function is_blocking_interactions(self) -> bool

        function get_interaction_slots(self)

        function clear(self)

        function copy(self)

        function insert_items(
                self, items: list, random_check_order=False, insert_when_same_item=True
                ) -> list:

            variable skipped

                variable stack

        function insert_item(
                self, itemstack, random_check_order=False, insert_when_same_item=True
                ) -> bool:

            variable slots

                        variable overflow

                        variable slot.itemstack.amount

        function update_shift_container(self)
            
            Called when the inventory should update the content of the ShiftContainer of the inventory-handler
