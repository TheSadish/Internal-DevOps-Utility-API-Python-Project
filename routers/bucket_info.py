from fastapi import APIRouter, HTTPException
from services import aws_service

router = APIRouter()

@router.get("/s3")
def get_bucket():
    '''
    This API will fetch all the buckets from AWS
    '''
    try:
        buckets = aws_service.get_bucket_info()
        return buckets
    except:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
        )