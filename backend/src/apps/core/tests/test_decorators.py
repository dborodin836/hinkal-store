import io

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase
from contextlib import redirect_stdout

from src.apps.core.decorators import hide_stdout


class TestDecorators(TestCase):
    def test_hide_output_no_return(self):
        @hide_stdout
        def my_sum(int_1: int, int_2: int):
            print(int_1 + int_2)

        stream = io.StringIO()
        file = InMemoryUploadedFile(stream, None, "tmp.txt", None, stream.tell(), None)
        with redirect_stdout(file):
            my_sum(42, 69)
        file.seek(0)  # VERY IMPORTANT
        self.assertEqual(file.read(), "")

    def test_hide_output_with_return(self):
        @hide_stdout
        def my_sum(int_1: int, int_2: int):
            res = int_1 + int_2
            print(res)
            return res

        stream = io.StringIO()
        file = InMemoryUploadedFile(stream, None, "tmp.txt", None, stream.tell(), None)
        with redirect_stdout(file):
            output = my_sum(42, 69)
            self.assertEqual(output, 111)
        file.seek(0)  # VERY IMPORTANT
        self.assertEqual(file.read(), "")
