import mlflow

run_id = "d3df398e95284128830d39cb421a5054"
with mlflow.start_run(run_id=None) as run:
    # mlflow.log_param("archi", "RAT")
    # mlflow.log_param("emb", "distil")
    # mlflow.log_param("lr", 7.4e-04)
    mlflow.set_tag("GPU", "P4")
    # mlflow.log_metric("test_accuracy", 0.6315280464216635)