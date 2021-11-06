***BucketItem.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class BucketItem extends AbstractFluidContainer

        variable NAME

        variable STACK_SIZE

        static
        function could_accept(
                cls,
                itemstack: ItemStack,
                fluidstack: FluidStack,
                ) -> bool:

        static
        function accept(
                cls,
                itemstack: ItemStack,
                fluidstack: FluidStack,
                insert_parts=True,
                ) -> bool:

        function on_player_interact(
                self, player, block, button: int, modifiers: int, itemstack, previous
                ) -> bool:

                variable bucket

    class FilledBucketItem extends AbstractFluidContainer,  ABC

        variable ASSIGNED_FLUID

        variable STACK_SIZE

        static
        function get_underlying_fluid_stacks(
                cls, itemstack: ItemStack
                ) -> typing.Iterable[FluidStack]:

        static
        function can_provide(
                cls,
                itemstack: ItemStack,
                fluidstack: FluidStack,
                ) -> bool:

        static
        function provide(
                cls,
                itemstack: ItemStack,
                fluidstack: FluidStack,
                extract_parts=True,
                ) -> bool:

        function on_player_interact(
                self, player, block, button: int, modifiers: int, itemstack, previous
                ) -> bool:

    @shared.registry class WaterBucket extends FilledBucketItem

        variable NAME

        variable ASSIGNED_FLUID

    @shared.registry class LavaBucket extends FilledBucketItem

        variable NAME

        variable ASSIGNED_FLUID