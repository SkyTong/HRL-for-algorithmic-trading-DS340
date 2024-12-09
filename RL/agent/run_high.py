import subprocess
import os
from high_level import DQN


def run_high_level(dataset, device):
    """
    Runs an instance of high_level.py with specified parameters in the background using subprocess.
    """
    log_dir = f"./logs/high_level"
    os.makedirs(log_dir, exist_ok=True)

    command = [
        "python", "-u", "high_level.py",
        "--dataset", dataset,
        "--device", device
    ]
    log_file = f"{log_dir}/{dataset}.log"
    with open(log_file, "w") as log:
        subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)




def main():
    run_high_level(dataset='ETHUSDT', device='cuda:0')


if __name__ == "__main__":
    main()
