***AbstractFluidContainer.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractFluidContainer extends mcpython.common.item.AbstractItem.AbstractItem,  ABC
        
        Common base class for container-like items holding fluids


        static
        function get_underlying_fluid_stacks(
                cls, itemstack: mcpython.common.container.ResourceStack.ItemStack
                ) -> typing.Iterable[mcpython.common.container.ResourceStack.FluidStack]:
            
            Informal method for getting the fluids in the container [All of them]


        static
        function could_accept(
                cls,
                itemstack: mcpython.common.container.ResourceStack.ItemStack,
                fluidstack: mcpython.common.container.ResourceStack.FluidStack,
                ) -> bool:
            
            Checks if the container could in theory accept the fluid given.
            When returning False, accept is never called


        static
        function accept(
                cls,
                itemstack: mcpython.common.container.ResourceStack.ItemStack,
                fluidstack: mcpython.common.container.ResourceStack.FluidStack,
                insert_parts=True,
                ) -> bool:
            
            Inserts a certain amount of fluid
            The fluidstack may contain remaining liquid if not everything could be accepted if insert_parts is True


        static
        function can_provide(
                cls,
                itemstack: mcpython.common.container.ResourceStack.ItemStack,
                fluidstack: mcpython.common.container.ResourceStack.FluidStack,
                ) -> bool:
            
            Checks if the given fluid container can provide the given fluid with the given amount


        static
        function provide(
                cls,
                itemstack: mcpython.common.container.ResourceStack.ItemStack,
                fluidstack: mcpython.common.container.ResourceStack.FluidStack,
                extract_parts=True,
                ) -> bool:
            
            Removes a certain amount of fluid from the container
            Is allowed to modify the fluidstack when not everything is provided when extract_parts is True
