from base_model import BaseModel


class SpaceModel(BaseModel):
    def get_all_spaces(self):
        sql_select = """SELECT id, "space", description FROM "space";"""
        self.cur.execute(sql_select)

        return self.cur.fetchall() or []

    def add_space(self, space_data):
        sql_insert = """
            INSERT INTO
               "space"
                ("space", description, updated)
            VALUES
              (%(space)s, %(description)s, now())
            RETURNING id, "space", description;
        """
        self.cur.execute(sql_insert, space_data)
        return self.cur.fetchone() or {}

    def edit_space(self, space_data):
        sql_update = """
            UPDATE "space"
               SET
                "space" = %(space)s,
                description = %(description)s,
                updated = now()
            WHERE id = %(id)s
            RETURNING id, "space", description
        """
        self.cur.execute(sql_update, space_data)
        return self.cur.fetchone() or {}

    def delete_space(self, space_id):
        sql_delete = """
            DELETE FROM "space"
            WHERE id = %(id)s;
        """

        self.cur.execute(sql_delete, {'id': space_id})
        return True
