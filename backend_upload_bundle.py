from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import boto3, os

app = FastAPI()
# Allow requests from your frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],             # or ["http://localhost:5177"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

@app.post("/api/upload-bundle/")
async def upload_bundle(file: UploadFile = File(...)):
    content = await file.read()
    if not content:
        raise HTTPException(400, "Empty file")
    bucket = os.getenv('S3_BUCKET')
    key = f"bundles/{file.filename}"
    s3.put_object(Bucket=bucket, Key=key, Body=content)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=3600
    )
    return {"url": url}
