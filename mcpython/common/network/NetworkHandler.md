***NetworkHandler.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NetworkHandler

        function __init__(self, side: mcpython.common.network.NetworkConnector.SideType)

            variable self.side

        function register_channel(self, channel: mcpython.common.network.NetworkChannel.Channel)

        function send_package(
                self, package: mcpython.common.network.packages.AbstractPackage.AbstractPackage
                ):

        function fetch_packages(self)

        variable shared.CLIENT_NETWORK_HANDLER

    variable shared.SERVER_NETWORK_HANDLER