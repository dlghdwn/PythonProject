from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    
    title = TitleNode()
    title.title = """우당당탕 크리스마스 소동"""
    title.story = """평범하게 길을 걷던 당신. \n크리스마스 날 이상한 일들이 펼쳐지는데... \n 당신은 살아남을 수 있을까?"""
    
    main01 = SelectionNode()
    main01.story = """1. 저기 쓰레기가 땅에 떨어져있다."""
    
    main01_01 = StoryNode()
    main01_01.story = """쓰레기를 줍는다."""
    
    main01_02 = StoryNode()
    main01_02.story = """쓰레기를 줍지 않는다."""
    
    main01_02_Ending = EndingNode("BAD ENDING")
    main01_02_Ending.endingTitle = """쓰레기 인간"""
    main01_02_Ending.story = """쓰레기를 줍지 않았다. 우우 쓰레기~"""
    
    main02 = SelectionNode()
    main02.story = """2. 앗! 몰래카메라 실험이었다! \n인터뷰에 응할까?"""
    
    main02_01 = StoryNode()
    main02_01.story = """인터뷰에 응한다."""
    
    main02_02 = StoryNode()
    main02_02.story = """인터뷰에 응하지 않는다."""
    
    main02_01_Ending = EndingNode("BAD ENDING")
    main02_01_Ending.endingTitle = """언제나 말조심"""
    main02_01_Ending.story = """인터뷰에 응했으나 말실수로 악플을 받았다..."""
    
    main03 = SelectionNode()
    main03.story = """3. 인터뷰를 무시하고 마저 가던 길을 간다 \n어느 쪽으로 갈까? """
    
    main03_01 = StoryNode()
    main03_01.story = """오른쪽"""
    
    main03_02 = StoryNode()
    main03_02.story = """왼쪽"""
    
    main03_02_Ending = EndingNode("BAD ENDING")
    main03_02_Ending.endingTitle = """길치"""
    main03_02_Ending.story = """길을 잃어버렸다..."""
    
    main04 = SelectionNode()
    main04.story = """4. 어떤 엔딩을 원하는가?"""    
    
    main04_01 = StoryNode()
    main04_01.story = """해피엔딩"""
    
    main04_01_Ending = EndingNode("BAD ENDING")
    main04_01_Ending.endingTitle = """속았다"""
    main04_01_Ending.story = """배드앤딩이다 이자식아"""
    
    main04_02 = StoryNode()
    main04_02.story = """배드엔딩"""
    
    main04_02_Ending = EndingNode("HAPPY ENDING")
    main04_02_Ending.endingTitle = """오잉?"""
    main04_02_Ending.story = """해피앤딩이다 이자식아"""
    
    main04_03 = StoryNode()
    main04_03.story = """???"""
    
    main04_03_Ending = EndingNode("HIDDEN ENDING")
    main04_03_Ending.endingTitle = """???"""
    main04_03_Ending.story = """오류오류오류오류오류"""
    
    title.addSelection(main01)
    
    main01.addSelection(main01_01)
    main01.addSelection(main01_02)
    
    main01_01.addSelection(main02)
    main01_02.addSelection(main01_02_Ending)
    
    main02.addSelection(main02_01)
    main02.addSelection(main02_02)
    
    main02_01.addSelection(main02_01_Ending)
    main02_02.addSelection(main03)
    
    main03.addSelection(main03_01)
    main03.addSelection(main03_02)
    
    main03_01.addSelection(main04)
    main03_02.addSelection(main03_02_Ending)
    
    main04.addSelection(main04_01)
    main04.addSelection(main04_02)
    main04.addSelection(main04_03)
    
    main04_01.addSelection(main04_01_Ending)
    main04_02.addSelection(main04_02_Ending)
    main04_03.addSelection(main04_03_Ending)
    
    storyManager = StoryExcutor(title, main01)
    while not storyManager.isEnd():
        storyManager.execute()