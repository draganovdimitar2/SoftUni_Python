from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.test_student = Student("Test")

    def test_init(self):
        self.assertEqual("Test", self.test_student.name)
        self.assertNotEqual(None, self.test_student.courses)
        self.assertEqual({}, self.test_student.courses)

        self.test_student.courses["some_course"] = ['some_notes']  # add some course to test it
        self.assertEqual({"some_course": ["some_notes"]}, self.test_student.courses)

    def test_enroll_course_already_added(self):
        self.test_student.courses["some_course"] = ['some_notes']
        method = self.test_student.enroll("some_course", ['first_note', 'second_note'])
        self.assertEqual("Course already added. Notes have been updated.", method)

    def test_enroll_add_course(self):
        self.test_student.courses["some_course"] = ['some_notes']
        method = self.test_student.enroll("another_course", ['first_note', 'second_note'], "")
        self.assertIn("another_course", self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", method)

        method = self.test_student.enroll("another_course1", ['first_note', 'second_note'], "Y")
        self.assertIn("another_course1", self.test_student.courses)
        self.assertEqual("Course and course notes have been added.", method)

        method = self.test_student.enroll("another_course2", ['first_note', 'second_note'], "N")
        self.assertIn("another_course2", self.test_student.courses)
        self.assertEqual([], self.test_student.courses["another_course2"])
        self.assertEqual("Course has been added.", method)

    def test_add_notes_error_raises(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("Not found", "")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

        self.test_student.courses["some_course"] = ['some_notes']
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("Not found", "")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_success(self):
        self.test_student.courses["some_course"] = ['some_notes']
        method = self.test_student.add_notes("some_course", "another_note")
        self.assertIn("another_note", self.test_student.courses["some_course"])
        self.assertEqual("Notes have been updated", method)

    def test_leave_course_error_raise(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("Not found")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        self.test_student.courses["some_course"] = ['some_notes']
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("Not found")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_success(self):
        self.test_student.courses["some_course"] = ['some_notes']
        self.assertIn('some_notes', self.test_student.courses.get("some_course"))
        method = self.test_student.leave_course("some_course")

        self.assertEqual(None, self.test_student.courses.get("some_course", None))
        self.assertEqual("Course has been removed", method)


if __name__ == "__main__":
    main()
