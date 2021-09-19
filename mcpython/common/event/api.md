***api.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractRegistry extends metaclass=ABCMeta

        function __init__(self)

            variable self.locked

            variable self.phase

            variable self.name

        @abstractmethod
        function is_valid(self, obj)

        @abstractmethod
        function register(self, obj, overwrite_existing=False)
            
            Registers an obj to this registry
            When locked, a RuntimeError is raised
            When an object with the name exists, and overwrite_existing is False, a RuntimeError is raised
            When the object does not extend IRegistryContent, a ValueError is raised
            When the object NAME-attribute is not set, a ValueError is raised


        @abstractmethod
        function entries_iterator(self)

        @abstractmethod
        function elements_iterator(self)

        @abstractmethod
        function lock(self)

        @abstractmethod
        function unlock(self)

        @abstractmethod
        function is_valid_key(self, key)

        @abstractmethod
        function get(self, key, default)

    class IRegistryContent extends mcpython.common.data.serializer.tags.ITagTarget.ITagTarget

        variable NAME

        variable TYPE

        static
        function on_register(cls, registry)

        variable INFO
            can be used to display any special info in e.g. /registryinfo-command, must be str!

        static
        function compressed_info(cls)