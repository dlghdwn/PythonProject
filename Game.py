from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    main01 = StoryNode()
    main01.story = """1. 저기 쓰레기가 땅에 떨어져있다."""
    
    main01_01 = StoryNode()
    main01_01.story = """쓰레기를 줍지 않았다. 우우 쓰레기"""
    
    main01_02 = StoryNode()
    main01_02.story = """2. 쓰레기를 주웠다. \n앗! 몰래카메라 실험이었다! \n인터뷰에 응할까?"""
    
    main01_02_01 = StoryNode()
    main01_02_01.story = """인터뷰에 응했으나 말실수로 악플을 받았다..."""
    
    main01_02_02 = StoryNode()
    main01_02_02.story = """인터뷰에 응하지 않았다."""
    
    main01.addSelection("01. 쓰레기를 줍지 않는다", main01_01)
    main01.addSelection("02. 쓰레기를 줍는다", main01_02)
    
    main01_02.addSelection("01. 인터뷰에 응한다", main01_02_01)
    main01_02.addSelection("02. 인터뷰에 응하지 않는다", main01_02_02)
    
    storyManager = StoryExcutor(main01)
    while not storyManager.isFinish():
        storyManager.execute()