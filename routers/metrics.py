from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics", status_code=200)
def get_metrics():
    '''
    This API gets system metrics like CPU, Memory, Disk usage
    '''
    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
        )