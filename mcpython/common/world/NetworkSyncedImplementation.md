***NetworkSyncedImplementation.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NetworkSyncedDimension extends Dimension
        
        Class holding a whole dimension on a client connected to a dedicated server


        function get_chunk(
                self,
                cx: typing.Union[int, typing.Tuple[int, int]],
                cz: int = None,
                generate: bool = True,
                create: bool = True,
                ) -> typing.Optional["NetworkSyncedChunk"]:

    class NetworkSyncedChunk extends Chunk

        function add_block(
                self,
                *args,
                network_sync=True,
                **kwargs,
                ):

            variable b

        function remove_block(self, *args, network_sync=True, **kwargs)