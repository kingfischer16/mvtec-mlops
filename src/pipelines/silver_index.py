"""
silver_index.py
==============

Purpose
------
Indexes all images in the bronze layer base path, writes the table to a table in silver zone.
"""

import os
import pandas as pd
import uuid

def crawl_files(base_path):
    file_records = []
    exclude_names = {"license", "readme"}
    for root, dirs, files in os.walk(base_path):
        for fname in files:
            fname_lower = fname.lower()
            # Exclude files named license/readme (with or without extension)
            if any(fname_lower.startswith(ex) for ex in exclude_names):
                continue
            file_path = os.path.join(root, fname)
            # Generate UUID5 using file_path as seed
            file_uuid = uuid.uuid5(uuid.NAMESPACE_URL, file_path)
            file_records.append({
                "UUID": str(file_uuid),
                "file_path": file_path,
                "file_name": fname,
                "folder": root
            })
    return spark.createDataFrame(pd.DataFrame(file_records))

def main():
    """
    Main function to index raw images and write to silver table.
    Parses command-line arguments for Databricks job execution.
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Index raw images and write to silver layer table"
    )
    parser.add_argument(
        "--catalog",
        required=True,
        help="Catalog name"
    )
    parser.add_argument(
        "--raw_volume_path",
        required=True,
        help="Path to raw volume containing images"
    )
    parser.add_argument(
        "--schema",
        required=True,
        help="Schema name"
    )
    parser.add_argument(
        "--table_name",
        default="raw_image_index",
        help="Table name (default: raw_image_index)"
    )
    parser.add_argument(
        "--mode",
        choices=["overwrite", "append"],
        default="overwrite",
        help="Write mode: overwrite or append (default: overwrite)"
    )
    
    args = parser.parse_args()
    
    # Crawl files and create DataFrame
    print(f"Crawling files from: {args.raw_volume_path}")
    df = crawl_files(args.raw_volume_path)
    
    # Write to silver table using three-level namespace
    target_table = f"{args.catalog}.{args.schema}.{args.table_name}"
    record_count = df.count()
    print(f"Writing {record_count} records to {target_table} in {args.mode} mode")
    
    df.write.mode(args.mode).saveAsTable(target_table)
    print(f"Successfully wrote to {target_table}")

if __name__ == "__main__":
    main()