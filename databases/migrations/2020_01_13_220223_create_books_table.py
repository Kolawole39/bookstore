from orator.migrations import Migration


class CreateBooksTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('books') as table:
            table.increments('id')
            table.string('title')
            table.string('description')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('books')
