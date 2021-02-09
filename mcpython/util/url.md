***url.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class SimulatedResponse
        
        Simulated response


        function __init__(self, content, is_json, raw=None)

            variable self.content

            variable self.is_json

            variable self.status_code

            variable self.raw

        function json(self)

    function get_url(url, **kwargs)
        
        Gets the content of an URL as an requests.get() or an an SimulatedResponse-instance
        :param url: the url to download from
        :param kwargs: kwargs to requests.get() with
        :return: the content

        
        Async variant of above get_url() method
