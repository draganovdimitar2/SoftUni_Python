from project.senior_student import SeniorStudent
from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    def setUp(self):
        self.senior_student = SeniorStudent("00001", "Test", 5.56)

    def test_init_success(self):
        self.assertEqual("00001", self.senior_student.student_id)
        self.assertEqual("Test", self.senior_student.name)
        self.assertEqual(5.56, self.senior_student.student_gpa)
        self.assertEqual(set(), self.senior_student.colleges)

    def test_init_error_raises(self):
        with self.assertRaises(Exception) as ex:
            self.senior_student.student_id = "1"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.senior_student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.senior_student.student_gpa = 0.5
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_to_college_success(self):
        method = self.senior_student.apply_to_college(5, "Test")
        self.assertEqual({"TEST"}, self.senior_student.colleges)
        self.assertEqual("Test successfully applied to Test.", method)

    def test_apply_to_college_application_fail(self):
        before_method_call = self.senior_student.colleges
        method = self.senior_student.apply_to_college(6.00, "Test")
        self.assertEqual('Application failed!', method)
        self.assertEqual(before_method_call, self.senior_student.colleges)

    def test_update_gpa_success(self):
        method = self.senior_student.update_gpa(7.00)
        self.assertEqual(7.00, self.senior_student.student_gpa)
        self.assertEqual('Student GPA was successfully updated.', method)

    def test_update_gpa_error_raises(self):
        method = self.senior_student.update_gpa(0.1)
        self.assertEqual('The GPA has not been changed!', method)
        self.assertEqual(5.56, self.senior_student.student_gpa)

    def test_eq(self):
        other_student = SeniorStudent("00002", "Test2", 5.56)
        self.assertEqual(other_student, self.senior_student)


if __name__ == "__main__":
    main()
