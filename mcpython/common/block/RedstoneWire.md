***RedstoneWire.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable states

    variable redstone_wire_bbox

    class RedstoneWire extends AbstractBlock.AbstractBlock

        variable NAME: str

        variable HARDNESS

        variable DEBUG_WORLD_BLOCK_STATES

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable NO_ENTITY_COLLISION

        function __init__(self)

            variable self.state

        function get_model_state(self) -> dict

            variable dimension

            variable block

            variable level

                variable self.level

        function update_visual(self)

            variable dimension

            variable block

            variable non_solid_above

                variable block

                        variable self.state[face]

                        variable block2

                            variable self.state[face]

                    variable block

                        variable self.state[face]

        function get_redstone_source_power(self, side: EnumSide) -> int

        function is_connecting_to_redstone(self, side: EnumSide) -> bool

        function get_tint_for_index(
                self, index: int
                ) -> typing.Tuple[float, float, float, float]:

            variable f

        function get_view_bbox(self)