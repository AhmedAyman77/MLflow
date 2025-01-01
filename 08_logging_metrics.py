import mlflow

if __name__ == "__main__":
    experiment = mlflow.get_experiment_by_name(name="testing_exp3")
    print(f"exp name {experiment.name}")

    with mlflow.start_run(run_name="logging_metrics", experiment_id=experiment.experiment_id) as run:

        # mlflow.log_metric("accuracy", 0.95)

        mlflow.log_metrics({
            "mes":0.01,
            "f1":0.95,
            "precision":0.95,
            "recall":0.95
        })

        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))