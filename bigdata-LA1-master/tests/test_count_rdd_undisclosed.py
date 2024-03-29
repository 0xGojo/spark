import subprocess
import os

def test_count_rdd():
    command="python ./answers/count_rdd.py ./data/frenepublicinjection2014.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=='12828'+os.linesep)
