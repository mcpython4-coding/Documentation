***Inventory.py - documentation - last updated on 26.7.2020 by uuk***
___

    improvements for the future:
    - add option to store under an special directory the data and output the binary data


    @G.registry class Inventory extends mcpython.storage.serializer.IDataSerializer.IDataSerializer
        
        Inventory serializer class


        variable PART

        static
        function load(cls, savefile, inventory: mcpython.gui.Inventory.Inventory, path: str, file=None)
            
            :param inventory: The inventory to save
            :param path: the path to save under
            :param file: the file to save into


            variable data

            variable inventory.uuid

            variable status

        static
        function save(cls, data, savefile, inventory: mcpython.gui.Inventory.Inventory, path: str, file=None, override=False)
            
            :param inventory: The inventory to save
            :param path: the path to save under
            :param file: the file to save into


            variable idata

            variable data[path]