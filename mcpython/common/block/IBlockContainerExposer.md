***IBlockContainerExposer.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IBlockContainerExposer
        
        Interface for blocks for exposing an inventory this block exposes to the outside

            
            Informal method for getting the items in the container [All of them]

            
            Checks if the container could in theory accept the item given.
            When returning False, accept is never called

            
            Inserts a certain amount of an item
            The itemstack may contain remaining items if not everything could be accepted if insert_parts is True

            
            Checks if the given item container can provide the given item with the given amount

            
            Removes a certain amount of the item from the container
            Is allowed to modify the itemstack when not everything is provided when extract_parts is True


    class SimpleInventoryWrappingContainer extends IBlockContainerExposer,  ABC

            variable working_stack

                    variable delta

            variable working_stack

                    variable delta

            variable working_stack

                    variable delta

            variable working_stack

                    variable delta