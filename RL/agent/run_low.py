import subprocess
import os


def run_experiment(alpha, clf, dataset, device, label):
    """
    Runs an instance of low_level.py with specified parameters in the background using subprocess.
    """
    log_dir = f"./logs/low_level/{dataset}"
    os.makedirs(log_dir, exist_ok=True)

    command = [
        "python", "-u", "low_level.py",
        "--alpha", str(alpha),
        "--clf", clf,
        "--dataset", dataset,
        "--device", device,
        "--label", label
    ]
    log_file = f"{log_dir}/{clf}_{label[-1]}.log"
    with open(log_file, "w") as log:
        subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)


def main():
    experiments = [
        {"alpha": 1, "clf": 'slope', "dataset": 'ETHUSDT', "device": 'cuda:0', "label": 'label_1'},
        {"alpha": 4, "clf": 'slope', "dataset": 'ETHUSDT', "device": 'cuda:1', "label": 'label_2'},
        {"alpha": 0, "clf": 'slope', "dataset": 'ETHUSDT', "device": 'cuda:2', "label": 'label_3'},
        {"alpha": 4, "clf": 'vol', "dataset": 'ETHUSDT', "device": 'cuda:0', "label": 'label_1'},
        {"alpha": 1, "clf": 'vol', "dataset": 'ETHUSDT', "device": 'cuda:1', "label": 'label_2'},
        {"alpha": 1, "clf": 'vol', "dataset": 'ETHUSDT', "device": 'cuda:2', "label": 'label_3'}
    ]

    for exp in experiments:
        run_experiment(**exp)


if __name__ == "__main__":
    main()

