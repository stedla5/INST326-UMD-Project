import  unittest
import Project_326

class testProject(unittest.TestCase):

    def test_display_result(self):
        self.correct =6
        q=6
        result=(self.correct / len(q) * 100)
        self.assertEqual(result, self.correct / len(q))
    

if __name__ == "__main__":
    unittest.main()