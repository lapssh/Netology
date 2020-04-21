import unittest
import os
import json
import app
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'fixtures/directories.json')
        f_documents = os.path.join(current_path, 'fixtures/documents.json')
        with open(f_documents, 'r', encoding='utf-8') as out_docs:
            documents = json.load(out_docs)
        with open(f_directories, 'r', encoding='utf-8') as out_dirs:
            directories = json.load(out_dirs)
        app.directories = directories
        app.documents = documents

    def test_check_document_existance(self):
        """Проверка наличия валидного документа, и отсутствия невалидного"""
        self.assertEqual(app.check_document_existance('11-2'), True)
        self.assertNotEqual(app.check_document_existance('левый документ, которого нет'), True)

    def test_show_all_docs_info(self):
        pass

    def test_add_new_doc(self):
        """Добавим новый документ, и убедимся, что он добавился"""
        new_doc_number = '5'
        new_doc_type = 'multipassport'
        new_doc_owner_name = 'Lilu Dallas'
        new_doc_shelf_number = '1'

        with patch('app.input', side_effect=[new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number]):
            self.assertEqual(app.add_new_doc(), new_doc_shelf_number)

        self.assertIn(new_doc_number, app.directories[new_doc_shelf_number])
        self.assertIn(new_doc_number, [doc['number'] for doc in app.documents])

    def test_remove_doc_from_shelf(self):
        """ Проверим есть ли документ на полке, удалим его, и проверим, что его нет"""
        self.assertIn('2207 876234', app.directories['1'])
        app.remove_doc_from_shelf('2207 876234')
        self.assertNotIn('2207 876234', app.directories['1'])

    def test_get_doc_owner_name(self):
        """Проверка работы фунцкии поиска имени по номеру документа"""
        with patch('app.input', return_value='2207 876234'):
            self.assertEqual(app.get_doc_owner_name(), 'Василий Гупкин')


if __name__ == '__main__':
    unittest.main()
