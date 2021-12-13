***ItemEntity.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ItemEntity extends mcpython.common.entity.AbstractEntity.AbstractEntity
        
        Class for the item entity in the world
        Experimental!
        todo: add real item rendering
        todo: check during attraction for collisions with blocks


        variable NAME

        variable SUMMON_ABLE

        variable ATTRACTION_DISTANCE
            todo: make this decidable by the item

        variable PICKUP_DISTANCE

        variable ATTRACTION_SPEED

        function __init__(
                self, *args, representing_item_stack: ItemStack = None, pickup_delay=0, **kwargs
                ):

            variable self.item_stack

            variable self.pickup_delay

            variable self.test_block
                todo: fetch real item model here

            variable self.test_block.dimension
                Set the block dimension so the block can do cool stuff with rendering if it wants to

        function draw(self)

            variable self.test_block.position
                Set the block position so it knows where it is

                variable self.test_block

                variable self.pickup_delay

                    variable p

                    variable p

                    variable d

                        variable v

                        variable v

                        variable self.position

                variable self.item_stack

            variable self.pickup_delay