***PlayerInfoPackages.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class PlayerInfoPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.players

        function setup(self)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

            variable self.players

        function handle_inner(self)

    class PlayerUpdatePackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.name

            variable self.position

            variable self.rotation

            variable self.motion

            variable self.dimension

            variable self.selected_slot

            variable self.gamemode

            variable self.update_flags

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)

                variable self.gamemode