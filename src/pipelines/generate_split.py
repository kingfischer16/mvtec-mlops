"""
generate_split.py
=================

Purpose
-------
Looks at the gold metadata table and splits the "test" DataSplit into "validate" and "test" split based on a random seed and a specified proportion for the "validate" split, e.g. validate_proportion=0.2 means that 20% of the "test" split will be assigned to the "validate" split and the remaining 80% will be assigned to the "test" split.
"""

from pyspark.sql.functions import col, when, rand
import argparse

def generate_dev_split(input_df, validate_proportion, random_seed):
    """
    Generate a Spark DataFrame with a "DevSplit" column.

    Parameters:
    -----------
    input_df : pyspark.sql.DataFrame
        Input DataFrame containing the UUID and DataSplit columns.
    validate_proportion : float
        Proportion of the "test" split to assign to "validate".
    random_seed : int
        Seed for random number generator to ensure reproducibility.

    Returns:
    --------
    pyspark.sql.DataFrame
        DataFrame with an additional "DevSplit" column.
    """
    return input_df.withColumn(
        "DevSplit",
        when(
            (col("DataSplit") == "test") & (rand(seed=random_seed) < validate_proportion), "validate"
        ).when(
            col("DataSplit") == "test", "test"
        ).otherwise(
            col("DataSplit")
        )
    ).select("UUID", "DevSplit")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate DevSplit column for input data.")
    parser.add_argument("--catalog", required=True, help="Catalog name.")
    parser.add_argument("--schema", required=True, help="Input schema name.")
    parser.add_argument("--input_table", required=True, help="Input table name.")
    parser.add_argument("--output_table", required=True, help="Output table name.")
    parser.add_argument("--validate_proportion", type=float, required=True, help="Proportion of 'test' split to assign to 'validate'.")
    parser.add_argument("--random_seed", type=int, required=True, help="Random seed for reproducibility.")

    args = parser.parse_args()

    # Load input data
    input_df = df_input = spark.read.table(
        f"{args.catalog}.{args.schema}.{args.input_table}")

    # Generate DevSplit column
    output_df = generate_dev_split(input_df, args.validate_proportion, args.random_seed)

    # Write output data
    output_path = f"{args.catalog}.{args.schema}.{args.output_table}"
    output_df.write.format("delta").mode("overwrite").saveAsTable(output_path)

