***url.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class SimulatedResponse
        
        Simulated response


        function __init__(self, content, is_json, raw=None)

            variable self.content

            variable self.is_json

            variable self.status_code

            variable self.raw

        function json(self)

    variable SIMULATE

    function get_url(url, **kwargs)
        
        gets the content of an URL as an requests.get() or an an SimulatedResponse-instance
        :param url: the url to download from
        :param kwargs: kwargs to requests.get() with
        :return: the content
