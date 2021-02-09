***NetworkConnector.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class SideType extends enum.Enum

        variable CLIENT

        variable SERVER

    class AbstractNetworkConnection extends ABC

        function __init__(self, side: SideType)

            variable self.side

        function send_data(self, data: bytes)

        function has_data(self) -> bool

        function receive_package(self) -> typing.Iterator[bytes]

    class SocketNetworkConnection extends AbstractNetworkConnection

    class ClientInnerServerConnection extends AbstractNetworkConnection