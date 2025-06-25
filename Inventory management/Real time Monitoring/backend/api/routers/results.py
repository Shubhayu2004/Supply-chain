from fastapi import APIRouter

router = APIRouter(prefix="/results", tags=["results"])

@router.get("/{result_id}")
def get_result(result_id: int):
    return {"message": f"Get detection result {result_id} (to be implemented)"}

@router.get("")
def list_results():
    return {"message": "List detection results (to be implemented)"} 