import sqlite3
import pandas as pd

conn = sqlite3.connect('./database/Base_de_Contatos.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE contatos (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         CELULAR TEXT,
#         ENVIADO boolean
# );
# """)

# print('Tabela criada com sucesso.')

#Insert in database 
df = pd.read_excel('C://Users//f48014593820//Documents//Workspace//WhatsAppBot//bot_whatsapp_envio_mensagens-master//Contatos.xlsx')
df['CELULAR'] = df['CELULAR'].astype('str')
cols = "`,`".join([str(i) for i in df.columns.tolist()])
for i,row in df.iterrows():
    sql = f"INSERT INTO `CONTATOS` (`CELULAR`,`ENVIADO`) VALUES ('{row.values[0]}','{row.values[1]}')"
    cursor.execute(sql)
    conn.commit()


df = pd.read_sql_query("SELECT * FROM CONTATOS", conn)
print(df.head())



# desconectando...
conn.close()