import pandas as pd
import sqlite3


class ContactDataBase:
    def __init__(self):
        self.conn = sqlite3.connect('./database/Base_de_Contatos.db')
        self.cursor = self.conn.cursor()

    def readContacts(self):
        df = pd.read_sql_query("SELECT * FROM CONTATOS", self.conn)
        celulares = df.CELULAR
        return celulares.values
        

    def readContact(self, contato):
        df = pd.read_sql_query("SELECT * FROM CONTATOS", self.conn)
        listCelular = list(df['CELULAR'])
        if contato in listCelular:
            return contato
        else:
            return "Este contato não está registrado ainda!"


    def insertContact(self,celular):
        celular = celular.replace('-','')
        celular = celular.replace(' ','')
        sql = f"INSERT INTO `CONTATOS` (`CELULAR`,`ENVIADO`) VALUES ('{celular}','False')"
        self.cursor.execute(sql)
        self.conn.commit()
        return 'Celular inserido com sucesso!'

    def insertContacts(self,pathFileContatos):
        wb = pd.read_excel(pathFileContatos)
        df = pd.DataFrame(wb)
        df['CELULAR'] = df['CELULAR'].astype('str')
        for i,row in df.iterrows():
            cel = row.values[0].replace('-','')
            cel = cel.replace(' ','')
            sql = f"INSERT INTO `CONTATOS` (`CELULAR`,`ENVIADO`) VALUES ('{cel}','{row.values[1]}')"
            self.cursor.execute(sql)
        self.conn.commit()
        return 'Registros inseridos com sucesso!'
    
    def limparBase(self):
        sql = "DELETE FROM CONTATOS WHERE ENVIADO='False' OR ENVIADO='True';"
        self.cursor.execute(sql)
        self.conn.commit()
        return 'Base apagada com sucesso!'

    def deleteContact(self, contato):
        df = pd.DataFrame(self.wb)
        index = df[(df.CELULAR == contato)].index

        df.drop(index, inplace=True)     
        df.to_excel(self.pathBaseDeContatos, index=False, encoding="ISO-8859-1")
        print('Contato Removido com sucesso!')

    def deleteContacts(self, pathFileContatos):
        df = pd.DataFrame(self.wb)
        df_contatos = pd.read_excel(pathFileContatos)
        celulares = df_contatos['CELULAR']
        
        for celular in celulares:
            index = df[(df.CELULAR == celular)].index
            df.drop(index, inplace=True)  
        df.to_excel(self.pathBaseDeContatos, index=False, encoding="ISO-8859-1")
        print('Contatos Removidos com sucesso!')

if __name__ == "__main__":
    dbContatos = ContactDataBase()
    celular = dbContatos.readContact('11950735276') #11 94232-6639
    print(celular)


# dbContatos = baseContatos.ContactDataBase()
# Exibindo todos os contatos
# contatos = dbContatos.readContacts()

# Exibindo somente um contato
# celular = dbContatos.readContact('11 94232-6639')
# print(celular.values)

# Inserindo um novo contato
# dbContatos.insertContact('11 94232-6639')

#Inserindo contatos em lote
# dbContatos.insertContacts('./Contatos.xlsx')

#Deletando um contato por telefone
# dbContatos.deleteContact('11950735276')

#Deletando contatos por lote
# dbContatos.deleteContacts('./Contatos.xlsx')