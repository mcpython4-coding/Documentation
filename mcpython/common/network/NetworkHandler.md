***NetworkHandler.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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