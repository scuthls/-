from question_classifier import *
from question_parser import *
from answer_search import *

class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '这个问题知识库中暂时没有，知识库将持续更新，敬请期待！'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        print(final_answers)
        if not final_answers:
            return "这个问题知识库中暂时没有，知识库将持续更新，敬请期待！"
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('input an question:')
        answers = handler.chat_main(question)
        print(answers)