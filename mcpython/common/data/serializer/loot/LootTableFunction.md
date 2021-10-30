***LootTableFunction.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ILootTableFunction extends mcpython.common.event.api.IRegistryContent

        variable TYPE

        function __init__(self, data: dict)

            variable self.data

        function apply(self, items: list, *args, **kwargs)

    variable loot_table_function_registry

    @shared.registry class ApplyBonus extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.enchantment

            variable self.formula

            variable self.parameters

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class CopyName extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.source

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class CopyNBT extends ILootTableFunction

        variable NAME

    @shared.registry class CopyState extends ILootTableFunction

        variable NAME

    @shared.registry class EnchantRandomly extends ILootTableFunction

        variable NAME

    @shared.registry class EnchantWithLevels extends ILootTableFunction

        variable NAME

    @shared.registry class ExplorationMap extends ILootTableFunction

        variable NAME

    @shared.registry class ExplosionDecay extends ILootTableFunction

        variable NAME

    @shared.registry class FurnaceSmelt extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

                    variable result

                    variable items[i]

    @shared.registry class FillPlayerHead extends ILootTableFunction

        variable NAME

    @shared.registry class LimitCount extends ILootTableFunction

        variable NAME

    @shared.registry class LootingEnchant extends ILootTableFunction

        variable NAME

    @shared.registry class SetAttributes extends ILootTableFunction

        variable NAME

    @shared.registry class SetContents extends ILootTableFunction

        variable NAME

    @shared.registry class SetCount extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class SetDamage extends ILootTableFunction

        variable NAME

    @shared.registry class SetLore extends ILootTableFunction

        variable NAME

    @shared.registry class SetName extends ILootTableFunction

        variable NAME

    @shared.registry class SetNBT extends ILootTableFunction

        variable NAME

    @shared.registry class SetStewEffect extends ILootTableFunction

        variable NAME

    @shared.registry class SetPotion extends ILootTableFunction

        variable NAME