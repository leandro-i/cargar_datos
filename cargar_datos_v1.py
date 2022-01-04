#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from tkinter.constants import BOTTOM, CENTER, DISABLED, HORIZONTAL, LEFT, RIGHT, TOP, X, Y
import pandas as pd
import os
import base64
from idlelib.tooltip import Hovertip

class Ventana():
    label = []
    entry = []
    cuadro = None
    frame_cuadro = None
    eliminados = []
    frame_entries = []
    frame_combo = []
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cargar datos')
        
        icon = """AAABAAEAQEAAAAEAIAAoQgAAFgAAACgAAABAAAAAgAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAABAREQAQEREBEBERABAREQCQEREAkBERABAREQEQEREAEBERAJAREQCQEREAEBERARAREQA
        QEREAkBERAJAREQAQEREBEBERABAREQCQEREAkBERABAREQEQEREAEBERAJAREQCQEREAEBERARA
        REQAQEREAkBERAJAREQAQEREBEBERABAREQCQEREAkBERABAREQEQEREAEBERAJAREQCQEREAEBE
        RARAREQAQEREAkBERAJAREQAQEREBEBERABAREQCQEREAkBERABAREQEQEREAEBERAJAREQCQERE
        AEBERARAREQAQEREAkBERAJAREQAQEREBEBERABAREQAQEREAEBERABAREQIQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBE
        RARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAEBERAJAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAQAAAAAQEREBEBERARAREQAQERECEBERABA
        REQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        CEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQEREAkBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREAkBERABAREQIQEREAEBERARAREQEQEREAEBE
        RAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQERE
        AEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBE
        RAJAREQAQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREAkBERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABA
        REQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        BAAAAABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQCQEREAEBERARAREQEQEREAEBERAiwczlg
        rnI5wK5yOb6wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5wKxxOcCw
        czm+rnI5wK5yOb6wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5wKxx
        OcCwczm+rnI5wK5yOb6wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5
        wKxxOcCwczm+rnI5wK5yOb6wcznArHE5wLBzOb6rcTlkQEREBEBERABAREQIQEREAEBERARAREQC
        QEREAEBERAhAREQAQEREBEBERARAREQAqnE5grBzOfKtcjmgrXI5orBzOZ6rcTmisHM5oK1yOaCt
        cjmisHM5nqtxOaKwczmgrXI5oK1yOaKwczmeq3E5orBzOaCuczn/rnI5xLBzOZ6rcTmisHM5oK1y
        OaCtcjmisHM5nqtxOaKwczmgrXI5oK1yOaKwczmeq3E5orBzOaCtcjmgrnI50LBzOf+rcTmisHM5
        oK1yOaCtcjmisHM5nqtxOaKwczmgrXI5oK1yOaKwczmeq3E5orBzOaCtcjmgrXI5orBzOZ6tcjny
        sHM5fkBERARAREQEQEREAEBERAhAREQAQEREAkBERABAREQAQERECEBERABAREQEQEREBLBzOX6s
        cjneQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIsHM5/6txOWRAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAKxyOYCuczn/QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEsHM53qpxOYJAREQAQEREBEBERARAREQAQERECEBERABA
        REQCQEREBEBERABAREQIQEREAEBERASscjmCsHM53kBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAK1yOf+wczlgQEREBEBERARAREQAQERE
        CEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAiwczmArnM5/0BERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBK5yOeCw
        czmAQERECEBERABAREQEQEREBEBERABAREQEAAAAAEBERARAREQEQEREAEBERAhAREQArHI5gK5y
        Od5AREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERASwczn/qHA6ZEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAqnE5grBzOf9AREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERACucjnerHI5gEBERABAREQIQEREAEBERARAREQEQEREAEBE
        RAJAREQAQEREBEBERARAREQAQERECLBzOYCucjngQEREBEBERABAREQIQEREAEBERARAREQEQERE
        AEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQErnM5/7BzOWBAREQIQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBLBzOX6tcjn/QEREAEBERARA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIsHM53qxy
        OYJAREQEQEREAEBERAhAREQAQEREBEBERAJAREQAQERECEBERABAREQEQEREBEBERACqcTmCsHM5
        3kBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAK5zOf+rcTlgQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERASscjmCsHM5/0BERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAKxyOd6wczl+QEREBEBERARAREQAQERECEBERABAREQCQERE
        AEBERABAREQIQEREAEBERARAREQEsHM5fq1yOeqwczlgq3E5ZKtxOWCwczlgqHA6ZLBzOWCrcTlk
        q3E5YLBzOWCocDpksHM5YKtxOWSrcTlgsHM5YKhwOmSwczn/rXI5nqtxOWCwczlgqHA6ZLBzOWCr
        cTlkq3E5YLBzOWCocDpksHM5YKtxOWSrcTlgsHM5YKhwOmSwczlgrXI5sK5zOf+wczlgqHA6ZLBz
        OWCrcTlkq3E5YLBzOWCocDpksHM5YKtxOWSrcTlgsHM5YKhwOmSwczlgq3E5ZKtxOWCwcznqqnE5
        gkBERABAREQEQEREBEBERABAREQIQEREAEBERAJAREQEQEREAEBERAhAREQAQEREBKxyOYKwczn/
        rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+w
        czn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65z
        Of+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5
        /65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOYBAREQIQEREAEBERARAREQEQEREAEBERAQAAAAA
        QEREBEBERARAREQAQERECEBERACscjmArnI53kBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREBLBzOf+ocDpkQEREAEBERARAREQEQEREAEBE
        RAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERACqcTmCsHM5/0BERARAREQEQERE
        AEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAK5yOd6scjmA
        QEREAEBERAhAREQAQEREBEBERARAREQAQEREAkBERABAREQEQEREBEBERABAREQIsHM5gK5yOeBA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBE
        RASuczn/sHM5YEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEsHM5fq1yOf9AREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAEBERARAREQEQEREAEBERAiwcznerHI5gkBERARAREQAQERECEBERABAREQEQEREAkBERABA
        REQIQEREAEBERARAREQEQEREAKpxOYKwczneQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQArnM5/6txOWBAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBKxyOYKwczn/QERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQArHI53rBzOX5A
        REQEQEREBEBERABAREQIQEREAEBERAJAREQAQEREAEBERAhAREQAQEREBEBERASwczl+rHI53kBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        CLBzOf+rcTlkQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERACscjmArnM5/0BERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBLBzOd6qcTmCQEREAEBERARAREQEQEREAEBERAhAREQAQEREAkBE
        RARAREQAQERECEBERABAREQErHI5grBzOd5AREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERACtcjn/sHM5YEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIsHM5gK5zOf9AREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERASucjngsHM5gEBE
        RAhAREQAQEREBEBERARAREQAQEREBAAAAABAREQEQEREBEBERABAREQIQEREAKxyOYCucjnirnI5
        IJpqOyaucjkgom06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IKJtOiShbTok
        sHM5/6lwOXiucjkgom06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IKJtOiSh
        bTokrnI5IKpxOZKwczn/om06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IKJt
        OiShbTokrnI5IJpqOyaucjkgrnI54qxyOYBAREQAQERECEBERABAREQEQEREBEBERABAREQCQERE
        AEBERARAREQEQEREAEBERAiwczmArnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/
        sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+t
        cjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7Bz
        Of+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+scjmCQERE
        BEBERABAREQIQEREAEBERARAREQCQEREAEBERAhAREQAQEREBEBERARAREQAqnE5grBzOeaocDlC
        qXA5RK9zOUCkbjpGr3M5QKhwOUKpcDlEr3M5QKRuOkavczlAqHA5QqlwOUSvczlApG46Rq9zOUCu
        czn/rHI5iK9zOUCkbjpGr3M5QKhwOUKpcDlEr3M5QKRuOkavczlAqHA5QqlwOUSvczlApG46Rq9z
        OUCocDlCrXI5orBzOf+kbjpGr3M5QKhwOUKpcDlEr3M5QKRuOkavczlAqHA5QqlwOUSvczlApG46
        Rq9zOUCocDlCqXA5RK9zOUCscjnmsHM5fkBERARAREQEQEREAEBERAhAREQAQEREAkBERABAREQA
        QERECEBERABAREQEQEREBLBzOX6scjneQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIsHM5/6txOWRAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAKxyOYCuczn/QEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEsHM53qpxOYJAREQA
        QEREBEBERARAREQAQERECEBERABAREQCQEREBEBERABAREQIQEREAEBERASscjmCsHM53kBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAK1y
        Of+wczlgQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQERE
        AEBERAiwczmArnM5/0BERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBK5yOeCwczmAQERECEBERABAREQEQEREBEBERABAREQEAAAAAEBERARA
        REQEQEREAEBERAhAREQArHI5gK5yOd5AREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBE
        RARAREQEQEREAEBERAhAREQAQEREBEBERASwczn/qHA6ZEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAqnE5grBzOf9AREQEQEREBEBERABAREQI
        QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERACucjnerHI5gEBERABA
        REQIQEREAEBERARAREQEQEREAEBERAJAREQAQEREBEBERARAREQAQERECLBzOYCucjngQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQErnM5
        /7BzOWBAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBLBzOX6tcjn/QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABA
        REQEQEREBEBERABAREQIsHM53qxyOYJAREQEQEREAEBERAhAREQAQEREBEBERAJAREQAQERECEBE
        RABAREQEQEREBEBERACqcTmCsHM53kBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        CEBERABAREQEQEREBEBERABAREQIQEREAK5zOf+rcTlgQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERASscjmCsHM5/0BERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAKxyOd6wczl+QEREBEBE
        RARAREQAQERECEBERABAREQCQEREAEBERABAREQIQEREAEBERARAREQEsHM5fq1yOfawczm+rnI5
        wK5yOb6wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5wKxxOcCwczn/
        rnI52K5yOb6wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5wKxxOcCw
        czm+rnI53q5zOf+wcznArHE5wLBzOb6ucjnArnI5vrBzOcCscTnAsHM5vq5yOcCucjm+sHM5wKxx
        OcCwczm+rnI5wK5yOb6wczn2qnE5gkBERABAREQEQEREBEBERABAREQIQEREAEBERAJAREQEQERE
        AEBERAhAREQAQEREBKxyOYKwcznyq3E5orBzOaCtcjmgrXI5orBzOZ6rcTmisHM5oK1yOaCtcjmi
        sHM5nqtxOaKwczmgrXI5oK1yOaKwczmerXI5/7BzOcKtcjmgrXI5orBzOZ6rcTmisHM5oK1yOaCt
        cjmisHM5nqtxOaKwczmgrXI5oK1yOaKwczmeq3E5orBzOdCuczn/rXI5orBzOZ6rcTmisHM5oK1y
        OaCtcjmisHM5nqtxOaKwczmgrXI5oK1yOaKwczmeq3E5orBzOaCtcjmgrnM58rBzOYBAREQIQERE
        AEBERARAREQEQEREAEBERAQAAAAAQEREBEBERARAREQAQERECEBERACscjmArnI53kBERABAREQI
        QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBLBzOf+o
        cDpkQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RACqcTmCsHM5/0BERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAK5yOd6scjmAQEREAEBERAhAREQAQEREBEBERARAREQAQEREAkBERABAREQE
        QEREBEBERABAREQIsHM5gK5yOeBAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABA
        REQEQEREBEBERABAREQIQEREAEBERASuczn/sHM5YEBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEsHM5fq1yOf9AREQAQEREBEBERARAREQAQERE
        CEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAiwcznerHI5gkBERARAREQA
        QERECEBERABAREQEQEREAkBERABAREQIQEREAEBERARAREQEQEREAKpxOYKwczneQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQArnM5/6tx
        OWBAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BKxyOYKwczn/QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQArHI53rBzOX5AREQEQEREBEBERABAREQIQEREAEBERAJAREQAQEREAEBERAhA
        REQAQEREBEBERASwczl+rHI53kBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBE
        RAhAREQAQEREBEBERARAREQAQERECLBzOf+rcTlkQEREBEBERABAREQIQEREAEBERARAREQEQERE
        AEBERAhAREQAQEREBEBERARAREQAQERECEBERACscjmArnM5/0BERABAREQIQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBLBzOd6qcTmCQEREAEBERARA
        REQEQEREAEBERAhAREQAQEREAkBERARAREQAQERECEBERABAREQErHI5grBzOd5AREQIQEREAEBE
        RARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERACtcjn/sHM5
        YEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        sHM5gK5zOf9AREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERASucjngsHM5gEBERAhAREQAQEREBEBERARAREQAQEREBAAAAABAREQEQEREBEBE
        RABAREQIQEREAKxyOYCucznusHM5gKpxOYKwczl+rHI5gqxyOYCwczmAqnE5grBzOX6scjmCrHI5
        gLBzOYCqcTmCsHM5fqxyOYKscjmAsHM5/6txObCwczl+rHI5gqxyOYCwczmAqnE5grBzOX6scjmC
        rHI5gLBzOYCqcTmCsHM5fqxyOYKscjmAsHM5gKxxOcKwczn/rHI5gqxyOYCwczmAqnE5grBzOX6s
        cjmCrHI5gLBzOYCqcTmCsHM5fqxyOYKscjmAsHM5gKpxOYKwczl+rnM57qxyOYBAREQAQERECEBE
        RABAREQEQEREBEBERABAREQCQEREAEBERARAREQEQEREAEBERAiwczmArnM5+q5yOeCwcznerHI5
        3rBzOd6ucjnernI54LBzOd6scjnesHM53q5yOd6ucjngsHM53qxyOd6wcznernI53q5zOf+wcznq
        rHI53rBzOd6ucjnernI54LBzOd6scjnesHM53q5yOd6ucjngsHM53qxyOd6wcznernI53q5yOeCw
        cznurXI5/7BzOd6ucjnernI54LBzOd6scjnesHM53q5yOd6ucjngsHM53qxyOd6wcznernI53q5y
        OeCwcznerHI53rBzOfqscjmCQEREBEBERABAREQIQEREAEBERARAREQCQEREAEBERAhAREQAQERE
        BEBERARAREQAqnE5grBzOd5AREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERACuczn/q3E5YEBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQErHI5grBzOf9AREQIQEREAEBERARAREQEQEREAEBE
        RAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERACscjnesHM5fkBERARAREQEQERE
        AEBERAhAREQAQEREAkBERABAREQAQERECEBERABAREQEQEREBLBzOX6scjneQEREAEBERARAREQE
        QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIsHM5/6txOWRA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAKxy
        OYCuczn/QEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEsHM53qpxOYJAREQAQEREBEBERARAREQAQERECEBERABAREQCQEREBEBERABAREQI
        QEREAEBERASscjmCsHM53kBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERARAREQEQEREAK1yOf+wczlgQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAiwczmArnM5/0BERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBK5yOeCwczmAQERECEBERABAREQE
        QEREBEBERABAREQEAAAAAEBERARAREQEQEREAEBERAhAREQArHI5gK5yOd5AREQAQERECEBERABA
        REQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERASwczn/qHA6ZEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAqnE5
        grBzOf9AREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERACucjnerHI5gEBERABAREQIQEREAEBERARAREQEQEREAEBERAJAREQAQEREBEBERARA
        REQAQERECLBzOYCucjngQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQErnM5/7BzOWBAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBLBzOX6tcjn/QEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIsHM53qxyOYJAREQEQEREAEBERAhA
        REQAQEREBEBERAJAREQAQERECEBERABAREQEQEREBEBERACqcTmCsHM54qJtOiShbTokrnI5IJpq
        Oyaucjkgom06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IK5zOf+scTl0rnI5
        IJpqOyaucjkgom06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IKJtOiStcjmS
        sHM5/5pqOyaucjkgom06JKFtOiSucjkgmmo7Jq5yOSCibTokoW06JK5yOSCaajsmrnI5IKJtOiSh
        bTokrnI5IKxyOeKwczl+QEREBEBERARAREQAQERECEBERABAREQCQEREAEBERABAREQIQEREAEBE
        RARAREQEsHM5fq1yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5
        /65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/
        sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+t
        cjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/qnE5gkBERABAREQEQEREBEBE
        RABAREQIQEREAEBERAJAREQEQEREAEBERAhAREQAQEREBKxyOYKwczn/rXI5/7BzOf+uczn/rnM5
        /7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/
        rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+u
        czn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7Bz
        Of+uczn/rnM5/7BzOYBAREQIQEREAEBERARAREQEQEREAEBERAQAAAAAQEREBEBERARAREQAQERE
        CEBERACscjmArnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/
        rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+w
        czn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65z
        Of+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+scjmAQEREAEBERAhAREQAQERE
        BEBERARAREQAQEREAkBERABAREQEQEREBEBERABAREQIsHM5gK5zOf+uczn/sHM5/61yOf+wczn/
        rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+w
        czn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61y
        Of+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5
        /61yOf+wczn/rHI5gkBERARAREQAQERECEBERABAREQEQEREAkBERABAREQIQEREAEBERARAREQE
        QEREAKpxOYKwczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+u
        czn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65z
        Of+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5
        /65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOX5AREQEQEREBEBERABAREQI
        QEREAEBERAJAREQAQEREAEBERAhAREQAQEREBEBERASwczl+rXI5/7BzOf+uczn/rnM5/7BzOf+t
        cjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7Bz
        Of+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5
        /7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7BzOf+uczn/
        rnM5/7BzOf+qcTmCQEREAEBERARAREQEQEREAEBERAhAREQAQEREAkBERARAREQAQERECEBERABA
        REQErHI5grBzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5/7Bz
        Of+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/rXI5
        /7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5/65zOf+wczn/
        rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5gEBERAhAREQAQEREBEBERARA
        REQAQEREBAAAAABAREQEQEREBEBERABAREQIQEREAKxyOYCuczn/sHM5/61yOf+wczn/rnM5/65z
        Of+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/rnM5
        /65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+wczn/
        rnM5/65zOf+wczn/rXI5/7BzOf+uczn/rnM5/7BzOf+tcjn/sHM5/65zOf+uczn/sHM5/61yOf+w
        czn/rnM5/6xyOYBAREQAQERECEBERABAREQEQEREBEBERABAREQCQEREAEBERARAREQEQEREAEBE
        RAivczlArHI5gKxyOYKwczl+qnE5grBzOYCscjmArHI5grBzOX6qcTmCsHM5gKxyOYCscjmCsHM5
        fqpxOYKwczmArHI5gKxyOYKwczl+qnE5grBzOYCscjmArHI5grBzOX6qcTmCsHM5gKxyOYCscjmC
        sHM5fqpxOYKwczmArHI5gKxyOYKwczl+qnE5grBzOYCscjmArHI5grBzOX6qcTmCsHM5gKxyOYCs
        cjmCsHM5fqpxOYKwczmArHI5gKxyOYKwczl+qnE5grBzOYCpcDlEQEREBEBERABAREQIQEREAEBE
        RARAREQCQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREAkBERABAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABA
        REQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        CEBERABAREQCQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQEAAAAAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBE
        RAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQERE
        AEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQE
        QEREAEBERAJAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARA
        REQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBE
        RARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQERE
        AEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQI
        QEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERAJAREQAQERECEBERABAREQEQEREBEBERABA
        REQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBE
        RABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQEQERE
        BEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABAREQE
        QEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBERABA
        REQCQEREAEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERECEBE
        RABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQAQERE
        CEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARAREQA
        QERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQEREBEBERARA
        REQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERAJAREQEQEREAEBERAhAREQAQEREBEBE
        RARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQAQERE
        BEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhAREQA
        QEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBERAhA
        REQAQEREBEBERARAREQAQERECEBERABAREQEQEREBEBERABAREQIQEREAEBERARAREQEQEREAEBE
        RAQAAAAAQEREAkBERABAREQAQEREAgAAAABAREQCQEREAEBERABAREQCAAAAAEBERAJAREQAQERE
        AEBERAIAAAAAQEREAkBERABAREQAQEREAgAAAABAREQCQEREAEBERABAREQCAAAAAEBERAJAREQA
        QEREAEBERAIAAAAAQEREAkBERABAREQAQEREAgAAAABAREQCQEREAEBERABAREQCAAAAAEBERAJA
        REQAQEREAEBERAIAAAAAQEREAkBERABAREQAQEREAgAAAABAREQCQEREAEBERABAREQCAAAAAEBE
        RAJAREQAQEREAEBERAIAAAAAQEREAkBERABAREQA////////////////////////////////////
        /////////////////////////////////////////////////////////////gAAAAAAAH/8AAAA
        AAAAf/7//v/+f/8//P/+//5//z/8//7//n//P/z//v//f/8//P/+//5//3/+//5//n//P/wAAAAA
        AAA//P/+//5//z/8//7//3//P/z//v/+f/9//v/+//5//z/8//7//n//P/z//v/+f/8//AAAAAAA
        AD/8//5//n//f/7//v/+f/8//P/+//5//z/8//7//n//P/z//v//f/8//P/+//5//3/+AAAAAAAA
        P/wAAAAAAAA//P/+//5//z/8//7//3//P/z//v/+f/9//v/+//5//z/8//7//n//P/whCEIQBCE/
        /AAAAAAAAD/8//7//n//f/7//v/+f/8//P/+//5//z/8//7//n//P/z//v//f/8//P/+//5//3/+
        AAAAAAAAP/wAAAAAAAA//AAAAAAAAD/8AAAAAAAAP/wAAAAAAAB//gAAAAAAAD/8AAAAAAAAP/wA
        AAAAAAA//kIQhCEIQn//////////////////////////////////////////////////////////
        //////////////////////////////////////8="""
        
        icon_data = base64.b64decode(icon)
        temp_file = 'temp_icon.ico'
        icon_file = open(temp_file, 'wb')
        icon_file.write(icon_data)
        icon_file.close()
        self.root.wm_iconbitmap(temp_file)
        os.remove(temp_file)        
        
        self.ajustar_ventana()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=LEFT, fill=Y)
        
        self.frame_entry = tk.Frame(self.frame)
        self.frame_entry.pack(side=TOP, expand=1)
        
        self.frame_btn = tk.Frame(self.frame)
        self.frame_btn.pack(side=BOTTOM)
        
        self.frame_btn2 = tk.Frame(self.frame_btn)
        self.frame_btn2.pack(side=TOP)
        
        self.crear_abrir()
        
        self.root.bind('<Return>', lambda e: self.abrir_archivo())
        

    def crear_abrir(self):
        self.btn_abrir = tk.Button(self.root, text='Abrir archivo', command=self.abrir_archivo, width=14)
        self.btn_abrir.pack(anchor=CENTER, pady=10)


    def crear_botones(self):        
        self.btn_deshacer = tk.Button(self.frame_btn2, text='↶', command=self.deshacer, width=3)
        self.btn_deshacer.pack(side=LEFT, padx=(10, 0), pady=0)
        Hovertip(self.btn_deshacer, 'Deshacer eliminado', hover_delay=500)
        
        self.btn_borrar_entry = tk.Button(self.frame_btn2, text='🗑', command=self.borrar_entry, width=3)
        self.btn_borrar_entry.pack(side=LEFT, padx=(10, 0), pady=0)
        Hovertip(self.btn_borrar_entry, 'Borrar entradas', hover_delay=500)        
        
        self.btn_abrir.destroy()
        self.btn_abrir = tk.Button(self.frame_btn, text='Abrir archivo', command=self.abrir_archivo, width=14)
        self.btn_abrir.pack(side=LEFT, padx=(20, 5), pady=10)
        
        self.btn_cargar = tk.Button(self.frame_btn, text='Cargar datos', command=self.cargar, width=14)
        self.btn_cargar.pack(side=LEFT, padx=5, pady=10)
        
        self.btn_eliminar = tk.Button(self.frame_btn, text='Eliminar último', command=self.eliminar_ultimo, width=14)
        self.btn_eliminar.pack(side=LEFT, padx=5, pady=10)        
        
        self.btn_guardar = tk.Button(self.frame_btn, text='Guardar archivo', command=self.guardar_archivo, width=14)
        self.btn_guardar.pack(side=LEFT, padx=(5, 10), pady=10)
        
        self.root.bind('<Return>', lambda e: self.cargar())


    def crear_entradas(self):
        alto = 65
        ancho = 50
        
        if self.tabla.index.is_numeric():
            n = len(self.tabla.columns)
        else:
            n = len(self.tabla.columns)+1
        
        alto_total = 70+(alto*n)
        ancho_total = 750+(ancho*n)
        
        self.ajustar_ventana((ancho_total if ancho_total < self.root.winfo_screenwidth() else int(self.root.winfo_screenwidth()*0.85)), (alto_total if alto_total < self.root.winfo_screenheight() else int(self.root.winfo_screenheight()*0.85)))
        
        for l, e in zip(self.label, self.entry):
            l.destroy()
            e.destroy()
        
        self.label = []
        self.entry = []
        
        for f in self.frame_entries:
            f.destroy()
        for f in self.frame_combo:
            f.destroy()
            
        self.frame_entries = []
        self.frame_combo = []
        
        if alto_total < self.root.winfo_screenheight():
            if self.tabla.index.is_numeric():
                for i, x in enumerate(self.tabla.columns):
                    self.label.append(tk.Label(self.frame_entry, text=x+':'))                
                    self.entry.append(tk.Entry(self.frame_entry))
                    
                    self.label[i].pack()
                    self.entry[i].pack(pady=10)
            else:
                for i, x in enumerate([self.tabla.index.name, *self.tabla.columns]):
                    self.label.append(tk.Label(self.frame_entry, text=x+':'))                
                    self.entry.append(tk.Entry(self.frame_entry))
                    
                    self.label[i].pack()
                    self.entry[i].pack(pady=10)
        else:
            condicion = lambda i: i % (alto_total // self.root.winfo_screenheight() +1) == 0            
            
            if self.tabla.index.is_numeric():
                self.frame_entries.append(tk.Frame(self.frame_entry))
                self.frame_entries[0].pack(side=TOP, expand=1)
                
                for i, x in enumerate(self.tabla.columns):
                    if condicion(i):
                        self.frame_entries.append(tk.Frame(self.frame_entry))
                        self.frame_entries[-1].pack(side=TOP, expand=1)
                        
                    self.frame_combo.append(tk.Frame(self.frame_entries[-1]))
                    self.frame_combo[-1].pack(side=LEFT, expand=1, padx=15)
                    
                    self.label.append(tk.Label(self.frame_combo[-1], text=x+':'))                
                    self.entry.append(tk.Entry(self.frame_combo[-1]))
                    
                    self.label[i].pack()
                    self.entry[i].pack(pady=10)
            else:
                for i, x in enumerate([self.tabla.index.name, *self.tabla.columns]):
                    self.label.append(tk.Label(self.frame_entry, text=x+':'))
                    self.entry.append(tk.Entry(self.frame_entry))
                    
                    self.label[i].pack()
                    self.entry[i].pack(pady=10)
        
        if not hasattr(self, 'btn_cargar') and not hasattr(self, 'btn_eliminar') and not hasattr(self, 'btn_guardar'):
            self.crear_botones()


    def ajustar_ventana(self, ventana_ancho=315, ventana_alto=50):
        # Ancho y alto de la pantalla
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()

        # Centrar        
        x = (pantalla_ancho/2 - ventana_ancho/2)
        y = (pantalla_alto/2 - ventana_alto/2) * 0.8

        self.root.geometry(f'{ventana_ancho}x{ventana_alto}+{int(x)}+{int(y)}')
        
        
    def crear_lista(self):
        if self.cuadro:
            self.cuadro.destroy()
        
        if self.frame_cuadro:
            self.frame_cuadro.destroy()
            self.scrollbar.destroy()
            self.scrollbar2.destroy()
            
        self.frame_cuadro = tk.Frame(self.root)
        self.frame_cuadro.pack(side=RIGHT, fill='both', expand=1)
            
        self.scrollbar = tk.Scrollbar(self.frame_cuadro)
        self.scrollbar.pack(side=RIGHT, fill=Y, padx=(0, 5), pady=10)
        
        self.scrollbar2 = tk.Scrollbar(self.frame_cuadro, orient=HORIZONTAL)
        self.scrollbar2.pack(side=BOTTOM, fill=X, pady=(0, 10), padx=(10, 0))
        
        self.cuadro = tk.Text(self.frame_cuadro, yscrollcommand=self.scrollbar.set, xscrollcommand=self.scrollbar2.set, wrap='none')  
        self.scrollbar.config(command=self.cuadro.yview)
        self.scrollbar2.config(command=self.cuadro.xview)
        
        self.cuadro.pack(side=LEFT, fill='both', expand=1, padx=(10, 0), pady=(10, 0))
        
        self.cuadro.insert(tk.INSERT, self.tabla.to_string())
        # Centrar Text
        # self.cuadro.tag_configure('center', justify='center')
        # self.cuadro.tag_add('center', 1.0, 'end')
        self.cuadro.config(state=DISABLED)        
        
    def borrar_entry(self):
        for e in self.entry:
                e.delete(0, tk.END)
        
        self.entry[0].focus_set()
            
    
    # Dataframe    
    def guardar_archivo(self):
        archivo_guardado = filedialog.asksaveasfilename(initialdir='./', title='Guardar archivo', initialfile='tabla.xlsx', defaultextension='*.xlsx', filetypes=[('Excel', '*.xlsx *.xls'), ('CSV', '*.csv')])
        
        try:
            if archivo_guardado.endswith('.xlsx') or archivo_guardado.endswith('.xls'):
                self.tabla.to_excel(archivo_guardado)
            elif archivo_guardado.endswith('.csv'):
                self.tabla.to_csv(archivo_guardado)
        except:
            pass        
        
    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(initialdir='./', title='Seleccionar archivo', filetypes=[("all files","*.*"), ('Excel files', '*.xlsx *.xls'), ('CSV files', '*.csv')])
        
        if not ruta:
            return
        
        self.tabla = None
        
        delattr(self, 'tabla')
        try:
            if ruta.endswith('.xls') or ruta.endswith('xlsx'):
                self.tabla = pd.read_excel(ruta, index_col=0)
            elif ruta.endswith('.csv'):
                self.tabla = pd.read_csv(ruta, index_col=0)
        except:
            print('no existe el archivo')
        
        self.crear_entradas()
        self.crear_lista()
        self.entry[0].focus_set()


    def cargar(self):                
        if self.tabla.index.is_numeric():
            nuevo = pd.DataFrame([[e.get() for e in self.entry]], columns=self.tabla.columns)
            
            if self.tabla.index.name != '':
                nuevo[self.tabla.index.name] = self.tabla.index[-1]+1
                nuevo = nuevo.set_index(self.tabla.index.name)
                self.tabla = self.tabla.append([nuevo], ignore_index=False)
            else:
                self.tabla = self.tabla.append([nuevo], ignore_index=True)
                self.tabla.index += 1
        else:
            nuevo = pd.DataFrame([[e.get() for e in self.entry]], columns=self.tabla.columns.insert(0, self.tabla.index.name)).set_index(self.tabla.index.name)
            self.tabla = self.tabla.append([nuevo], ignore_index=False)
            
        self.borrar_entry()        
        self.crear_lista()        
        self.cuadro.yview_moveto(1)
        
    def eliminar_ultimo(self):
        self.eliminados.append(self.tabla.iloc[-1])
        
        self.tabla = self.tabla.iloc[:-1]
        self.crear_lista()
        self.cuadro.yview_moveto(1)
        
    def deshacer(self):
        try:
            self.tabla = self.tabla.append([self.eliminados.pop()])
            self.crear_lista()
            self.cuadro.yview_moveto(1)
        except:
            pass


ventana = Ventana()

ventana.ajustar_ventana()

try:
    ventana.tabla = pd.read_excel('./tabla.xlsx')
except:
    ventana.tabla = pd.DataFrame()


ventana.root.mainloop()