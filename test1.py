from utils.Circuit import Circuit
from utils.SpiceKernel import SpiceKernel
"""
Circuit.py와 SpiceKernel.py에 대한 test입니다.
"""

# Circuit.py
# Circuit.py는 수정된 modified_netlist파일을 입력으로 받음.
netlist_path = "//home//hoyeon//Desktop//CCT_Automate_Tutorial//netlist//simplecsamp_modified.spice"
circuit = Circuit(netlist_path)
# 결과가 올바르게 나오는지 확인.
print(circuit.netlist)
print(circuit.dsgnvar_to_val)
print(circuit.dvc_to_dsgnvar)
print(circuit.dvc_to_val)

# Spicekernel.py
# Spicekernel.py로 시뮬레이션을 실행.
skl = SpiceKernel()
skl.run(circuit)