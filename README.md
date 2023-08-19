# LECS admin

docker does`t work yet

## project notes
### delete file from git history
* install ```git-filter-repo```
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