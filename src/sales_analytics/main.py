from .db import create_in_memory_db
from .loaders import load_all_data
from .analytics import generate_reports
from .config import DEFAULT_REPORTS_DIR

def main() -> None:
    conn = create_in_memory_db()
    load_all_data(conn)
    generate_reports(conn, output_dir=DEFAULT_REPORTS_DIR)

if __name__ == "__main__":
    main()
