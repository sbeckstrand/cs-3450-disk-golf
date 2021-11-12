from .apps import ApiConfig

def is_in_group_players(user):
    return user.groups.filter(name=ApiConfig.name).exists()
    