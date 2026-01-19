import subprocess
import platform

def test_runner_agent(state):
    mvn_cmd = "mvn.cmd" if platform.system() == "Windows" else "mvn"

    result = subprocess.run(
        [mvn_cmd, "clean", "verify"],
        cwd="../java-app",
        capture_output=True,
        text=True,
        shell=False
    )

    output = result.stdout + "\n" + result.stderr
    return {"test_run_output": output}
