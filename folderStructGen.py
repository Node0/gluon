#!/usr/bin/env python3.11

import os
import subprocess

folder_structure = {
    "gluon": [
        "Cargo.toml",
        "build.rs",
        "config/config.json",
        "config/settings_postgres.json",
        "config/settings_sqlite.json",
        "crates/gluon-server/Cargo.toml",
        "crates/gluon-server/src/lib.rs",
        "crates/gluon-server/src/graphql_router.rs",
        "crates/gluon-server/src/backend_registry.rs",
        "crates/gluon-tui/Cargo.toml",
        "crates/gluon-tui/src/lib.rs",
        "crates/gluon-tui/src/app.rs",
        "crates/gluon-tui/src/input.rs",
        "crates/gluon-tui/src/views/welcome.rs",
        "crates/gluon-tui/src/views/backend_config.rs",
        "crates/gluon-tui/src/views/config_preview.rs",
        "crates/gluon-config/Cargo.toml",
        "crates/gluon-config/src/lib.rs",
        "crates/gluon-config/src/model.rs",
        "crates/gluon-backend-api/Cargo.toml",
        "crates/gluon-backend-api/src/conditioner.rs",
        "src/main.rs",
        "backends/postgres/irs.json",
        "backends/postgres/metadata.json",
        "backends/postgres/logic.rs",
        "backends/sqlite/irs.json",
        "backends/sqlite/metadata.json",
        "backends/sqlite/logic.rs"
    ]
}

def create_structure(base_path, structure):
    for base, files in structure.items():
        for file in files:
            file_path = os.path.join(base_path, base, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            subprocess.run(["touch", file_path])

if __name__ == "__main__":
    create_structure(".", folder_structure)
    print("Folder structure created successfully.")
