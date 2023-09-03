# LECS admin

docker does`t work yet

## project notes
### delete file from git history
[original article](https://docs.github.com/ru/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
) 
* install ```git-filter-repo``` (Fedora`s command)
```shell
sudo dnf install git-filter-repo
```
* remove file by filepath (save file copy, because this command will remove file from project and from git history). Maybe you need to use flag ```--force``` in the end.
```shell
git filter-repo --invert-paths --path PATH-TO-YOUR-FILE-WITH-SENSITIVE-DATA
```
* push
```shell
git push origin master --force
```

### copy file from local to remote
```shell
scp /path/to/file/ user@remote_ip:/path/to/dir/
```
### move file to other dir
```shell
mv /path/to/file/ /path/to/new/dir/
```
### change pg user`s password
```shell
ALTER USER user_name WITH PASSWORD 'new_password';
```

#### [article on resolving django security warnings](https://www.toptal.com/django/secure-django-heroku-pydantic-tutorial-part-4)

#### [how to deploy django project](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru)

#### [what to do with domen in django project](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)

#### [how to integrate DRF and django-filter](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html?highlight=DRF)