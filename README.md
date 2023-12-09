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
4) In Your local terminal please switch to main branch 
   and pull changes
   `git switch main`
   `git pull`
5) Switch to new_feature branch `git switch new_feature`
6) Perform `git merge main`  

In This step similar message should appear

![Alt text](git_merge_conflict.png?raw=true "Title")
7) solve conflicts 

By choosing Your favourite IDE, please solve conflicts.


![Alt text](solving_conflicts.png?raw=true "Title")

Click `Merge...`

![Alt text](pycharm_merge_conflicts.png?raw=true "Title")

In next step this window should appear.

![Alt text](merge_revision.png?raw=true "Title")

Accept `<< X lane1.book_seat("Ted")` on right side by clicking arrows to remove Adam.

On left side accept `Changes from new_feature` to change `ekiM` to `Mike`

After solving conflicts click `Apply`  and mark as resolved

8) Use "git commit" to conclude merge
9) As last step perform `git push`.
Additionally You can add `--force-with-lease` flag. It is a safer option that will not overwrite any work on the remote branch if more commits were added to the remote branch (by another team-member or coworker or what have you). It ensures you do not overwrite someone elses work by force pushing.
 
