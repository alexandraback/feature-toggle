import os
from datetime import datetime

import boto3

from feature_toggle.helper import to_dynamodb
from feature_toggle.models.feature import Feature

DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE)


def main() -> None:
    data = {
        "app_name": "polaris",
        "feat_name": "new-issue",
        "enabled": True,
        "insert_time": datetime(2020, 5, 1, 12, 0, 0),
    }
    feature = Feature.model_validate(data)

    resp = to_dynamodb(table=table, item=feature)
    print(resp)

    # resp = table.scan()
    # print(resp)
