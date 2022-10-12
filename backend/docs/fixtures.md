To dump data about dishes, categories, vendors, and customer use this command.

```sh
$ python -Xutf8 .\manage.py dumpdata -o fixtures/demo_data.json --indent 4 --exclude admin --exclude contenttypes --exclude sessions --exclude auth.p
ermission --exclude auth.group
```
