***BucketItem.py - documentation - last updated on 28.12.2021 by uuk***
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

                variable bucket

    class FilledBucketItem extends AbstractFluidContainer,  ABC

        variable ASSIGNED_FLUID

        variable STACK_SIZE

    @shared.registry class WaterBucket extends FilledBucketItem

        variable NAME

        variable ASSIGNED_FLUID

    @shared.registry class LavaBucket extends FilledBucketItem

        variable NAME

        variable ASSIGNED_FLUID