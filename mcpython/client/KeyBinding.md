***KeyBinding.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class KeyMouseBinding
        
        Class holding a key or mouse binding


        function __init__(
                self,
                name: str,
                group_name: str,
                default: typing.Union[int, typing.Iterable[int]],
                default_mod: typing.Union[int, typing.Iterable[int]] = 0,
                ):

            variable self.name

            variable self.group_name

            variable self.key_or_button

            variable self.mod

        function applies(self, key_or_button: int, mod: int) -> bool