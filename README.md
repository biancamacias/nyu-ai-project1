# NYU CS-UY 4613 Project 1

By Isabel Huey and Bianca Macias
Project 1, coded in Python

## How to create a new branch via command line

1. Make sure you are in the main branch.
 ```
 $ git checkout master
 ```
2. Create new branch (which is branched off of main).
```
$ git checkout -b [branch name]
```
3. Start working on your new branch!

## How to commit changes

NOTE: commit often!

1. Make sure there are changes to commit.
```
$ git status
```
2. Add all the files you want to commit (they will be in red, files already
   added to be committed will be green)
```
$ git add [filename]
```
3. Once you've added all your files to be committed, commit it with a message.
```
$ git commit -m "fixed bug in function loop"
```

## How to push changes after you've committed

1. If you've never pushed to the repo, first set upstream to origin.
```
$ git push --set-upstream origin [current branch name]
```

2. Push changes after new commits.
```
$ git push
```
