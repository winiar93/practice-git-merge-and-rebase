# Git Merging and Rebasing Exercises

Welcome to the Git Merging Exercises repository! 
This repository is designed to provide practice exercises 
for understanding and mastering Git merging and rebasing.

Before start please fork this repo.


# Practice merge 


1) Switch to branch main
2) Add new passenger `Ted` between `Alice` and `Bob`
   `plane1.book_seat("Ted")`. 
    Please use github editor to make a changes.
3) Commit changes 

In this way we will generate a conflict in futher steps.
```
Conflict in git is situation  when two people have changed the same lines in a file, 
or if one developer deleted a file while another developer was modifying it. 
In these cases, Git cannot automatically determine what is correct.
```

4) In Your local terminal please switch to main branch 
   and pull changes
   `git switch main`
   `git pull`
5) Switch to new_feature branch `git switch new_feature`
6) Perform `git merge main`  

In This step, a similar message should appear:

![Alt text](git_merge_conflict.png?raw=true "Title")

7) solve conflicts 

By choosing Your favourite IDE, please solve conflicts.


![Alt text](solving_conflicts.png?raw=true "Title")

Click `Merge...`

![Alt text](pycharm_merge_conflicts.png?raw=true "Title")

In the next step, this window should appear.

![Alt text](merge_revision.png?raw=true "Title")

Accept `<< X lane1.book_seat("Ted")` on right side by clicking arrows to remove Adam.

On left side accept `Changes from new_feature` to change `ekiM` to `Mike`

After solving conflicts click `Apply`  and mark as resolved

8) Use "git commit" to conclude merge
9) As last step perform `git push`.
Additionally You can add `--force-with-lease` flag. It is a safer option that will not overwrite any work on the remote branch if more commits were added to the remote branch (by another team-member or coworker or what have you). It ensures you do not overwrite someone elses work by force pushing.


 # Practice rebase

1) Reset changes on both branches by performing `git reset --soft HEAD~1`
2) Repeat same steps until point 6
3) Insted `git merge main` command perform `git rebase main`
4) Solve conficts
5) Commit changes and push them
6) Verify history using `git log` ( press `q` to exit )

# What is difference between merge and rebase?

Both merge and rebase are used in Git to integrate changes from one branch into another, but they do so in different ways and have distinct implications for the commit history and project workflow.

## Merge:

`Merge Commit`: When you perform a merge, Git creates a new commit that combines the changes from the source branch into the target branch. This new commit is known as a "merge commit."

`Preserves History`: The commit history of both branches remains intact. Merge commits show the point at which the branches were merged.

`Clarity of Changes`: Merging explicitly shows separate branches' development and the exact point where they were merged.


## Rebase:

`Linear History`: Rebase rewrites the commit history by moving the entire branch to the tip of the target branch, incorporating the commits one by one. It does this by essentially replaying the commits on top of the target branch.

`No Merge Commits`: Unlike merge, rebase doesn't create a merge commit. Instead, it replants the commits from one branch onto another, resulting in a linear sequence of commits.

`Cleaner History`: Rebase offers a cleaner history as it eliminates unnecessary merge commits, resulting in a straight and more linear commit history.
   
