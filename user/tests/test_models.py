from django.test import TestCase
from user.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Oh', last_name='My')

    def test_first_name_label(self):
        author = Author.objects.get(first_name='Oh')
        filed_label = author._meta.get_field('first_name').verbose_name

        self.assertEqual(filed_label, 'first name')


class SamleTestClass(TestCase):

    # 클래스 전체에서 사용되는 설정을 위해 테스트 시작될때 한번 실행
    @classmethod
    def setUpTestData(cls):
        print("setup test data - 1")

    # 각각의 테스트 메소드가 실행될 떄 실행
    def setUp(self):
        print("setup test data - 2")

    @classmethod
    def tearDownClass(cls):
        print("tear down - end")

    def test_save_author(self):
        # given
        first_name = "Oh"
        last_name = "kk"

        # when
        author = Author(first_name=first_name, last_name=last_name)
        author.save()

        # then
        author = Author.objects.get(first_name=first_name)
        self.assertEqual(author.first_name, first_name)



