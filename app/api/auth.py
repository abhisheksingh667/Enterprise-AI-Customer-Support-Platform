from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterUser, LoginUser
from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token

from app.database.session import get_db
from app.database.crud import create_user, get_user_by_username

from app.utlis.storage import StorageManager

from app.core.logger import logger

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# ---------------------- Register ---------------------- #

@router.post("/register")
def register(
    user: RegisterUser,
    db: Session = Depends(get_db)
):

    # Check if username already exists
    existing_user = get_user_by_username(
        db,
        user.username
    )

    if existing_user:

        logger.warning(
            f"Registration failed. Username already exists: {user.username}"
        )

        return {
            "message": "Username already exists"
        }

    # Hash Password
    hashed_password = hash_password(user.password)

    # Save User
    created_user = create_user(
        db=db,
        username=user.username,
        hashed_password=hashed_password
    )

    # Create User Storage Folder
    StorageManager.create_user_folders(
        created_user.username
    )

    logger.info(
        f"New user registered: {created_user.username}"
    )

    return {
        "message": "User Registered Successfully"
    }


# ---------------------- Login ---------------------- #

@router.post("/login")
def login(
    user: LoginUser,
    db: Session = Depends(get_db)
):

    # Find User
    existing_user = get_user_by_username(
        db,
        user.username
    )

    if existing_user is None:

        logger.warning(
            f"Login failed. Invalid username: {user.username}"
        )

        return {
            "message": "Invalid Username"
        }

    # Verify Password
    if not verify_password(
        user.password,
        existing_user.hashed_password
    ):

        logger.warning(
            f"Login failed. Invalid password for user: {user.username}"
        )

        return {
            "message": "Invalid Password"
        }

    # Generate JWT Token
    token = create_access_token(
        {
            "sub": existing_user.username
        }
    )

    logger.info(
        f"User logged in: {existing_user.username}"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }