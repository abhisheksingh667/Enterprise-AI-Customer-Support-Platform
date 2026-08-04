from fastapi import APIRouter, UploadFile, File, Depends
from pathlib import Path
import shutil

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/api/v1/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):

    # Create user's upload folder
    upload_dir = Path(
        f"storage/users/{current_user.username}/uploaded_pdfs"
    )

    upload_dir.mkdir(parents=True, exist_ok=True)

    # Save PDF
    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF Uploaded Successfully",
        "user": current_user.username,
        "filename": file.filename,
        "saved_to": str(file_path)
    }