# Tutorial for Automating circuit.
한양대학교 회로설계 자동화 프로젝트를 위한 Tutorial repository 입니다.  
반드시 **아래를 읽고 진행**해주세요!! :blush:감사합니다.:blush:

## netlist directory
netlist directory에는 3가지의 파일이 존재합니다. 

1. simplecsamp : xschem에서 사용하는 기본 파일입니다. (중요하지 않음)
2. simplecsamp.spice : xschem에서 netlist를 save를 했을 경우 나오는 기본적인 netlist 파일 입니다.
3. simplecsamp_modified.spice: simplecsamp.spice를 수정한 netlist 파일입니다.


ngspice 자체는 netlist 파일인 2번이나 3번 파일을 사용할 수 있습니다. 하지만 2번 파일은 파이썬 내부에서 ngspice를 작동시키기 위한 입력으로 적절한 형식이 아닙니다. ngspice를 파이썬 내부에서 작동시키기 위해서는 `batch mode(배치모드)`만 허용되는데 xschem에서 직접적으로 나온 2번 파일의 경우 `interactive mode(대화형 모드)`에서의 command를 포함하기 때문입니다. 

보통 먼저 xschem상에서 회로설계를 어느정도 진행하고 그 후 파이썬 프로그래밍을 통해 최적의 파라미터(R,tr_width,tr_length,...)를 결정한다고 생각하면, 회로설계에서 파이썬 으로 전환하는 시점에서는 2번에서 3번으로 netlist 파일형식을 변화시켜주는 작업이 필요합니다. 잊지말고 프로그래밍하는 과정에 다다르면 **`batch mode`에서 허용되는 command를 참고하여 형식변환**을 해주시기 바랍니다.(`batch mode`커맨드는 ngspice_manual 참고)