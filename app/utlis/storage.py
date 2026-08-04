from pathlib import Path


class StorageManager:

    BASE_DIR = Path("storage/users")

    @staticmethod
    def create_user_folders(username: str):

        user_folder = StorageManager.BASE_DIR / username

        pdf_folder = user_folder / "uploaded_pdfs"
        chroma_folder = user_folder / "chroma_db"

        pdf_folder.mkdir(parents=True, exist_ok=True)
        chroma_folder.mkdir(parents=True, exist_ok=True)

        return {
            "user_folder": user_folder,
            "pdf_folder": pdf_folder,
            "chroma_folder": chroma_folder
        }



