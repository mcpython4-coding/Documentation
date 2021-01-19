***DamageSource.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class DamageSource
        
        Class direct representing an mc DamageSource


        function __init__(self, name: str = None)

            variable self.attributes

            variable self.__attributes

            variable self.type

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