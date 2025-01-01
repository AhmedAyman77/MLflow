import mlflow

if __name__ == "__main__":
    # create experiment
    experiment_id = mlflow.create_experiment(
        name="test_experiment",
        artifact_location="testing_location",
        tags={"env":"dev", "version":"1.0.0"}
    )

    print(experiment_id)

# run the experiment with this command
# python _create_experiment.py