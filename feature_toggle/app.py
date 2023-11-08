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
    }
    feature = Feature.model_validate(data)
    print(feature.model_dump())

    # resp = to_dynamodb(table=table, item=feature)
    # print(resp)

    # resp = table.scan()
    # print(resp)
