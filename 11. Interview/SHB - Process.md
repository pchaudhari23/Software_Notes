- Production deployments are done by DevOps member.
- DevOps person co-ordinates with the developer of the feature to push the code changes from dev branch to production branch.

-------------------------------------------------------------
Steps:
1.Take pull of the repo in a folder and switch to dev branch.
2.Take pull of same repo in another folder and switch to UAT branch.
3.Open the two folders in WinMerge tool to compare them. 
4.Confirm with the developer about the code changes made in dev branch and the push the code changes in UAT branch.
5.Raise a merge request to merge UAT branch into prod branch.
6.Once approved UAT is merged into prod branch. UAT and prod branches are always in sync.

-------------------------------------------------------------
WinMerge:
- Used to compare the same folder/ repo but two different branches.
- Left panel contains code from dev branch.
- Right panel contains code from UAT branch.
- Compare a particular file. If the code changes made by the developer are regarding the ticket being deployed, shift the snippet from left to right.
- Sometimes both files are made completely identical i.e. whole file is shifted from left to right.
- Sometimes small snippets are shifted. Sometimes new files are added.
- Then commit and push on the UAT branch. And raise merge request.

-------------------------------------------------------------
1. Deploy on NitorAWS - code pushed on develop branch
2. Deploy on UAT - code pushed on UAT branch
3. Deploy on production - code pushed on prod branch

-------------------------------------------------------------
Task end to end process:
- Ticket assigned to dev on JIRA
- Analyse the task, prepare estimate and timeline if big task or change request
- Do unit testing 
- Code reviewed and MR merged by team lead

Dev -> Unit testing -> Deployment Dev server -> QA -> UAT on Dev server -> Deployment on UAT branch -> Deployment on Production branch -> QA on production -> UAT on production -> QC on production -> Assign to CS team to verify with the client

Dev -> QA -> QC -> CS Team -> Client

-----------------------------------------------------------------------------
Coding practices:
Cross Teams work:
Client interaction:
Processes:
Manager:
Business Analyst:
DevOps:
Deployment:
QA Team and QA Lead: QA round OR QA iteration
Dev team: Technical Lead, Architect
CS team:Client/Customer success
TWINTIP TEAM: Cross Teams work

-----------------------------------------------------------------------------
Defend yourself in front of Manager, QA, Client
Handle the conflicts with QA. This is not a bug but expected behaviour. This is invalid bug.

-----------------------------------------------------------------------------
Timelines/ Estimates for the task:
1.Sr. no.
2.Task
3.Total Man Days
4.Start date 
5.End date
6.Status

- Keep some buffer time in between, any schedule or plan must be flexible enough. Release if early completed.

RTM:Requirements Traceability Matrix - Used for testing
Agile: long tasks(epic) broken into smaller tasks (stories) put into two week development cycles (sprints).
Build upgrades

-----------------------------------------------------------------------------