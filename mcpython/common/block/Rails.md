***Rails.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable SHAPES

    class IRail extends AbstractBlock,  ABC

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable NO_ENTITY_COLLISION

        function is_currently_orientated_for_side(self, side: EnumSide, up: bool) -> bool

    class IStraightRail extends IRail,  ABC

        function __init__(self)

            variable self.shape

        function get_model_state(self) -> dict

                variable self.shape

            variable dimension

            variable connecting_faces

                variable block

                    variable self.shape

                    variable self.shape

        function is_currently_orientated_for_side(self, side: EnumSide, up: bool) -> bool

    class ActivatorRail extends IStraightRail

        variable NAME

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS

        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)

            variable self.force_active

        function get_model_state(self) -> dict

                variable self.force_active

    class PoweredRail extends ActivatorRail

        variable NAME

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS

    class DetectorRail extends ActivatorRail

        variable NAME

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS