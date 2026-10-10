# AgroVisión, capítulo 11: composición del lote y criterios de revisión manual.
# Parte de las predicciones que guarda NB_LIBRO_12 (resultados/cap10_experimentos/robustez_predicciones.csv).
# Uso, desde la raíz del repositorio:
#     python guiones/cap11_indicadores.py resultados valores_cap11.json
# Requiere pandas y numpy. No usa GPU y termina en segundos.
import sys,json,itertools,pandas as pd,numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
Z=sys.argv[1]+'/cap10_experimentos/'
d=pd.read_csv(Z+'robustez_predicciones.csv'); d['ok']=d.real==d.pred
P=d[['p_damaged','p_empty','p_overripe','p_ripe','p_unripe']].values; s=np.sort(P,axis=1)
d['pmax']=s[:,-1]; d['margen']=s[:,-1]-s[:,-2]
V={}
o=d[d.familia=='original'].copy()
def regla(x,a=0.75,b=0.25): return ~((x.pmax>=a)&(x.margen>=b))
def resumen(x,marca):
    n=len(x); e=(~x.ok).sum(); m=marca.sum(); em=(marca&~x.ok).sum()
    return dict(n=int(n),errores=int(e),marcadas=int(m),frac_marcadas=round(m/n,3),errores_marcados=int(em),frac_err=round(em/max(e,1),3),falsas=int(m-em),exactitud_resto=round(((~marca)&x.ok).sum()/max((~marca).sum(),1),3),errores_resto=int(e-em))
print('REGLA proyecto, nueve modelos:',resumen(o,regla(o)))
V['regla_original']=resumen(o,regla(o))
L=[]
for u in [0.6,0.75,0.9,0.95,0.98,0.99,0.995,0.999]:
    r=resumen(o,o.pmax<u); r['umbral']=u; L.append(r)
print(pd.DataFrame(L).to_string()); V['umbral_pmax']=L
# por modelo
pm=[]
for m,x in o.groupby('modelo'):
    r=resumen(x,regla(x)); r['modelo']=m; r['conf_err']=round(x[~x.ok].conf.mean(),3); pm.append(r)
print(pd.DataFrame(pm).to_string()); V['regla_por_modelo']=pm
# desacuerdo entre dos modelos
piv=o.pivot(index='imagen',columns='modelo',values='pred'); real=o.drop_duplicates('imagen').set_index('imagen').real.reindex(piv.index)
D=[]
for a,b in itertools.combinations(piv.columns,2):
    des=piv[a]!=piv[b]; ea=piv[a]!=real; D.append(dict(a=a,b=b,desacuerdo=int(des.sum()),err_a=int(ea.sum()),err_a_marcados=int((des&ea).sum()),err_b=int((piv[b]!=real).sum()),err_b_marcados=int((des&(piv[b]!=real)).sum())))
D=pd.DataFrame(D); print('desacuerdo pares: media',D.desacuerdo.mean().round(2),'errores cubiertos', (D.err_a_marcados.sum()+D.err_b_marcados.sum())/(D.err_a.sum()+D.err_b.sum()))
V['desacuerdo']=dict(media_desacuerdos=float(D.desacuerdo.mean()),frac_errores=float((D.err_a_marcados.sum()+D.err_b_marcados.sum())/(D.err_a.sum()+D.err_b.sum())))
# ambos modelos se equivocan igual
# composición del lote
comp=pd.DataFrame({'real':o.real.value_counts(normalize=True),'pred':o.pred.value_counts(normalize=True)}); print(comp.round(3))
pc=o.groupby('modelo').pred.value_counts(normalize=True).unstack().fillna(0); print(pc.round(3)); print(pc.agg(['min','max']).round(3))
V['composicion']={'real':comp.real.round(4).to_dict(),'pred_media':comp.pred.round(4).to_dict(),'pred_min':pc.min().round(4).to_dict(),'pred_max':pc.max().round(4).to_dict()}
for f,n in [('desenfoque',1.0),('desenfoque',2.5),('resolucion',4.0),('contraste',0.3),('oscurecer',0.35)]:
    x=d[(d.familia==f)&(d.nivel==n)]; c=x.pred.value_counts(normalize=True); print(f,n,c.round(3).to_dict(),resumen(x,regla(x)))
    V['%s_%s'%(f,n)]={'composicion':c.round(4).to_dict(),'regla':resumen(x,regla(x))}
# matriz de costos: errores por tipo, nueve modelos
ct=pd.crosstab(o.real,o.pred); print(ct)
V['confusion_9']=ct.to_dict()
# tipos de error con consecuencia
print('inmaduro->maduro',ct.loc['unripe','ripe'],'maduro->inmaduro',ct.loc['ripe','unripe'],'vacio->otra',18-ct.loc['empty','empty'],'maduro->sobremaduro',ct.loc['ripe','overripe'],'sobremaduro->maduro',ct.loc['overripe','ripe'])
# m_2026
x=o[o.modelo=='m_2026']; print('m_2026',resumen(x,regla(x)), x[~x.ok][['imagen','real','pred','pmax','margen']].to_string())
x=o[o.modelo=='n_2026']; print('n_2026',resumen(x,regla(x)))
# intervalo binomial de una proporción en n racimos
from math import sqrt
for n in [30,70,100,200,400]:
    p=0.43; print(n, round(1.96*sqrt(p*(1-p)/n),3))
json.dump(V,open(sys.argv[2],'w'),ensure_ascii=False,indent=1,default=float)
