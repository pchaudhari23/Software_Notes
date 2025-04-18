CICD Pipeline - Code from one end, deployment on other end.
Stages:
CI: Commit => Merge
CD: Package => Build => Deploy

---

Deployment techniques:

1. In Place deployment: Application on instance stopped, new version deployed and application started again. No new instances are created.
2. Rolling: Deployed on instances one by one. Number of instances compromised. A rolling deployment is generally faster than a blue/green deployment.
3. Rolling with additional batches: Preserve full instance capacity
4. Blue Green: All the traffic redirected immediately to new version on new instances by swapping cname
5. Immutable: Deploy the new version to a fresh group of instances by performing an immutable update.
6. All at once: All traffic shifted from one version to another in one go
7. Linear: Equal increments in equal number of minutes
8. Traffic Splitting/ Canary deployment: First route some % for some minutes then remaining % in two increments

---

Deployment platforms:

1. EC2
2. On Premises
3. ECS
4. Elastic Beanstalk - Rolling with additonal batch, Immutable
5. Lambda: Canary deployment
6. CloudFormation

---

1. Blue Green: Elastic Beanstalk, OpsWorks, CloudFormation, CodeDeploy, and Amazon ECS.
2. Rolling deployment: CloudFormation, ECS, Elastic Beanstalk, OpsWorks
3. In Place deployment: CodeDeploy

---

Deployment methods using Code deploy:

1. On Premises: In Place
2. EC2: In Place, Blue Green
3. ECS: Blue Green - all at once/linear/canary
4. Lambda: Blue Green, does not support in place deployment. Two versions are created and use all at once/linear/canary

---
