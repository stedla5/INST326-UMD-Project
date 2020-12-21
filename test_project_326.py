import  unittest
import Project_1
import json

class testProject(unittest.TestCase):

    def test_display_result(self):
        self.correct =6
        q=6
        result=(self.correct / len(q) * 100)
        self.assertEqual(result, self.correct / len(q))

    def test_question(self):
        #set up data to be compared in assert
        quiz_names_tester = {1:"INST 326 Quiz OOP Programming", 2:"Python Dictionary",3:"Python Variables and Data Types"}
        num = Project_1.quizName
        current_quiz_num = quiz_names_tester[num]
        a = 'answer' + str(num)
        q = 'question' + str(num)
        c = 'choices' + str(num)
        with open('quiz.json') as f:
            obj = json.load(f)
        answer_group_tester = (obj[a])
        question_group_tester = (obj[q])
        choices_group_tester = (obj[c])

       #____________________________________________________Tests___________________________________________________________
        #test1a: test for CORRECT quiz names dictionary
        self.assertEqual(quiz_names_tester , Project_1.quiz_group_names , "Should be the same dictionary as line 14")

        #test1b: test for INCORRECT quiz names dictionary
        self.assertFalse(Project_1.quiz_group_names ==  quiz_names_tester[1])
        
        #test2: test CORRECT current quiz name
        self.assertEqual(current_quiz_num, Project_1.quiz_group_names[num], f"Should be {current_quiz_num}")

        #test3a: Test CORRECT Question set
        self.assertEqual(question_group_tester , Project_1.q , "Should be the same dictionary as line 14")
        #test3b: Test CORRECT choices set
        self.assertEqual(choices_group_tester , Project_1.options , "Should be the same dictionary as line 14")
        #test3c: Test CORRECT answer set
        self.assertEqual(answer_group_tester , Project_1.a , "Should be the same dictionary as line 14")

       
 


if __name__ == "__main__":
    unittest.main() 


