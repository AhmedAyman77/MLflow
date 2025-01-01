import mlflow

if __name__ == "__main__":

    experiment_id = mlflow.create_experiment(
        name = "testing_exp3",
        artifact_location="testing_artifacts",
        tags={"env":"dev", "version":"1.0.0"}
    )

    experiment = mlflow.get_experiment(experiment_id)
    print(f"exp name {experiment.name}")


    with mlflow.start_run(run_name="Ahmed", experiment_id=experiment_id) as run:

        mlflow.log_param("learning_rate", 0.05)

        print("run_id: {}".format(run.info.run_id))
        print("experiment_id: {}".format(run.info.experiment_id))
        print("status: {}".format(run.info.status))
        print("start_time: {}".format(run.info.start_time))
        print("end_time: {}".format(run.info.end_time))
        print("lifecycle_stage: {}".format(run.info.lifecycle_stage))