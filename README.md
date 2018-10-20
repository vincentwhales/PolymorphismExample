

## Seeding the database

1. `python manage.py shell`
1. `from projects.models import *`
1. `for i in range(30): ArtProject.objects.create(topic='Art project number:%s' % i)`
1. `for i in range(30): ResearchProject.objects.create(topic='Research project number:%s' % i)`


## Testing CBV works with Polymorphism:

- Visit `http://127.0.0.1:8000/projects/`
- Visit `http://127.0.0.1:8000/projects/art`
- Visit `http://127.0.0.1:8000/projects/research`

