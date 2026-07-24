AWS CLI Commands:

| Use Case                    | AWS CLI Command                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------- |
| **Basic AWS**         |                                                                                                     |
| Configure AWS CLI           | `aws configure`                                                                                   |
| Verify current identity     | `aws sts get-caller-identity`                                                                     |
| Check CLI version           | `aws --version`                                                                                   |
| List configured profiles    | `aws configure list-profiles`                                                                     |
| List all AWS regions        | `aws ec2 describe-regions`                                                                        |
| **EC2**               |                                                                                                     |
| List EC2 instances          | `aws ec2 describe-instances`                                                                      |
| Start an instance           | `aws ec2 start-instances --instance-ids <instance-id>`                                            |
| Stop an instance            | `aws ec2 stop-instances --instance-ids <instance-id>`                                             |
| Reboot an instance          | `aws ec2 reboot-instances --instance-ids <instance-id>`                                           |
| List security groups        | `aws ec2 describe-security-groups`                                                                |
| **S3**                |                                                                                                     |
| List S3 buckets             | `aws s3 ls`                                                                                       |
| List objects in a bucket    | `aws s3 ls s3://<bucket-name>`                                                                    |
| Upload a file               | `aws s3 cp file.txt s3://<bucket-name>/`                                                          |
| Download a file             | `aws s3 cp s3://<bucket-name>/file.txt .`                                                         |
| Sync a directory            | `aws s3 sync ./local-folder s3://<bucket-name>/`                                                  |
| **Lambda**            |                                                                                                     |
| List Lambda functions       | `aws lambda list-functions`                                                                       |
| Get function details        | `aws lambda get-function --function-name <function-name>`                                         |
| Invoke a function           | `aws lambda invoke --function-name <function-name> response.json`                                 |
| Update function code        | `aws lambda update-function-code --function-name <function-name> --zip-file fileb://function.zip` |
| Delete a function           | `aws lambda delete-function --function-name <function-name>`                                      |
| **DynamoDB**          |                                                                                                     |
| List tables                 | `aws dynamodb list-tables`                                                                        |
| Describe a table            | `aws dynamodb describe-table --table-name <table-name>`                                           |
| Get an item                 | `aws dynamodb get-item --table-name <table-name> --key '{"id":{"S":"1"}}'`                        |
| Put an item                 | `aws dynamodb put-item --table-name <table-name> --item file://item.json`                         |
| Scan a table                | `aws dynamodb scan --table-name <table-name>`                                                     |
| **IAM**               |                                                                                                     |
| List IAM users              | `aws iam list-users`                                                                              |
| List IAM roles              | `aws iam list-roles`                                                                              |
| List IAM policies           | `aws iam list-policies`                                                                           |
| Get user details            | `aws iam get-user --user-name <user-name>`                                                        |
| List attached role policies | `aws iam list-attached-role-policies --role-name <role-name>`                                     |

---

AWS SDK for JavaScript v3 – Node.js applications, serverless, frontend integrations

| AWS Service           | JS SDK Package                      |
| --------------------- | ----------------------------------- |
| S3                    | `@aws-sdk/client-s3`              |
| EC2                   | `@aws-sdk/client-ec2`             |
| Lambda                | `@aws-sdk/client-lambda`          |
| DynamoDB              | `@aws-sdk/client-dynamodb`        |
| SQS                   | `@aws-sdk/client-sqs`             |
| SNS                   | `@aws-sdk/client-sns`             |
| IAM                   | `@aws-sdk/client-iam`             |
| STS                   | `@aws-sdk/client-sts`             |
| ECR                   | `@aws-sdk/client-ecr`             |
| ECS                   | `@aws-sdk/client-ecs`             |
| EKS                   | `@aws-sdk/client-eks`             |
| CloudFormation        | `@aws-sdk/client-cloudformation`  |
| CloudWatch            | `@aws-sdk/client-cloudwatch`      |
| CloudWatch Logs       | `@aws-sdk/client-cloudwatch-logs` |
| EventBridge           | `@aws-sdk/client-eventbridge`     |
| Secrets Manager       | `@aws-sdk/client-secrets-manager` |
| Systems Manager (SSM) | `@aws-sdk/client-ssm`             |
| RDS                   | `@aws-sdk/client-rds`             |
| API Gateway           | `@aws-sdk/client-api-gateway`     |
| KMS                   | `@aws-sdk/client-kms`             |

---
