import pandas as pd 
import re

class Circuit():
    """
    회로에 대한 모든 정보가 있는 Circuit 객체입니다. netlist에 있는 정보를 읽어들여서 완성되는 객체입니다.
    ★★★ Note ★★★
    "Assumption"을 지켜줘야 올바르게 정보를 읽을 수 있습니다. "Assumption"을 반드시 확인해주세요!
    """
    def __init__(self, netlist_path : str) -> None:
        """
        args
        netlist_path : 
        """
        self.netlist_path = netlist_path
        # ★★★ Note ★★★
        # 회로 설계자가 netlist를 보며 사전에 반드시 정의해줘야 하는 부분입니다.
        # 1. 설계변수에 대한 설정.
        self.designvar_annotation_start = "** design_variables_start" # netlist에서 설계변수에 대한 정보의 시작을 표시하는 주석.
        self.devignvar_annotation_end = "** design_variables_end" # netlist에서 설계변수에 대한 정보의 끝을 표시하는 주석.
        self.designvar_names = ["Length1","Width1","Nf1"] #netlist에서 self.design_variables_start와 self.design_variables_end 사이에 있는 설계변수들의 목록.
        # 2. 소자 파라미터에 대한 설정.
        self.device_annotation_start = "**.subckt simplecsamp" # netlist에서 소자에 대한 정보의 시작을 표시하는 주석.
        self.device_annotation_end = "**** begin user architecture code" # netlist에서 소자에 대한 정보의 끝을 표시하는 주석.
        self.device_names = ["XM1"] #netlist의 self.device_annotation_start와 self.device_annotation_end 사이에 있는 값을 조절할 수 있는 소자들의 목록.
        
        
        # Circuit 객체를 instantiate할 때 자동으로 정보를 읽습니다. 바로 위에서 설정들이 올바르게 되어있어야 합니다.
        self.netlist = self._load_netlist()
        self.dsgnvar_to_val, self.dvc_to_dsgnvar, self.dvc_to_val = self._update_circuit()
        
    def _load_netlist(self) -> str:
        """
        self.netlist_path에 저장된 경로를 통해서 netlist 파일에 저장된 텍스트를 그대로 읽어들입니다.
        """
        with open(self.netlist_path,"r") as f:
            netlist = f.read()
        return netlist
    
    def _map_dsgnvar_to_val(self) -> dict:
        """
        self.netlist로부터 self.designvar_annotation_start와 self.devignvar_annotation_end 사이에 있는 설계변수(design variable)들에 대하여 매핑된 각각의 값을 가져옵니다.
        ★★★ Note ★★★
        self.designvar_names 목록에 있는 설계변수들의 값만 가져오기 때문에 반드시 먼저 올바르게 정의해줘야 합니다.
        
        outputs
        params_info = {"design_variable1" : value1, "design_variable2 : value2, ...}
        """
        start_idx = self.netlist.find(self.designvar_annotation_start) + len(self.designvar_annotation_start)
        end_idx = self.netlist.find(self.devignvar_annotation_end)
        raw_inform = self.netlist[start_idx:end_idx].strip().split("\n")
        
        dsgnvar_to_val ={}
        for raw_txt in raw_inform:
            raw_txt = raw_txt.strip().split(" ")
            var_name = raw_txt[1]; var_value = float(raw_txt[3])
            dsgnvar_to_val[var_name] = var_value

        return dsgnvar_to_val
    
    def _map_device_to_dsgnvar(self) -> dict:
        """
        self.netlist로부터 self.device_annotation_start와 self.device_annotation_end 사이에 있는 값을 조절할 수 있는 소자(device)들에 대하여 매핑된 각각의 설계변수를 가져옵니다.
        ★★★ Note ★★★
        self.device_names 목록에 있는 소자이름만 가져오기 때문에 반드시 먼저 올바르게 정의해줘야 합니다.
        
        outputs
        devices_info = {"M1_L" : "design_variable1","M1_W" : "design_variable2", ...}
        """
        start_idx = self.netlist.find(self.device_annotation_start) + len(self.device_annotation_start)
        end_idx = self.netlist.find(self.device_annotation_end)
        raw_inform = self.netlist[start_idx:end_idx].strip().split("\n")
            
        dvc_to_dsgnvar = {}
        for raw_txt in raw_inform:
            raw_txt = raw_txt.strip().split(" ")
            for dvc_name in self.device_names:
                if dvc_name in raw_txt:
                    name = dvc_name
                    for dsgn_var in self.designvar_names:
                        # netlist에서 설계변수가 소자의 특정값에 할당될 때 {design_variable} 이렇게 쓰였기에 .index로 인식하려면 중괄호를 양옆에 붙여줘야 함.
                        design_var_idx = raw_txt.index("{"+dsgn_var+"}") 
                        subfix_idx = design_var_idx - 2
                        dvc_to_dsgnvar[name+"_"+raw_txt[subfix_idx]] = dsgn_var

        return dvc_to_dsgnvar
    def _update_circuit(self) -> None:
        """
        circuit 객체의 3가지 정보인 self.dsgnvar_to_val, self.dvc_to_dsgnvar, self.dvc_to_val를 업데이트 합니다.
        self.__init__에 포함되어 있어서 instantiate시 자동으로 update됩니다.
        """
        dsgnvar_to_val = self._map_dsgnvar_to_val()
        dvc_to_dsgnvar = self._map_device_to_dsgnvar()
        
        dvc_to_val = {}
        for dvc,dsgvar in dvc_to_dsgnvar.items():
            dvc_to_val[dvc] = dsgnvar_to_val[dsgvar]
            
        return dsgnvar_to_val, dvc_to_dsgnvar, dvc_to_val