from Config.ConfigFileGeneral import ConfigGeneral


class ConfigStaging(ConfigGeneral):
    baseUrl = "https://staging-affiliates.demoskin.com"
    register_api = f"{baseUrl}/global/api/User/registration"
