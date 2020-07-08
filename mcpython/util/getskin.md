***getskin.py - documentation - last updated on 4.7.2020 by uuk***
___

    variable DEBUG

    variable SIMULATE

    variable userid_url

    variable userinfo_url

    class SimulatedResponse
        
        Simulated response


        function __init__(self, content, is_json, raw=None)

            variable self.content

            variable self.is_json

            variable self.status_code

            variable self.raw

        function json(self)

    function find_texture_info(properties)

    function get_url(url, **kwargs)
        
        gets the content of an URL as an requests.get() or an an SimulatedResponse-instance
        :param url: the url to download from
        :param kwargs: kwargs to requests.get() with
        :return: the content


    function download_skin(username: str, store: str)
        
        will download skin data for an user name
        :param username: the user to download for
        :param store: where to store the data
        :raises ValueError: raised when an error occurred during retrieving the data
        Will also store data in an cache for later usage


            variable r

        variable userid

        variable r

        variable userinfo

            variable texture_info

        variable skin_url

        variable r

        variable image

            variable new_image