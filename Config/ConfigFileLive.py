from Config.ConfigFileGeneral import ConfigGeneral


class ConfigLive(ConfigGeneral):
    baseUrl = "https://affiliates.demoskin.com"
    register_api = f"{baseUrl}/global/api/User/registration"
