Cloud Development Kit (CDK):

EC2 - Amazon Elastic Compute Cloud

Cloud computing - Iaas, PaaS, SaaS
IaaS => Virtual Machine
EC2 Instance => Iaas, Lambda => PaaS, PowerBI => SaaS

Apps => Stacks => Constructs

Stacks => Classes
Constructs => allows you to configure services
Constructs are basic building blocks of CDK application

Constructs -
i. scope - this
ii. id - some unique string
iii. props - Object

const constructName = new construct(scope,id, {propslist Object - key and value pair})
OR
new construct(...,....,....);

L1(Lower level) - Explicitly configure all resource properties
L2(Higher level) - Some properties are cofigured by default

cloud formation template - used to create construct resources (eg: S3 bucket, Lambda function, Dynamo db instance) - text file JSON or YAML format

Commands to run on terminal:
cdk doc: open cdk documentation
cdk diff: shows differences between deployed stuff and what is coded locally
cdk deploy: deploy the changes
cdk destroy: remove some the deployed resource
cdk destroy --all: remove all the deployed resources
cdk synth: to generate cloud formation template

first cd to that folder -
npm init -y: mono repo - project inside another project

transpile???

CODE: Create Lambda function with CDK

import {
APIGatewayProxyEventV2,
APIGatewayProxyResultV2,
Context
} from 'aws-lambda';

async function getPhotos(
event: APIGatewayProxyEventV2,
context: Context
) : Promise <APIGatewayProxyResultV2> {
return {
statusCode: 200,
body: 'I am in lambda'
};
}

export { getPhotos };

---

cdk.CfnOutput(this,id,{
value: '......',
exportName: '......'
}
);

AWS CDK, AWS CLI, typescript - install globally

cdk bootstrap

---
