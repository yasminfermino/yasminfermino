# Testando estruturação da captura dos dados de gov_lic_alteryx

import pandas as pd

def capturamaxdata(nometabela)
#roda conexão com CDP realizando um show partitons e tras todas as partiçoes existentes, assim podemos seguir com raciocinio de pegar a max data

df = pd.DataFrame({
    'AnoMesDia': ['20241010', '20241011', '20241012']
})

# Adiciona uma nova coluna, por exemplo, 'Descrição'
df['id'] = range(1, len(df)+1)
df = df.sort_values('id', ascending=False)

maxdata = df['AnoMesDia'].iloc[0]
print(maxdata)

# maxdtgla = def(ghp00036.gov_lic_alteryx)
# maxdtglar = def(ghp00036.gov_lic_alteryx_racion)
# maxdttp128 = def(ghp00036.tp128)

"""SELECT 
    a.funcional,
    a.maquina,
    a.lastmodified,
    b.supt,
    b.gerencia,
    b.coordenacao
FROM 
    ghp00036.gov_lic_alteryx a
RIGHT JOIN 
    ghp00036.gov_lic_alteryx_racion r ON a.funcional = r.funcional
WHERE 
    r.racion = TRUE
JOIN 
    ghp00036.tp128 b ON a.funcional = b.funcional"""