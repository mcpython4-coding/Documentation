***ItemAtlas.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable LATEST_INFO_VERSION

    class ItemAtlasHandler

        function __init__(self, folder=shared.build + "/item_atlases")

            variable self.scheduled_item_files

            variable self.folder

        function add_file(self, internal_name: str, file: str)

        function add_file_dynamic(self, internal_name: str, file: str)

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
