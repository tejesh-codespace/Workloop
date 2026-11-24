"""WorkLoop AWS Lambda handlers (DynamoDB + S3)."""
import json
import os
import uuid
from datetime import datetime, timezone

import boto3

dynamodb = boto3.resource("dynamodb")
JOBS_TABLE = os.environ.get("JOBS_TABLE", "WorkLoopJobs")
REQUESTS_TABLE = os.environ.get("REQUESTS_TABLE", "WorkLoopRequests")
WORKERS_TABLE = os.environ.get("WORKERS_TABLE", "WorkLoopWorkers")


def _resp(status: int, body: dict) -> dict:
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body),
    }


def post_job(event, context):
    data = json.loads(event.get("body") or "{}")
    item = {
        "jobId": f"j-{uuid.uuid4().hex[:8]}",
        "title": data["title"],
        "role": data["role"],
        "employer": data["employer"],
        "address": data["address"],
        "duration": data["duration"],
        "startDate": data["startDate"],
        "pay": data.get("pay", "Discuss after match"),
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }
    dynamodb.Table(JOBS_TABLE).put_item(Item=item)
    return _resp(201, {"job": item})


def send_request(event, context):
    data = json.loads(event.get("body") or "{}")
    item = {
        "requestId": f"r-{uuid.uuid4().hex[:8]}",
        "jobId": data["jobId"],
        "workerId": data["workerId"],
        "status": "PENDING",
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }
    dynamodb.Table(REQUESTS_TABLE).put_item(Item=item)
    return _resp(201, {"request": item})


def add_work_review(event, context):
    data = json.loads(event.get("body") or "{}")
    table = dynamodb.Table(WORKERS_TABLE)
    worker = table.get_item(Key={"workerId": data["workerId"]}).get("Item") or {}
    history = worker.get("pastWork", [])
    history.insert(0, {
        "employer": data["employer"],
        "duration": data["duration"],
        "rating": str(data["rating"]),
        "review": data["review"],
    })
    table.update_item(
        Key={"workerId": data["workerId"]},
        UpdateExpression="SET pastWork = :h",
        ExpressionAttributeValues={":h": history},
    )
    return _resp(200, {"workerId": data["workerId"], "pastWorkCount": len(history)})
