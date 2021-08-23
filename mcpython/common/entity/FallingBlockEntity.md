***FallingBlockEntity.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class FallingBlockEntity extends mcpython.common.entity.AbstractEntity.AbstractEntity
        
        Class for the falling block entity
        todo: can we replicate some original block behaviour, like inventories, interaction, ...?


        variable NAME

        function __init__(self, *args, representing_block=None, **kwargs)

            variable self.block - todo: store in nbt

            variable self.nbt_data["motion"]

        function draw(self)

        function tick(self, dt)

            variable block