import subprocess
from .Circuit import Circuit
class SpiceKernel():
    """
    ngspice와 Python을 연결시켜주는 SpiceKernel 객체 입니다. 
    run 함수로 시뮬레이션을 수행합니다.
    """
    def __init__(self) -> None:
        pass
    
    def run(self, circuit : Circuit) -> None:
        """
        "run" 함수를 통해 Circuit.netlist에 정의된대로 ngspice 시뮬레이션을 수행합니다.
        """
        command = "ngspice -b " + circuit.netlist_path
        with subprocess.Popen(args=command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) as process:
            process.communicate()