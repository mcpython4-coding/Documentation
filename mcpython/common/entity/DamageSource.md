***DamageSource.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class DamageSource
        
        Class direct representing a mc DamageSource
        Used theoretically everywhere; in mcpython, only in API definitions


        function __init__(self, name: str = None)

            variable self.attributes

            variable self.__attributes

            variable self.bypasses_armor

            variable self.bypasses_invulnerability

            variable self.bypasses_magic

            variable self.is_explosion

            variable self.is_fire

            variable self.is_magic

            variable self.is_projectile

            variable self.is_lighting

            variable self.target_entity

            variable self.source_entity

        function setAttribute(self, key, value)

        function getAttribute(self, key)

        function __eq__(self, other)