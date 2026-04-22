"""
gold_base_tables.py
===================

Purpose
-------
Defines the base table in the gold layer, which splits the silver table information
into image path, defect presence, and defect type.
"""

from pyspark.sql.functions import col, lit, regexp_extract, when

def build_mvtec_ad_table(df_files, products_to_include):
    # Exclude files from 'ground_truth' folder
    filtered_df = df_files.filter(~col("file_path").contains("ground_truth"))

    # Regex patterns
    product_pattern = r"mvtec_ad/([^/]+)/"
    split_pattern = r"/(train|test)/"
    defect_pattern = r"/(test|train)/([^/]+)/"

    # Add columns
    result_df = filtered_df \
        .withColumn("ProductType", regexp_extract(col("file_path"), product_pattern, 1)) \
        .withColumn("DataSplit", regexp_extract(col("file_path"), split_pattern, 1)) \
        .withColumn("HasDefect", when(regexp_extract(col("file_path"), defect_pattern, 2) == "good", lit(False)).otherwise(lit(True))) \
        .withColumn("DefectType", when(col("HasDefect") == False, lit(None)).otherwise(regexp_extract(col("file_path"), defect_pattern, 2))) \
        .filter(col("ProductType").isin(products_to_include)) \
        .select(
            col("UUID"),
            col("file_path").alias("FilePath"),
            col("ProductType"),
            col("DataSplit"),
            col("HasDefect"),
            col("DefectType")
        )
    return result_df

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Build gold base table for MVTec AD dataset from silver index table"
    )
    parser.add_argument(
        "--catalog",
        required=True,
        help="Catalog name"
    )
    parser.add_argument(
        "--input_table_name",
        required=True,
        help="Input table name in silver layer (e.g., raw_image_index)"
    )
    parser.add_argument(
        "--output_table_name",
        default="raw_image_index",
        help="Output table name in gold layer (default: raw_image_index)"
    )
    parser.add_argument(
        "--products",
        nargs="+",
        required=True,
        help="List of product types to include (e.g., bottle cable)"
    )
    parser.add_argument(
        "--mode",
        choices=["overwrite", "append"],
        default="overwrite",
        help="Write mode: overwrite or append (default: overwrite)"
    )
    
    args = parser.parse_args()
    
    # Load silver index table
    print(f"Loading silver index table: {args.catalog}.{args.input_table_name}")
    df_input = spark.read.table(f"{args.catalog}.{args.input_table_name}")
    
    # Build gold base table
    print(f"Building gold base table for products: {', '.join(args.products)}")
    df_output = build_mvtec_ad_table(df_files=df_input, products_to_include=args.products)
    
    # Write to gold layer
    target_table = f"{args.catalog}.{args.output_table_name}"
    record_count = df_output.count()
    print(f"Writing {record_count} records to {target_table} in {args.mode} mode")
    
    df_output.write.mode(args.mode).saveAsTable(target_table)
    print(f"Successfully wrote to {target_table}")

if __name__ == "__main__":
    main()