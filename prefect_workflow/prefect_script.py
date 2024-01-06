from prefect import flow, task
import subprocess
import sys

@task
def run_docker_container(image_name):
    result = subprocess.run(["sudo", "docker", "run", image_name], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr, file=sys.stderr)

@flow(log_prints=True)
def docker_scrapers_flow():
    run_docker_container("scraper1-image")
    run_docker_container("scraper2-image")

if __name__ == "__main__":
    docker_scrapers_flow()
