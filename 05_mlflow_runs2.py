import mlflow

if __name__ == "__main__":

    with mlflow.start_run(run_name="A7med") as run:
        # your machine learning code will be here -> models, res, images, params
        mlflow.log_param('learning_rate',0.05)
        print(f"run_id{run.info.run_id}")

        print(run.info)
