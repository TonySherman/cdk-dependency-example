from pathlib import Path
from aws_cdk import (
    Stack,
    aws_dynamodb,
    aws_lambda,
    aws_lambda_event_sources,
)
from constructs import Construct

from settings import StackSettings


class CdkDependencyExampleStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        stream_arn: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        settings = StackSettings()

        table = aws_dynamodb.Table.from_table_attributes(
            self,
            "DemoTable",
            table_name=settings.TABLE_NAME,
            table_stream_arn=stream_arn,
        )

        lambda_function = aws_lambda.Function(
            self,
            "DemoLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler="main.handler",
            code=aws_lambda.Code.from_asset(f"{Path(__file__).parent}/lambda_code"),
        )

        lambda_function.add_event_source(
            aws_lambda_event_sources.DynamoEventSource(
                table=table,
                starting_position=aws_lambda.StartingPosition.TRIM_HORIZON,
            )
        )

