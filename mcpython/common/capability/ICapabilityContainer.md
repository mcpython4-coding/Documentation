***ICapabilityContainer.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ICapabilityContainer extends IBufferSerializeAble

        variable CAPABILITY_CONTAINER_NAME

        function __init__(self)

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)

            variable self.capability_data

        function forceAttachmentOfCapability(self, name: str)

        function prepare_container(self)

        function init_container(self)

        function get_capability_content(self, name: str, raw=False)

            variable capability

        function copy_capabilities(self, target: "ICapabilityContainer")

        function copy_capability(self, target: "ICapabilityContainer", name: str)

            variable capability

            variable data

            variable new_data

        function write_raw_capability_data(self, key: str, data)

        function read_raw_capability_data(self, key: str)

        function serialize_container(self)

            variable d

                variable capability

                    variable d[name]

        function deserialize_container(self, data: typing.Optional[dict])

                variable self.capability_data[name]