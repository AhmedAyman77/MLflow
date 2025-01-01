import mlflow

if __name__ == "__main__":
    experiment = mlflow.get_experiment_by_name(name="testing_exp3")
    print(f"exp name {experiment.name}")

    with mlflow.start_run(run_name="logging_params", experiment_id=experiment.experiment_id) as run:

        mlflow.log_params({
            "learning_rate": 0.05,
            "epochs": 100,
            "batch": 64,
            "optimizer": "Adam",
            "loss": "categorical_crossentropy",
        })

        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))