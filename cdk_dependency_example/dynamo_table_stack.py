from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct

from settings import StackSettings


class TableStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ):
        super().__init__(scope, construct_id, **kwargs)

        settings = StackSettings()

        self.table = dynamodb.Table(
            self,
            'DemoTable',
            partition_key=dynamodb.Attribute(name='PK', type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name='SK', type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY,
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            table_name=settings.TABLE_NAME,
            stream=dynamodb.StreamViewType.NEW_IMAGE,
            point_in_time_recovery=settings.POINT_IN_TIME_RECOVERY,
        )

        self.table.add_global_secondary_index(
            index_name='QueryIndex',
            partition_key=dynamodb.Attribute(name='GSI1PK', type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name='GSI1SK', type=dynamodb.AttributeType.STRING),
        )
