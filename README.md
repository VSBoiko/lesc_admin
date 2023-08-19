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
### change ph user`s password
```shell
ALTER USER user_name WITH PASSWORD 'new_password';
```
