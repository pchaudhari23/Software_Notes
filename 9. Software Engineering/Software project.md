SOFTWARE DEVELOPMENT:

---

SOFTWARE TESTING:

---

SOFTWARE PROJECT:

People, Team members and their roles:
Manager:
Business Analyst:

---

AGILE:

======================================WORK IN PROGRESS====================================================

SOFTWARE DEVELOPMENT:
Product design
Product development

Environment:

1. Development
2. UAT, Test environment
3. Production

Environments: Usually for API based projects
Sandbox - Dev (Development and testing on dev)
Production - Test (For production testing)
Production - Live

---

SOFTWARE TESTING:

- UAT - client does it

Project Testing:

1. Alpha testing
2. Beta testing
3. Sanity testing
4. Regression testing
5. Unit testing
6. Smoke testing
7. Adhoc testing
8. Penetration testing
   Unit testing - done by developers before commiting and creating a merge request
   Testing happens in both Dev and production environments.
   Once deployed on dev - then test.
   Then deployed on prod - then test.

QA - Quality Assurance - Done during software development life cycle
QC - Quality Control - Done during software testing life cycle, after production release.
QC done by Client side software tester.

Intermittent issues - Issues unable to reproduce on dev and QA end.

- Try to force the error, try o simulate it if there are no steps to reproduce it. And then fix the code or handle such errors and situations in the code.

---

PROJECT:
SDLC - Software Development Lifecycle
STLC - Software Testing Lifecycle

- Client Demo
- Project flows
- Branching strategy, naming conventions
- Tools used for the project - gitlab, git tortoise, devops tools, jira, azure devops etc.
- Setup process to be followed
- Deployment process
- Migration activity - Migrating backend or cloud platform
- POC - small demo to gain customer confidence. POC is prepared before starting a project and shown to customer.
- Timelines/Estimate for a feature development
- Resource sharing between multiple projects
- Client Interviews
- Resource billling from client
- Change requests (CRs)
- Deployment
- KTs
- Escalations?
- Code freeze
- Freelancing?
- Business Analyst? - Decides the business logic, the project requirements
- Product documentation
- Project management - Azure Devops, JIRA
- Wikis about the project - Knowledge article for others reference
- Query logs - for any questions to be answered by client
- DevOps - Developers and Person from opeartions
- Audits?
- Client is aggressive and bossy
- Client does not know programming, he is a non technical person
- Understanding the business requirements and developing the business logic for that.
- Set a process, follow a process. Process: Sequence of actions. What to do, what steps to follow when something happens.
- Project deliverables
- Cross teams communication. When multiple teams are working on same project.
- Project culture - The way we do things around here to succeed. Represents the shared norms, beliefs, values, and assumptions of the project team. How are the team members, how is the manager. Who is good who is bad? Who is helpful, who is reliable? who has attitude? how is coordination between dev and QA? Such things
- Daylight saving meeting time adjustments
- Holiday deployment and code freeze
- No pushing to prod on Friday
- Coding test and client interview of billable resource before project onboarding

Meetings:

1. Kickoff meeting
2. Scrum meeting
3. Standup meeting
4. Sprint planning
5. Retrospective meetings - after sprints - 1.what went well? 2.what didn't go well?? 3.what could have been done better?

Sprint:

- Create stories but dont keep it in current sprint. Created backlog items. After sprint completion, pickup backlog items. Assign it story points - fibonnaci.
- Be liberal in assigning story points, considering buffer time.

- Meeting MOM (Minutes Of Meeting)
- Dev & QA => Client => Client's client or End Users
- Release management and Business approval

---

Shadowbox: Agile project
2 managers
QA team
Devloper team
2 devops
2 business analysts - (they are doctors)

Developers and testers must understand business requirements first. That is the source of knowledge for both. If both are on the same page only then the project can happen otherwise there will be miscommunication and conflicts between devs and QA.

===============================================================================================

Service based organisation:
Resource billing
Shadow resources
How does that organisation earn revenue?
How much does the client pay?
When does he do cost cutting?
How is the client?

Dev:

- Sandbox
  Prod:
- Production validation
- Production live

QA sequence => Test Sandbox(dev) => Test Production Validation
QC => Test Production Live => QA should not place orders on live

- Explore the GitHub repo of any product or library. To know how company or open source technology works technically.
- Upgrading dependencies/libraries during ongoing project? Usually we don't upgrade to latest versions immediately, we wait for it to become stable?
- After PR is merged => Jenkins automated pipeline triggered => new build created and deployed on dev instance
- Write project documentation. MD file or story book. Developer guide. For new devs joining the team.
- Spillovers
- Adding the JIRA tickets in backlog.
- Sprint planning
- Retrospective meetings
