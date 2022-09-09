import Utils

# Ctes -------------------------------------------------------------------------

URL = 'https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?vista=csv&y=22-23&t=s1&AL_T_2=AL.T.2&AL_S_3=AL.S.3&AL_L_8=AL.L.8&Cal_T_2=Cal.T.2&Cal_S_3=Cal.S.3&Cal_L_8=Cal.L.8&DS_T_3=DS.T.3&DS_S_3=DS.S.3&DS_L_5=DS.L.5&DS_TG_5=DS.TG.5&IPS_T_1=IPS.T.1&IPS_S_3=IPS.S.3&IPS_L_6=IPS.L.6&IPS_TG_6=IPS.TG.6&RI_T_2=RI.T.2&RI_S_3=RI.S.3&RI_L_8=RI.L.8&RI_TG_8=RI.TG.8'
FILE_NAME = "horario.db"
todayDate = Utils.getTodayDate()

# tipos de vista URL (parametro de URL "vista")
# [web , csv , ]
WEB = 'web'
CSV = 'csv'
TABLA = 'tabla'