***KeyBinding.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class KeyMouseBinding
        
        class holding an key or mouse binding


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