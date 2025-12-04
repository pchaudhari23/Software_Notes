Git:

- It is a distributed version control system which is used to track the changes made in the source code file or revert back to previous versions during the development of any project.
- GitHub is owned by Microsoft and was created by Linus Torvald.

FEATURES:

1. Economical - Under GPL (GNU Public Licence)
2. Secure
3. Fast
4. Open Source
5. Lightweight (Does not consume much of the system resources)
6. Distributed
7. Supports parallel, non linear development with the help of branching.

PLATFORMS:

1. GitHub
2. GitLab
3. Bitbucket
4. Sourcetree
5. Tortoise Git

Other Version control systems:

1. Mercurial
2. CVS
3. SVN
4. IBM Rational Clearcase (proprietory)
5. Perforce (proprietory)

---

Step 1: Add files (to the Staging Area)
Step 2: Commit the changes (to Local Repository)
Step 3: Push the changes (to Remote Repository)

1. Pull from remote repository
2. Add a file => commit (to local repository) => push to remote repository

---

COMMANDS:

---

BRANCHING:

- Branching is used when multiple developers are working on the same project but different parts/features/bugs of the project.
- Every developer can create a branch for his or her part of the work code.
- Branch is created from main or develop branch, push the code on particular branch.
- Publish branch: Make branch from local to remote.

MERGE REQUEST/PULL REQUEST:

- A PR should be as small with as minimum changes possible.
- Create Merge request/ Raise Pull request
- Select source branch and destination branch, then create request.
- Assign Reviewer (usually a senior dev or lead from the team): To do code review
- Sometimes live code review is done
- Resolve the comments on PR and reply to comments
- Assign Approver:To have the branch merged into the main branch.
- Branch is merged in develop branch.

So 2 steps - 1.Approve the merge request, 2.Merge the merge request branch

---

CONVENTIONS:
When new project is started: Create three branches from main

1. Production branch
2. Testing or UAT branch
3. Develop branch
4. Feature/Bug branches (created from and merged into develop branch)

- main/master branch : this is root branch, all the code is deployed on this branch - production environment
- develop branch - this branch is created from main branch, all the developer's work and feature developments are merged in this branch and tested. Push this branch in main only if everything is working fine.
- main branch => develop branch (created from main) - all others branches created from develop and merged in develop and tested.
- Feature/Bug branches created from develop branch and raise MR and merge into develop branch once code reviewed and feature is unit tested.
- Take latest pull from develop branch before creating it from develop branch. Before pushing the code, also take latest pull from develop branch so my branch is sync with other developers.
- Don't merge feature or bug branches directly into production, merge them in dev branch only. Merge only dev branch in UAT (after QA signoff) and then UAT branch into Production.
- Delete the feature branch after feature is in production.
- .bak file in repository - Used to take backup or copy of a file.

Branch name convention:
Feature: feature/`<feature name OR ticket name>`
Bug: bug/`<bug name OR ticket name>`

Commit message convention:
Feature: [FEAT `<Feature name or Ticet number>`]
Bug: [FIXED `<Bug name or ticket name>`]
Paritially completed: [WIP `<Feature name OR Ticket name>`]

Comments:
Whenever making code changes to the existing snippet write the comment with date, ticket number and name so that others know
Eg:
//SBK-1212 Start :: Pritam Chaudhari 23/09/2022
Your code changes
//SBK-1212 End

---

QUESTIONS:

1. How do we authenticate a SSH Key?
2. What is origin?
3. forking? - create the same repo in my own github account?
4. local branch vs remote branch?
5. Situation - 1 git: version control, 2 Platforms: Gitlab and GitHub, 3 projects with different email ids
   i. Gitlab - client email id
   ii. Github - company email id
   iii. Contributing to an open source library using my personal gmail email id for github
   How to manage this on a single machine?
6. Enable 2FA for my repo?
7. How to ssh instead of https in git repo?
   ======================================WORK IN PROGRESS=================================================

GitHub commands: (on git bash - go to local repository folder => R click => Git Bash here) (Local Repo)

1. cd : Change to other directory
2. cd .. : go to previous directory
3. pwd: display the current directory
4. ls: display all the files in the current directory
5. mkdir: make a new directory
6. clear: clear the console screen
7. cat `<filename>` : shows the file content in the bash terminal (shell)

---

1. git init: Create an empty local repo
2. git remote add origin "`<url>`" : To link remote repo to local repo
   url => clone or download (green button in remote repo) => copy & paste
3. git pull origin master: pulls all the files from the remote repo to local repo
   OR git pull origin `<branchname>` : to pull from that branch
4. git push origin master: push all the changes from local to remote repo
   git push origin `<branchname>` : to push from that branch
   git push: clone or download => use SSH generate public SSH key and add that to GitHub account
5. git status: to show how many files are added, committed or uncommitted
6. git log: to show the log of recently commited files.
   OR git log --stat: to show log and well as the files which were pushed or committed
7. i. git add `<filename>` : To add only one file
   ii. git add -A : To add multiple files to the staging area
8. i. git commit -m "`<commit message>`" : To commit a single file.
   ii. git commit -a -m "`<commit message>`" : To commit multiple files to local repository
9. ssh -keygen: To generate a ssh key
   |---=> cat `<path>` (.pub extension)
10. Key Authentication:
    i. ssh -T `<ssh url>`
    ii. ssh -keygen -t rsa (In remote repository: Settings=> SSH and CPG keys => New SSH Key => (copy generated SSH key from git bash) => paste => add ssh key)
11. git branch -m master main: change name of master branch to main

---

- To create a repository in remote repository:

* Start a project => Repository name & optional description => public or private??? => Initialize this repository with a README => Add .gitignore: NONE, Add a licence: NONE.
* README => edit => you can write a readme description => Commit changes

---

\*To revert the changes made in a file:
git log => copy commit hash (first 8 HEX digits) of the file you want to revert => git checkout <8 digit HEX> `<filename>`

---

New commands:

1. git branch: to show the branches and on which branch the user currently is
2. git status: to show status of the files in the working directory - which were modified, which are added etc.
3. git fetch: to fetch all the branches.
4. git stash: to stash the changed files before switching to new branch or taking a pull
5. git stash apply: to restore the stash
6. git stash pop: removes the stash

- after popping the stash, developer might get conflicts.
- a conflict occurs when two developers have made changes on the same line.
- developer has 4 options:
  i. accept incoming changes - keeps the change done by developer and discards others change.
  ii. accept current change - keeps the change done by other developer and discards own change.
  iii. accept both changes - keeps the changes done by both the developers
  iv. compare changes -

Note- if you have newly added some files, they will be untracked files, not tracked by the version control system. So stage all the files including untracked ones and then stash

6. git checkout `<branch name>` : switch to a different branch
7. git checkout -b `<branch name>` : to create a new branch from the branch you are currently on and switch on it
8. git branch -d `<branch name>` : delete a branch

---

Steps to commit only some files among number of modified files:

1. git add file1 file2 file3 file4 : to add 4 modified files to staging area
2. git commit -m "commit message" : will commit the 4 files added to staging area

To revert the commits OR uncommit last 'n' commits and keep them in working directory:
git reset --soft HEAD~n~
eg: to revert last 2 commits use - git reset --soft HEAD2

To undo the last commit and discard the changes (completely remove them): git reset --hard HEAD~1

To check which username and email is being used in git:

1. git config user.name
2. git config user.email

---

Scenario: Raised a PR and got conflicts
Solution :
i. Git add and commit OR stage all the changes on current branch
ii. checkout to dev and take a pull
iii. git checkout `<your feature branch>`
iv. git rebase dev

If the problem still there
i. git reflog
ii git stash
iii. git reset --hard "HEAD@{9}"
iv. git rebase --continue

---

Configure your Git username/email:

To set your global username/email configuration:
Open the command line.

Set your username:
git config --global user.name "FIRST_NAME LAST_NAME"

Set your email address:
git config --global user.email "MY_NAME@example.com"

To set repository-specific username/email configuration:
From the command line, change into the repository directory.

Set your username:
git config user.name "FIRST_NAME LAST_NAME"

Set your email address:
git config user.email "MY_NAME@example.com"

Verify your configuration by displaying your configuration file:
cat .git/config

=====================================================================================
GIT MERGE in main before raising PR:
1.Stage and commit
2.Checkout main
3.Pull main
4.Checkout your branch again
5.Do git merge main
6.if any conflicts then resolve conflicts and commit again
7.then test the code
8.then push
9.raise pr

=====================================================================================

- Commit delta changes, only selected files.

---

BUFFER THINGS:

Git:

- git stash clear: clear all stash
- git stash: stash changes
- git stash apply: pop the stash
- commit delta changes
- using vs code git:...
- Draft PR - PR which is just made and not to be merged yet. Work is still in progress
- PR comments - do changes and also reply to comments. replying is also important

MERGE & DEPLOYMENT PROCESS:

dev branch is merged into test and test branch is merged into prod after respective testing

For some user story, multiple developers work on the same branch.

After PR is merged => Jenkins automated pipeline triggered => new build created and deployed on dev instance

- Production deployments are done by DevOps member.
- DevOps person co-ordinates with the developer of the feature to push the code changes from dev branch to production branch.
- Use Filezilla/ WinSCP for transferring file between local and remote computer. Useful for managing build.
- Deploy on NitorAWS - code pushed on develop branch
- Deploy on UAT - code pushed on UAT branch
- Deploy on production - code pushed on prod branch

Dev => Unit testing => Merge, build and deploy on Dev server => QA on dev server by dev => Merge, build and deploy on UAT server => QA on production => Merge, build and deploy on production server => QA on production => UAT on production => QC on production => Assign to CS team to verify with the client

Dev => QA => QC => CS Team => Client

---

WINMERGE:

- Used to compare the same folder/ repo but two different branches.
- Left panel contains code from dev branch.
- Right panel contains code from UAT branch.
- Compare a particular file. If the code changes made by the developer are regarding the ticket being deployed, shift the snippet from left to right.
- Sometimes both files are made completely identical i.e. whole file is shifted from left to right.
- Sometimes small snippets are shifted. Sometimes new files are added.
- Then commit and push on the UAT branch. And raise merge request.

Deployment Steps:

1. Take pull of the repo in a folder and switch to dev branch.
2. Take pull of same repo in another folder and switch to UAT branch.
3. Open the two folders in WinMerge tool to compare them.
4. Confirm with the developer about the code changes made in dev branch and the push the code changes in UAT branch.
5. Raise a merge request to merge UAT branch into prod branch.
6. Once approved UAT is merged into prod branch. UAT and prod branches are always in sync.

---
