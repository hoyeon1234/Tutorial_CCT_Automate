# Netlist Manual
netlist 폴더에는 3개의 파일이 있습니다. 

1. simplecsamp : xschem에서 사용하는 기본 파일 형식입니다. (사용 X)
2. simplecsamp.spice : xschem에서 netlist를 바로 저장할 경우의 netlist 파일 입니다. (수정 전)
3. simplecsamp_modified.spice: simplecsamp.spice를 수정한 netlist 파일 입니다. (수정 후)

ngspice는 2번이나 3번의 netlist 파일을 입력으로 사용할 수 있지만... 2번 파일은 파이썬 내부에서 ngspice를 작동시키기 위한 입력으로 적절한 형식이 아닙니다. ngspice는 파이썬 내부에서 `batch mode(배치모드)`로 실행되지만 2번 파일의 경우 `interactive mode(대화형 모드)`의 command를 포함하기 때문입니다. 

보통 1)먼저 xschem에서 회로설계를 어느정도 진행하고 2)파이썬 프로그래밍으로 최적의 파라미터(R,tr_width,tr_length,...)를 결정하는 과정을 거칠 것이라 생각합니다. 이때 회로설계에서 프로그래밍으로 전환하는 시점에서는 2번에서 3번으로 netlist 파일형식을 변화시켜주는 작업이 반드시 필요합니다. 반드시 프로그래밍하는 하기 전  **`batch mode`에서 허용되는 command를 참고하여 netlist를 수정** 해주시기 바랍니다. (`batch mode`커맨드는 ngspice_manual 참고해주세요~!)
