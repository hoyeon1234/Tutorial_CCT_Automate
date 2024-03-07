# Starting Automation!
본 메뉴얼은 파이썬을 통한 회로 자동화를 시작하기 위한 메뉴얼입니다. Xschem을 통해 회로설계가 어느정도 진행되었다고 가정하며 소자의 파라미터를 최적화 하기위해 **ngspice와 Python을 연결하는 과정**에만 집중합니다.

## 1. 전반적인 회로설계
[Xschem - Common Source Amplifier 설계](https://www.youtube.com/watch?v=YUA_I55k-tM)  
위의 링크는 Xschem에서 간단히 Commom Source Amplifier를 설계하고 DC simulation 유튜브 예시입니다. 앞으로 진행될 예시에서는 위 영상을 기반으로 자동화의 다음 단계인 **ngspice와 Python의 연결**에만 초점을 둡니다.

## 2. netlist file save
위의 영상에서와 같이 회로를 만들었다면 다음 단계를 위해 회로가 가지고 있는 종합적인 정보를 담은 **netlist** 파일이 필요합니다. 그 과정은 아래와 같습니다.

1. 화면 중앙 상단의 Simulation -> Set netlist DIR로 netlist가 저장될 경로 설정.
    - 예시 : /home/hoyeon/Desktop/CCT_Automate_Tutorial/netlist/simplecsamp.spice
2. 화면 중앙 상단의 Simulation -> Show netlist after netlist command 설정
3. 화면 우측 상단의 Netlist -> Save