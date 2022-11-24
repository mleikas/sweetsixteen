from pathlib import Path

file_path = Path(__file__).parent.parent
database_path = file_path / "references.db"
print(database_path)
