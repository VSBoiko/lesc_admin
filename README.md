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