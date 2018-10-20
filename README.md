

## Seeding the database

```
$ python manage.py shell

>>> from projects.models import *
>>> for i in range(30): ArtProject.objects.create(topic='Art project number:%s' % i)

>>> for i in range(30): ResearchProject.objects.create(topic='Research project number:%s' % i)
```


## Testing CBV works with Polymorphism:

- Visit `http://127.0.0.1:8000/projects/`
- Visit `http://127.0.0.1:8000/projects/art`
- Visit `http://127.0.0.1:8000/projects/research`


## Verify that querying works

```
$ python manage.py shell

>>> from projects.models import *

>>> Project.objects.filter(topic='Art project number:29').get()
<ArtProject: Art project number:29>
```


## DRF

1. Visit `http://127.0.0.1:8000/api/projects/`
