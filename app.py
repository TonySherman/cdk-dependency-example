#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_dependency_example.cdk_dependency_example_stack import (
    CdkDependencyExampleStack,
)
from cdk_dependency_example.dynamo_table_stack import TableStack


app = cdk.App()

env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION"),
)


table_stack = TableStack(
    app,
    "TableStack",
    env=env,
)


CdkDependencyExampleStack(
    app,
    "CdkDependencyExampleStack",
    env=env,
    stream_arn=table_stack.table.table_stream_arn,
)

app.synth()
