***ServerChangePackage.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ServerChangePackage extends AbstractPackage
        
        Package server -> client sending a request to change the server


        variable PACKAGE_NAME

        function __init__(self)

            variable self.new_server_ip

            variable self.new_server_port

        function set_new_address(self, ip: str, port: int)

            variable self.new_server_ip

            variable self.new_server_port

            variable pair