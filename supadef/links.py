from .config import SERVICE_ENDPOINT


# this is silly? yagni? or nah?
# perhaps if it's constrained to routes for user-specific data
# strictly GET requests (or ws 'GET's). no other operations encoded here
def route(slug: str, loader=False) -> str:
    slug_to_pattern = {
        'user': '/{username}',
        'user > billing': '/{username}/billing',
        'user > account': '/{username}/account',
        'user > project': '/{username}/{project_name}',
        'user > project > functions > run': '/fn/run/{run_id}',
        'user > project > danger zone': '/{username}/{project}/danger_zone',
        'user > project > env': '/{username}/{project}/env',
        'docs > cli > supadef connect': '',
        'supadef connect': '/email',
        'supadef projects': '/projects',
        'supadef create': '/project',
        'supadef logs': '/fn/logs/{run_id}',
        'supadef push': '/project/{name}/upload_package',
        'supadef run': '/run',
        'supadef destroy': '/project',
        'supadef set_env': '/project/{name}/set_env'
    }
    if slug not in slug_to_pattern.keys():
        raise ValueError(f'no such slug: {slug}')

    pattern = slug_to_pattern[slug]
    if loader:
        pattern = pattern + '/content_html'

    return pattern


def link(slug: str,
         loader=False,
         username: str = None,
         project_name: str = None,
         run_id: str = None,
         service_endpoint: str = SERVICE_ENDPOINT) -> str:
    subs = {
        'username': username,
        'project_name': project_name,
        'run_id': run_id
    }
    pattern = route(slug, loader).format(**subs)

    return service_endpoint + pattern

