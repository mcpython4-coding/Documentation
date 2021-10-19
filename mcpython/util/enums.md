***enums.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable COLORS

    class EnumSide extends enum.Enum
        
        Enum holding the 6 different sides of an Block.
        Also used for defining axis where it points in the direction


        variable TOP

        variable BOTTOM

        variable NORTH

        variable EAST

        variable SOUTH

        variable WEST

        static
        function iterate(cls)
            
            Iterator for the faces


        function __init__(self, dx: int, dy: int, dz: int, normal_name: str, index: int)
            
            Constructs a new enum instance
            :param dx: the delta in x
            :param dy: the delta in y
            :param dz: the delta in z
            :param normal_name: the normal name of the face


            variable self.relative

            variable self.normal_name

            variable self.index

        function invert(self)
            
            Will invert the face to its opposite
            :return: the opposite face


        function relative_offset(self, position)

        function __eq__(self, other)

        function __hash__(self)

        function rotate(self, rotation: tuple)

        function rotate_reverse(self, rotation: tuple)

        function as_bit(self) -> int

    variable FACE_ORDER: typing.List[EnumSide]

    variable FACE_ORDER_HORIZONTAL

    variable ROTATE: typing.List[typing.List[EnumSide]]
        How to rotate the different faces?

    variable HORIZONTAL_OFFSETS

    class LogAxis extends enum.Enum

        variable X

        variable Y

        variable Z

    class ToolType extends enum.Enum

        variable HAND

        variable PICKAXE

        variable AXE

        variable SHOVEL

        variable SHEAR

        variable SWORD - not real an tool, but internally handled as one of it

        variable HOE - not real an tool, but internally handled as one of it

    class SlabModes extends enum.Enum

        variable TOP

        variable BOTTOM

        variable DOUBLE

    class LoadingStageStatus extends enum.Enum

        variable WORKING

        variable MOD_CHANGED

        variable EVENT_CHANGED

        variable FINISHED

    class ButtonMode extends enum.Enum

        variable DISABLED

        variable ENABLED

        variable HOVERING

    class NormalWoodTypes extends enum.Enum

        variable ACACIA

        variable BIRCH

        variable SPRUCE

        variable JUNGLE

        variable OAK

        variable DARK_OAK

        function __init__(self, name: str)

            variable self.data_name

        function __hash__(self)

        function __eq__(self, other)

        function __repr__(self)

    class NetherWoodTypes extends enum.Enum

        variable CRIMSON

        variable WARPED

        function __init__(self, name: str)

            variable self.data_name

        function __hash__(self)

        function __eq__(self, other)

        function __repr__(self)

    function all_woods()

    class BlockRotationType extends enum.Enum

        variable ROTATE_Y_90

        variable ROTATE_Y_180

        variable ROTATE_Y_270

        variable FLIP_Y

        variable ROTATE_X_90

        variable ROTATE_X_180

        variable ROTATE_X_270

        variable FLIP_X

        variable ROTATE_Z_90

        variable ROTATE_Z_180

        variable ROTATE_Z_270

        variable FLIP_Z