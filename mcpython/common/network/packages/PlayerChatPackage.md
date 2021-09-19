***PlayerChatPackage.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class PlayerChatInputPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.text

        function setup(self, text: str)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)

                variable text

    class PlayerMessageShowPackage extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.text

        function setup(self, text: str)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)

    class PlayerClientCommandExecution extends AbstractPackage

        variable PACKAGE_NAME

        function __init__(self)

            variable self.text

        function setup(self, text: str)

        function write_to_buffer(self, buffer: WriteBuffer)

        function read_from_buffer(self, buffer: ReadBuffer)

        function handle_inner(self)