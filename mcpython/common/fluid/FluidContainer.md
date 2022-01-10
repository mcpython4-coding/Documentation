***FluidContainer.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FluidContainer extends ABC
        
        Abstract base class for container objects (items, blocks, ...) exposing
        fluid transfers

            
            Informal method for getting the fluids in the container [All of them]

            
            Checks if the container could in theory accept the fluid given.
            When returning False, accept is never called

            
            Inserts a certain amount of fluid
            The fluidstack may contain remaining liquid if not everything could be accepted if insert_parts is True

            
            Checks if the given fluid container can provide the given fluid with the given amount

            
            Removes a certain amount of fluid from the container
            Is allowed to modify the fluidstack when not everything is provided when extract_parts is True
