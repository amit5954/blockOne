import random

try:
    from app import app
    import unittest
    app.testing = True
except Exception as e:
    print("Something missing while pulling App for unittest" + str(e))


class FlaskTest(unittest.TestCase):
    tester = app.test_client()
    create_payload = {"firstName": 'Amit', "lastName": "amit", "classofStudent": '3 A', "nationality": 'India'}
    update_payload = {"firstName": 'Updated', "lastName": "Alien", "classofStudent": '5 A', "nationality": 'Pakistan'}
    student_id = random.randint(1, 10000)
    del_student = list()

    def test_create_student_201(self):
        response = self.tester.post("student/{}".format(self.student_id), json=self.create_payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'firstName' in response.data)

    def test_create_student_content_type(self):
        self.del_student.append(random.randint(1, 10000))
        response = self.tester.post("student/{}".format(self.del_student[0]), json=self.create_payload)
        self.assertEqual(response.content_type, "application/json")

    def test_create_student_content(self):
        response = self.tester.post("student/{}".format(random.randint(1, 10000)), json=self.create_payload)
        self.assertTrue(b'firstName' in response.data)

    def test_create_student_409(self):
        response = self.tester.post("student/3452", json=self.create_payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 409)

    def test_update_student_status_code(self):
        response = self.tester.put("student/{}".format(self.student_id), json=self.update_payload)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_student_content_type(self):
        response = self.tester.put("student/{}".format(self.student_id), json=self.update_payload)
        self.assertEqual(response.content_type, "application/json")

    def test_update_student_content(self):
        response = self.tester.put("student/{}".format(self.student_id), json=self.update_payload)
        statuscode = response.status_code
        self.assertTrue(b'firstName' in response.data)

    def test_get_student(self):
        response = self.tester.get("student/" + str(self.student_id))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_student_404(self):
        response = self.tester.get("student/" + str(55434534))
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_get_student_string_id(self):
        response = self.tester.get("student/" + str('stri'))
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_get_student_id_complex_number(self):
        response = self.tester.get("student/" + str('3+4j'))
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_get_student_null_id(self):
        response = self.tester.get("student/" + str(''))
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    def test_get_student_content_type(self):
        response = self.tester.get("student/" + str(self.student_id))
        self.assertEqual(response.content_type, "application/json")

    def test_get_student_content(self):
        response = self.tester.get("student/" + str(self.student_id))
        self.assertTrue(b'firstName' in response.data)

    def test_get_all_student(self):
        response = self.tester.get("/allstudents")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_all_student_content_type(self):
        response = self.tester.get("/allstudents")
        self.assertEqual(response.content_type, "application/json")

    def test_get_all_student_content(self):
        response = self.tester.get("/allstudents")
        self.assertTrue(b'firstName' in response.data)

    def test_delete_student_200(self):
        response = self.tester.delete("student/" + str(self.del_student[0]))
        statuscode = response.status_code
        self.assertEqual(statuscode, 204)

    def test_delete_student_404(self):
        response = self.tester.delete("student/660")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)


if __name__ == "__main__":
    unittest.main()
