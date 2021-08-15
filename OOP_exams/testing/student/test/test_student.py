import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("George", {"Python": [1, 2, 3]})
        self.student_without_courses = Student("Peter")

    def test_init(self):
        self.assertEqual(self.student_without_courses.courses, {})

    def test_init_with_course(self):
        self.assertEqual(self.student.name, "George")
        self.assertEqual(self.student.courses, {"Python": [1, 2, 3]})

    def test_init_with_none_course(self):
        s = Student("Harry", None)
        self.assertEqual(s.courses, {})

    def test_enroll_update(self):
        course_name = "Python"
        notes = [4, 5]
        res_dict = {"Python": [1, 2, 3, 4, 5]}
        res_msg = "Course already added. Notes have been updated."
        self.student.enroll(course_name, notes)
        self.assertEqual(self.student.courses, res_dict)
        self.assertEqual(self.student.enroll(course_name, notes), res_msg)

    def test_enroll_with_notes(self):
        course_name = "OOP"
        notes = [1, 2, 3]
        res_dict = {"OOP": [1, 2, 3]}
        res_msg = "Course and course notes have been added."
        self.assertEqual(self.student_without_courses.enroll(course_name, notes), res_msg)
        self.assertEqual(self.student_without_courses.courses, res_dict)

    def test_enrol_without_notes(self):
        course_name = "Python"
        notes = [1, 2, 3]
        res_dict = {"Python": []}
        res_msg = "Course has been added."
        self.assertEqual(self.student_without_courses.enroll(course_name, notes, "N"), res_msg)
        self.assertEqual(self.student_without_courses.courses, res_dict)

    def test_add_notes_existing_course(self):
        course_name = "Python"
        notes = 'notes'
        res_dict = res_dict = {"Python": [1, 2, 3, notes]}
        res_msg = "Notes have been updated"
        self.assertEqual(self.student.add_notes(course_name, notes), res_msg)
        self.assertEqual(self.student.courses, res_dict)

    def test_add_notes_non_existing_course(self):
        course_name = "JavaScript"
        notes = 'notes'
        res_msg = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name, notes)
        self.assertEqual(res_msg, str(ex.exception))
        self.assertEqual(self.student.courses, {"Python": [1, 2, 3]})

    def test_leave_course_successful(self):
        course_name = "Python"
        res = self.student.leave_course(course_name)
        res_msg = "Course has been removed"
        self.assertEqual(res, res_msg)
        self.assertEqual(self.student.courses, {})

    def test_leave_course_unsuccessful(self):
        course_name = "Javascript"
        res_msg = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course_name)
        self.assertEqual(res_msg, str(ex.exception))

