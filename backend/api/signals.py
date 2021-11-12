def populate_models(sender, **kwargs):
    from django.apps import apps
    from .apps import ApiConfig
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    player, created = Group.objects.get_or_create(name=ApiConfig.name)

    models = apps.all_models[ApiConfig.name]
    
    for model in models:
        content_type = ContentType.objects.get(
            app_label=ApiConfig,
            model=model
        )
        permissions = Permission.objects.filter(content_type=content_type)
        player.permissions.add(*permissions)
