import Utils

# Ctes -------------------------------------------------------------------------

URL = 'https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?y=24-25&t=s1&AC.T.2=AC.T.2&AC.S.1=AC.S.1&AC.L.5=AC.L.5&AC.TG.5=AC.TG.5&RI.T.2=RI.T.2&RI.S.1=RI.S.1&RI.L.7=RI.L.7&RI.TG.7=RI.TG.7&CVVS.T.1=CVVS.T.1&CVVS.S.3=CVVS.S.3&CVVS.L.9=CVVS.L.9&CVVS.TG.9=CVVS.TG.9&SI.T.1=SI.T.1&SI.S.-=SI.S.-&SI.L.9=SI.L.9&SI.TG.9=SI.TG.9&SR.T.1=SR.T.1&SR.S.1=SR.S.1&SR.L.2=SR.L.2&SR.TG.2=SR.TG.2&vista=tabla'
DATA_DIRECTORY = "dataApp/"
FILE_NAME = DATA_DIRECTORY+"horario.db"
todayDate = Utils.getTodayDate()

