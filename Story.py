class Node: # 내용이 담긴 자료구조
    def __init__(self):
        self.story = ""
        
    def printStory(self):
        print(self.story)

class TitleNode(Node):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.__next = None
        
    def addSelection(self, nextNode):
        self.__next = nextNode
    
    def getNextSelection(self):
        return self.__next
    
    def printStory(self):
        print("===== " + self.title + " ======\n\n")
        print(self.story)
        print()
        
        
    

class StoryNode(Node): # 단일 흐름 스토리
    def __init__(self):
        super().__init__() #부모먼저 실행
        self.__next = None
    
    def addSelection(self, nextNode):
        assert(self.__next == None) # 다음 노드 확인, 있다면 다음 스토리 중간에 변경 불가하도록 체크
        self.__next = nextNode
    
    def getNextSelection(self): #다음 노드를 반환 함수
        return self.__next

class SelectionNode(Node): # 선택지를 물어보는 스토리
    def __init__(self):
        super().__init__()
        self.__next = list()
    
    def addSelection(self, nextNode):
        assert(type(nextNode) is StoryNode) # 분기의 선택지는 반드시 스토리 노드로 연결되어야 한다
        self.__next.append(nextNode)
        
    def getNextSelection(self, idx):
        return self.__next[idx]
    
    def printStory(self):
        print(self.story)
        print()
        
        for i in range(len(self.__next)):
            print(i+1, ". ", self.__next[i].story)

class EndingNode(Node): #엔딩
    def __init__(self, endingType):
        super().__init__()
        self.endingType = endingType
        self.endingTitle = ""
        
    def printStory(self):
        print(self.story)
        print()
        print("~ " + self.endingType + " - " + self.endingTitle + " ~ ")
        print()

class StoryExcutor: #스토리 실행
    def __init__(self, titleNode, startNode):
        self.__title = titleNode
        self.__root = startNode
        self.__head = self.__title
    
    def execute(self): 
        self.__head.printStory()
        
        if(type(self.__head) is TitleNode):
            self.__head = self.__head.getNextSelection()
        elif(type(self.__head) is StoryNode): # 스토리 노드 작동 방식
            self.__head = self.__head.getNextSelection()
        elif(type(self.__head) is SelectionNode): # 분기 노드 작동 방식
            self.__chooseSelection()
            
        elif(type(self.__head) is EndingNode):  # 엔딩 노드 작동 방식
            self.__gameover()
            
        else:    # 그냥 노드 -> 오류 상황!
            raise Exception("Node class는 인스턴스를 생성하면 안됩니다!")
        
        print("\n" + "="*30 + "\n")
    
    def isEnd(self):
        return self.__head == None
    
    def __chooseSelection(self): # 입력을 받아 선택지를 이동함
       
        while True:
            try:
                idx = int(input("\n당신의 선택은... "))
                self.__head = self.__head.getNextSelection(idx-1) # 선택한 분기의 스토리 노드로 넘어간다
                self.__head = self.__head.getNextSelection() # 분기 출력 시 이미 출력한 내용이므로 다음 노드로 바로 넘긴다
                break
            except BaseException as e:
                print("[ Error ] 번호를 잘못 입력했습니다!")        
        print()
        
    def __gameover(self): # 다시하기를 물어봄
        if(self.__head.endingType == "BAD ENDING"):
            print("Game Over...")
        elif(self.__head.endingType == "HAPPY ENDING"):
            print("Clear!")
        elif(self.__head.endingType == "HIDDEN ENDING"):
            print("Clear...?")
        else:
            raise Exception("Ending Type은 BAD, HAPPY, HIDDEN 3가지 밖에 없습니다!")
              
        while True:
            try:
                play_again = int(input("\n다시하시겠습니까? \n 1. 다시하기 \n 2. 나가기 \n\n번호 입력 : "))
                
                if(play_again == 1):
                    # 다시하기 코드
                    print("\n 앗 다시 태어났다! \n")
                    self.__head = self.__root
                elif(play_again == 2):
                    #나가기 코드
                    self.__endingScroll()
                    self.__head = None
                else:
                    raise KeyError()

                break
            except:
                print("[ Error ] 번호를 잘못 입력했습니다!\n")
            
    def __endingScroll(self):
        print("\n===== 우당당탕 크리스마스 소동 =====")
        print("팀 : 파이썬의 신")
        print("팀장 : 이홍주")
        print("스토리 기획 : 박혜민")
        print("게임 개발 : 이홍주")
        print("PPT : 강진영")
        
        print("\n\n   플레이해주셔서 감사합니다.   \n\n")