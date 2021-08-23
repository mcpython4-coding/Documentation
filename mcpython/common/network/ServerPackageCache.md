***ServerPackageCache.py - documentation - last updated on 19.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ServerPackageCache
        
        Package Id's have no meaning outside of this cache
        This cache system is for looking up packages send before


        function __init__(self)

        function get_sync_package(
                self,
                ) -> mcpython.common.network.package.PackageCacheSyncPackage.PackageCacheSyncPackage:
            
            Helper method for creating a sync package of this cache


        function sync_from_package(
                self,
                package: mcpython.common.network.package.PackageCacheSyncPackage.PackageCacheSyncPackage,
                ):
            
            Uses a package to sync up this cache with another one


        function prepare_cache_entry(
                self, package: mcpython.common.network.package.AbstractPackage.AbstractPackage
                ):
            
            Prepares the cache for the given package.
            Used when someone wants a package as it had not arrived

            
            Looks up a package in the cache
            :param package_id: the package id
            :return: the package, or None if it is not in the cache

            
            Similar to lookup_package(), but will use request packages to get the original package back from
            other partners in the network
            WARNING: really slow lookup method when not in local cache, use only when really needing packages
            :param package_id: the package id
            :return: the package, or None if it is nowhere arrival


            variable package