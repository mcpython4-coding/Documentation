***api.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class BlockStateNotNeeded extends Exception

    @onlyInClient() class IBlockStateRenderingTarget

        variable NAME

        function __init__(self)

            variable self.block_state

            variable self.position

            variable self.face_info

        function get_model_state(self)

        function get_tint_for_index(
                self, index: int
                ) -> typing.Tuple[float, float, float, float]:

    @onlyInClient() class IBlockStateDecoder extends mcpython.common.event.api.IRegistryContent,  ABC
        
        Abstract base class for block state decoders
        Identification of files to decode:
            bool(is_valid(data)) == True, where data is the loaded json data
            for developers of mods: add an entry called "mod_marker" storing the mod name the loader is implemented in and
                check for it here
        Loading:
            __init__(data, BlockStateDefinition) -> Instance
        Baking:
            bake() is called to on_bake references and do similar stuff, returning success or not
        Drawing:
            add_face_to_batch() should add the given face to the batches given
            add_raw_face_to_batch() should add a face to the batch without the block instance, but instead the position
            draw() should draw the block in-place
        todo: cache non-offset data from models per state for faster drawing
        todo: can we do something rendering wise which will make it efficient to draw multiple same blocks
        todo: block batches should be selected before, based on a property on block class


        variable TYPE

        static
        function is_valid(cls, data: dict) -> bool
            
            Checker function if some data matches the loader


        function __init__(self, block_state)

            variable self.data

            variable self.block_state

        function parse_data(self, data: dict)

        function bake(self) -> bool
            
            Bake method for doing some stuff after loading all block-states
            :return: if successful or not


        function add_face_to_batch(
                self,
                instance: IBlockStateRenderingTarget,
                batch: pyglet.graphics.Batch,
                face: mcpython.util.enums.EnumSide,
                ) -> list:

        function add_raw_face_to_batch(
                self, instance: IBlockStateRenderingTarget, position, state, batches, faces
                ):

        function draw_face(
                self,
                instance: IBlockStateRenderingTarget,
                face: mcpython.util.enums.EnumSide,
                ):

        function transform_to_bounding_box(
                self,
                instance: IBlockStateRenderingTarget,
                ):

    @onlyInClient() class IItemModelLoader

        static
        function validate(cls, data: dict) -> bool

        static
        function decode(cls, data: dict, model)

    @onlyInClient() class AbstractBoxModel extends ABC

        function copy(self) -> "AbstractBoxModel"