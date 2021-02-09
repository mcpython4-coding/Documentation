***ItemAtlas.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable LATEST_INFO_VERSION

    class ItemAtlasHandler

        function __init__(self, folder=shared.build + "/item_atlases")

            variable self.scheduled_item_files

            variable self.folder

        function add_file(self, internal_name: str, file: str)

        function add_file_dynamic(self, internal_name: str, file: str)

                variable image

                        variable self.position_map[file]

                    variable atlas

                    variable self.position_map[file]

                    variable image

            variable self.lookup_map[internal_name]

        function load(self)

        function build(self)

            variable added

                        variable self.position_map[file]

                    variable image

                            variable self.position_map[file]

                        variable atlas

                        variable self.position_map[file]

                    variable self.lookup_map[ref]

                variable image

        function dump(self)

        function get_texture_info(self, name: str)

        function get_texture_info_or_add(self, name: str, file: str)
            
            Save variant for adding an texture to the atlas
            Will ensure that the file is there, but must be fed with the texture file and name
