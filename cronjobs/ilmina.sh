#!/usr/bin/env bash
set -e
set -x

cd "$(dirname "$0")" || exit
source ./project_root.sh
source ./shared_extras.sh

python3 "${ETL_DIR}/export_spawns.py" \
  --db_config="${DB_CONFIG}" \
  --output_dir="${DADGUIDE_ILMINA_DIR}"
cp -r ${RAW_DIR}/na/. ${DADGUIDE_ILMINA_DIR}
