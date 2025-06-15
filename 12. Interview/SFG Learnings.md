Exploring the codebase. Spending time daily - 30 min
1.b2bi-ui-shared
i.packages - build-lib - login - sample-app

2.gatewayui
i.sfg-sanity-test
ii.sfg-ui

- craco config contains package aliases
- babel.config.js: file used for javascript compiler babel so that modern javascript can be used on current/old browsers

---

- Uses monorepo architecture
- uses yarn workspaces and turborepo build system

---

Snippets:
const { page } = Shell.usePage(
[],
(function Page(pageUtil) {
return {
// model, form, datasources, datatable, ui, observers, init, functions ... etc
})(pageUtil)
);

const pageConfig = {}

JSX:
Shell.Page
Shell.PageHeader => title, description
Shell.PageBody => CDS.Form => Grid
Shell.PageActions

CDS:

---

React hook form:

---

Shell:

---

E2E testing, BDD, Playwright & Cucumber:

- FVT

---

Storybook:

---

CRACO:

---

Checkmarx, security scans, Blackduck scan:

---

- File or folder?
- Markdown or notion?
- Every month activity
- No common knowledge, just related to code
- No confidential code/data

---
