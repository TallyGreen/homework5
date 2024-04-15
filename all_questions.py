import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = "True"

    # type: bool
    answers['(a) B'] = "False"

    # type: bool
    answers['(a) C'] = "False"

    # type: bool
    answers['(a) D'] = "True"

    # type: bool
    answers['(b) A'] = "True"

    # type: False
    answers['(b) B'] = "False"

    # type: bool
    answers['(b) C'] = "True"

    # type: bool
    answers['(b) D'] = "False"

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5*math.log((1-p)/p)"

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'Disagree'

    # type: explain_string
    answers['Explain'] = "The classifiers he's employing, akin to flipping a coin 1000 times, each have an error rate of 0.5 theoretically. Given their nature of random guessing, employing ensemble techniques won't likely yield favorable outcomes. This stems from the inability of these base classifiers to converge towards any specific class, even with boosting or bagging incorporated."
 
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 'p'

    # type: eval_float
    answers['(a) C2-TPR'] = '2 * p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2 * p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "C1 exhibits a lower true positive rate compared to C2, yet it also demonstrates a lower false positive rate. Without understanding the context of what the models are estimating, it's not possible to definitively declare one model superior to the other based on these metrics alone."
    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) explain'] = "Precision and recall metrics fail to consider the distinction between TP and FP.While recall may increase, so does the count of FP. TPR  and FPR are more apt in this scenario, as they offer a metric to highlight the random guessing aspect of each classifier."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "Although both classifiers exhibit identical precision, C2 boasts a superior Recall/TPR and F-1 Measure, albeit with a trade-off of a higher FPR. This indicates that C2 excels in identifying positives, and the presence of false positives is not significantly detrimental. However, if false positives carry a risk, then C1 would be the preferable choice."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'Precision, Recall, and F-1 Measure offer a more comprehensive perspective on performance by providing a proportional comparison of the two classifiers.'

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'C3 represents an improved version of C1. It achieves higher precision (superior even to C2), F-1 measure, and Recall, while maintaining the low FPR observed in C1. Although its metrics may not reach the level of C2, the trade-off of a slightly higher FPR is justifiable in my view.' 
    return answers



#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '(p * 100) / ((p * 100) + (p * 900))'

    # type: eval_float
    answers['(a) recall for C0'] = '(p * 100) / ((p * 100) + ((1-p) * 100))'

    # type: eval_float
    answers['(b) F-measure of C0'] = '2 * ((0.1 * p) / (0.1 + p))'

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers

#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 0.533,
        'precision': 0.615,
        'F-measure': 0.571,
        'accuracy': 0.88
    }
    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'F-measure emerges as the preferred metric among the three, as it integrates precision and recall into a single statistic. In scenarios with imbalanced classes, accuracy can be significantly biased, as it merely considers the total number of mistakes without discerning between false positives and false negatives, failing to address the discrepancy between them in context.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'
    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'missing a cancer diagnosis appears more critical than incorrectly diagnosing someone. Therefore, TPR/FPR stands out as the most appropriate metric for evaluation.'


    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'False positives and false negatives in this scenario are less severe, as receiving a spam email does not have life-threatening consequences. Therefore, F-measure provides a balanced assessment that considers both precision and recall.'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
