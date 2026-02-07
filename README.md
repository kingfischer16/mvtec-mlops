# MVTec MLOps Pipeline

A comprehensive MLOps pipeline for industrial anomaly detection, built on Databricks Community Edition (free tier). This project demonstrates best practices for data engineering, machine learning experimentation, and model deployment with full traceability and governance.

## 🎯 Project Overview

This project implements a production-ready MLOps pipeline using the Databricks Community Edition (free tier), showcasing:

- **Medallion Architecture**: Bronze/Silver/Gold data layers for structured data processing
- **Image Processing Pipeline**: Handling industrial anomaly detection images across the medallion architecture
- **ML Experimentation**: Systematic model development and hyperparameter tuning
- **Full Traceability**: MLflow integration for model versioning and experiment tracking (Unity Catalog planned for paid tiers)
- **Deployment Ready**: End-to-end pipeline from raw data to deployed models

The project focuses on industrial anomaly detection using the MVTec Anomaly Detection (AD) dataset, implementing computer vision models to identify defects in manufactured products.

## 🏗️ Architecture

### Medallion Architecture

The project follows Databricks' medallion architecture pattern:

```
Bronze (Raw) → Silver (Cleaned) → Gold (Feature/Aggregated)
```

- **Bronze Layer**: Raw ingestion of MVTec AD images and metadata
- **Silver Layer**: Cleaned, validated, and transformed data ready for analysis
- **Gold Layer**: Feature-engineered datasets optimized for ML model training

### Technology Stack

- **Platform**: Databricks Community Edition (free tier)
- **Experiment Tracking**: MLflow for model versioning and metrics
- **Data Governance**: Delta Lake for data reliability (Unity Catalog for paid tiers)
- **Image Processing**: PySpark for distributed image processing
- **ML Frameworks**: PyTorch/TensorFlow for deep learning models
- **Orchestration**: Databricks Workflows (to be added via Asset Bundles)

## 🚀 Key Features

### 1. Data & Image Processing
- Distributed image ingestion and preprocessing using PySpark
- Automated data quality checks at each medallion layer
- Scalable image transformation pipeline
- Metadata extraction and cataloging

### 2. Data Governance & Catalog
- Delta Lake for ACID transactions and data versioning
- Structured table organization for Bronze/Silver/Gold layers
- Metadata management and data quality tracking
- Unity Catalog integration available when migrating to paid tiers

### 3. MLflow Traceability
- Automatic logging of all experiments and runs
- Model versioning with artifact storage
- Parameter and metric tracking
- Model registry for production deployment

### 4. ML Experimentation
- Structured experiment framework
- Hyperparameter tuning with automated tracking
- Model comparison and selection
- Reproducible training pipelines

### 5. Deployment Pipeline
- Model promotion workflow (Staging → Production)
- Batch inference capabilities
- Model serving endpoints (planned)
- A/B testing framework (planned)

## 📋 Prerequisites

- Databricks Community Edition account (free): [Sign up here](https://community.cloud.databricks.com/)
- Basic knowledge of Python and PySpark
- Understanding of computer vision and anomaly detection concepts

## 🏁 Getting Started

### 1. Setup Databricks Environment

1. Sign up for a [Databricks Community Edition account](https://community.cloud.databricks.com/)
2. Create a new cluster with the following specifications:
   - Runtime: Latest ML Runtime (includes MLflow, PyTorch, TensorFlow)
   - Python: 3.9 or higher

### 2. Clone Repository

```bash
# In Databricks Workspace
# Use Repos feature to connect your GitHub repository
# Navigate to Repos → Add Repo → Enter repository URL
```

### 3. Database and Schema Setup

In Databricks Community Edition, use the default Hive metastore:
- Create a database for the project (e.g., `mvtec_ad_mlops`)
- Set up schemas/tables for Bronze, Silver, and Gold layers
- Use Delta Lake format for all tables
- Note: Unity Catalog features require paid Databricks tiers

### 4. Run Pipeline Notebooks

(Coming soon - notebooks will be added to the repository)

1. **Data Ingestion**: Import MVTec AD dataset
2. **Bronze Layer**: Raw data processing
3. **Silver Layer**: Data cleaning and validation
4. **Gold Layer**: Feature engineering
5. **Model Training**: Run experiments with MLflow tracking
6. **Model Deployment**: Deploy best model to registry

## 📁 Project Structure

```
mvtec-mlops/
├── README.md                          # This file
├── .gitignore                         # Git ignore rules
├── databricks-asset-bundles/          # (Coming soon) DAB configuration
├── notebooks/                         # (Coming soon) Databricks notebooks
│   ├── 01_data_ingestion/
│   ├── 02_bronze_layer/
│   ├── 03_silver_layer/
│   ├── 04_gold_layer/
│   ├── 05_model_training/
│   └── 06_model_deployment/
├── src/                              # (Coming soon) Python modules
│   ├── data_processing/
│   ├── feature_engineering/
│   ├── models/
│   └── utils/
├── tests/                            # (Coming soon) Unit tests
├── config/                           # (Coming soon) Configuration files
└── docs/                             # (Coming soon) Additional documentation
```

## 🔄 Workflow

1. **Data Ingestion**: MVTec AD dataset is ingested into the Bronze layer
2. **Data Processing**: Images are processed through Silver layer (cleaning, validation)
3. **Feature Engineering**: Gold layer creates ML-ready features
4. **Experimentation**: Multiple models are trained and tracked via MLflow
5. **Model Selection**: Best performing model is identified
6. **Registration**: Model is registered in MLflow Model Registry
7. **Deployment**: Model is deployed for inference

## 📊 Data Lineage & Traceability

Every step of the pipeline is tracked:

- **Data Lineage**: Delta Lake provides data versioning and time travel capabilities
- **Experiment Tracking**: MLflow logs all training runs with parameters, metrics, and artifacts
- **Model Versioning**: All models are versioned in MLflow Model Registry with metadata
- **Audit Trail**: MLflow tracking provides complete history of experiments and model changes
- **Note**: Full Unity Catalog lineage features are available when upgrading to paid tiers

## 🔮 Coming Soon

The following features are currently in development and will be added to the repository:

- **Databricks Asset Bundles (DABs)**: Infrastructure-as-code for the entire pipeline
- **Automated Workflows**: Scheduled jobs for data processing and model training
- **CI/CD Integration**: Automated testing and deployment
- **Advanced Models**: Ensemble methods and transformer-based architectures
- **Real-time Inference**: Model serving endpoints for production use
- **Monitoring & Alerting**: Model performance tracking and drift detection
- **Unity Catalog Migration**: Documentation for upgrading to paid tiers with Unity Catalog

## 📖 MVTec Anomaly Detection Dataset

This project uses the MVTec AD dataset, a benchmark dataset for anomaly detection in industrial images. The dataset contains:

- 15 categories of objects and textures
- Over 5,000 high-resolution images
- Various types of defects (scratches, dents, contamination, etc.)
- Both training and test sets with annotations

Learn more: [MVTec AD Dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad)

**Note**: Please review the MVTec AD dataset license and terms of use before downloading and using the dataset. The dataset is freely available for research and educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📝 License

This project's license will be determined and added in future updates. Until then, please contact the repository owner for usage permissions.

## 🙏 Acknowledgments

- Databricks for providing the Community Edition
- MVTec for the industrial anomaly detection dataset
- The open-source ML community for tools and frameworks

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

**Note**: This project is continuously evolving. Check back regularly for updates, including the Databricks Asset Bundles configuration and additional code that are currently on the maintainer's local machine and will be added soon.
