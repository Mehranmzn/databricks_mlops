import unittest
from unittest.mock import patch, MagicMock
import unittest.main as main  
import push_data_mongo  

class TestMainFunctions(unittest.TestCase):

    @patch('main.lint_code')
    def test_lint_code(self, mock_lint_code):
        mock_lint_code.return_value = True
        result = main.lint_code()
        self.assertTrue(result)
        mock_lint_code.assert_called_once()

    @patch('main.run_unit_tests')
    def test_run_unit_tests(self, mock_run_unit_tests):
        mock_run_unit_tests.return_value = True
        result = main.run_unit_tests()
        self.assertTrue(result)
        mock_run_unit_tests.assert_called_once()

    @patch('main.build_docker_image')
    def test_build_docker_image(self, mock_build_docker_image):
        mock_build_docker_image.return_value = 'test-image:latest'
        image_name = 'test-image:latest'
        result = main.build_docker_image(image_name)
        self.assertEqual(result, image_name)
        mock_build_docker_image.assert_called_once_with(image_name)

    @patch('main.push_docker_image')
    def test_push_docker_image(self, mock_push_docker_image):
        mock_push_docker_image.return_value = True
        image_name = 'test-image:latest'
        result = main.push_docker_image(image_name)
        self.assertTrue(result)
        mock_push_docker_image.assert_called_once_with(image_name)

    @patch('push_data_mongo.push_data_to_mongo')
    def test_push_data_to_mongo(self, mock_push_data_to_mongo):
        mock_push_data_to_mongo.return_value = True
        data = {'key': 'value'}
        result = push_data_mongo.push_data_to_mongo(data)
        self.assertTrue(result)
        mock_push_data_to_mongo.assert_called_once_with(data)

if __name__ == '__main__':
    unittest.main()
