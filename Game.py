from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    main01 = StoryNode()
    main01.story = """1. 저기 쓰레기가 땅에 떨어져있다."""
    
    main_01_01 = StoryNode()
    main_01_01.story = """쓰레기를 줍지 않았다. 우우 쓰레기"""
    
    main_01_02 = StoryNode()
    main_01_02.story = """2. 쓰레기를 주웠다. \n앗! 몰래카메라 실험이었다! \n인터뷰에 응할까?"""
    
    main_02_01 = StoryNode()
    main_02_01.story = """인터뷰에 응했으나 말실수로 악플을 받았다..."""
    
    main_02_02 = StoryNode()
    main_02_02.story = """3. 인터뷰에 응하지 않았다. \n마저 가던 길을 간다 \n어느 쪽으로 갈까?"""
    
    main_03_01 = StoryNode()
    main_03_01.story = """4. 오른쪽으로 가니 내가 가려던 마트가 보였다."""
    
    main_03_02 = StoryNode()
    main_03_02.story = """바보 마트는 왼쪽이 아니야"""
    
    main01.addSelection("01. 쓰레기를 줍지 않는다", main_01_01)
    main01.addSelection("02. 쓰레기를 줍는다", main_01_02)
    
    main_01_02.addSelection("01. 인터뷰에 응한다", main_02_01)
    main_01_02.addSelection("02. 인터뷰에 응하지 않는다", main_02_02)
    
    main_02_02.addSelection("01. 오른쪽", main_03_01)
    main_02_02.addSelection("02. 왼쪽", main_03_02)

    storyManager = StoryExcutor(main01)
    while not storyManager.isFinish():
        storyManager.execute()