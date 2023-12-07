class StoryNode: #스토리 내용
    def __init__(self):
        self.story = ""
        self.__select = list()
        self.__next = list()
    
    def addSelection(self, selectText, nextNode):
        self.__select.append(selectText)
        self.__next.append(nextNode)
    
    def getSelectionList(self):
        return self.__select
    
    def getNextSelection(self, idx):
        return self.__next[idx]

class StoryExcutor: #스토리 실행
    def __init__(self, startNode):
        self.__root = startNode
        self.__head = startNode
    
    def execute(self):
        print("=" * 30)
        print()
        print(self.__head.story)
        print()
        
        if(self.__isEnding()):
            self.__head = None
            return
        
        for selection in self.__head.getSelectionList():
            print(selection)
        
        print()
        while True:
            try:
                idx = int(input("당신의 선택은... "))
                self.__head = self.__head.getNextSelection(idx-1)
                break
            except BaseException as e:
                print("[ Error ] 번호를 잘못 입력했습니다!")        
        print()
    
    def initialize(self):
        self.__head == self.__root
    
    def isFinish(self):
        return self.__head == None
    
    def __isEnding(self):
        return len(self.__head.getSelectionList()) == 0