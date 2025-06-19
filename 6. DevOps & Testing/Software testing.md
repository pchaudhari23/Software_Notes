SOFTWARE TESTING:

| **Type**                         | **Description**                                                              |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **Alpha Testing**                | Done by internal teams before releasing to external users.                   |
| **Beta Testing**                 | Done by a limited number of external users before full release.              |
| **Sanity Testing**               | Quick checks to ensure specific functionalities work after changes.          |
| **Regression Testing**           | Ensures new code changes don't break existing features.                      |
| **Unit Testing**                 | Done by developers before committing code and raising a merge request.       |
| **Smoke Testing**                | Basic tests to confirm the build is stable enough for further testing.       |
| **Ad-hoc Testing**               | Unstructured testing to find defects without predefined test cases.          |
| **Penetration Testing**          | Security testing to find vulnerabilities. Often handled by security experts. |
| **UAT(User Acceptance Testing)** | Done by client                                                               |

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

Regression testing: Done to check if fix does not break existing
Sanity testing:
Unit Testing - Test a feature before releasing to QA. Fixing a bug or developin a feature should not break something else.

RTM:Requirements Traceability Matrix - Used for testing

QA shares the test plan while development is in progress

- FVT test cases
- Test suite

---

- Try out, install new softwares
- Explore its features
- Test it, find its limitations and bugs

---

Exploring apps similar to what we are building.
Testing and exploring the features of our competitor apps.

---

QA sequence => Test Sandbox(dev) => Test Production Validation
QC => Test Production Live => QA should not place orders on live
