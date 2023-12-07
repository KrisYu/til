# git view a file in commit 


[View the change history of a file using Git versioning](https://stackoverflow.com/questions/278192/view-the-change-history-of-a-file-using-git-versioning)

```
git log -p file 
```


[How can I view an old version of a file with Git?](https://stackoverflow.com/questions/338436/how-can-i-view-an-old-version-of-a-file-with-git)

```
git show HEAD@{2013-02-25}:./fileInCurrentDirectory.txt
```