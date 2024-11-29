import mysql.connector
class base_model:
    conn = mysql.connector.connect(
        host="localhost",
        user="JustHieu15",
        password="hieuthao1",
        database="final_python"
    )

    cursor = conn.cursor()

    def get_table_name(self):
        return self.__class__.__name__.lower()

    def get_fields(self):
        return {name: value for name, value in vars(self).items() if not name.startswith('_')}

    def save(self):
        table_name = self.get_table_name()
        fields = self.get_fields()
        columns = ",".join(fields.keys())
        placeholders = ",".join(['%s'] * len(fields))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        base_model.cursor.execute(sql, tuple(fields.values()))
        base_model.conn.commit()
        return base_model.cursor.lastrowid

    def update(self, id):
        table_name = self.get_table_name()
        fields = self.get_fields()
        set_clause = ','.join([f"{k} = %s" for k in fields.keys()])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE id =%s )"
        values = list(fields.values()) + [id]
        base_model.cursor.execute(sql, values)
        base_model.conn.commit()
        return base_model.cursor.rowcount

    @classmethod
    def findAll(cls):
        table_name = cls.__name__.lower()
        sql = f"SELECT * FROM {table_name}"
        base_model.cursor.execute(sql)
        results = base_model.cursor.fetchall()
        return results
