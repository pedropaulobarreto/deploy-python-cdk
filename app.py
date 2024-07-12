#!/usr/bin/env python3

import aws_cdk as cdk

from deploy_python_cdk.deploy_python_cdk_stack import DeployPythonCdkStack


app = cdk.App()
DeployPythonCdkStack(app, "DeployPythonCdkStack")

app.synth()
