from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    #시작
    title = TitleNode()
    title.title = """우당당탕 크리스마스 소동"""
    title.story = (
        "착한 어린이들이 모두 잠든 12월 24일 밤. "
        "\n산타 할아버지는 어린이들에게 선물을 배달하기 위해 선물주머니를 확인했어요."
        "\n이럴 수가! 선물 주머니가 찢어져 선물들이 이리저리 흩어져 버렸지 뭐예요?"
        "\n어린이들이 깨어나기 전까지 이 일을 해결하려면 소원을 들어주는 별똥별을 찾아야 해요."
        "\n산타 할아버지는 무사히 사건을 해결할 수 있을까요?"
    )
    
    #선택지 1
    main01 = SelectionNode()
    main01.story = """1. 어린이들의 선물이 사라져 모두 선물을 못 받게 생겼어! 어떡하지?"""
    
    main01_01 = StoryNode()
    main01_01.story = """아침 전까지 별똥별을 찾아 선물들을 되돌려놔야겠어!"""
    
    main01_02 = StoryNode()
    main01_02.story = (
        "에잇! 이게 내 책임은 아니지 않나? \n"
        "   이렇게 된 김에 휴가나 떠나야지!"
    )
    
    #선택지2
    main02 = SelectionNode()
    main02.story = ( 
        "2. 산타 할아버지는 루돌프와 함께 별똥별을 찾기 시작했습니다. \n"    
        "   그렇게 1시간이나 달렸지만 별똥별은 보이지 않는군요."
    )
    
    main02_01 = StoryNode()
    main02_01 = (
        "이만큼이나 찾았는데 안 나오다니... 이 근처에는  없는 거 같다. \n"
        "   근처 마을로 이동하자"
    )
    
    main02_02 = StoryNode()
    main02_02 = (
        "내가 놓친게 분명히 있을거야! \n"
        "   주변을 좀 더 돌아보자"
    )
        
    main02_02_Ending = EndingNode("HIDDEN ENDING")
    main02_02_Ending.endingTitle = """새로운 인연"""
    main02_02_Ending.story = (
        "어라? 저기 작은 소녀는 누구지? 성냥팔이 소녀를 발견한 산타할아버지! \n "
        "   산타할아버지는 소녀의 사연을 듣곤 자신의 집에서 같이 살자고 제안했어요. \n" 
        "   성냥팔이 소녀에게는 최고의 크리스마스가 되었답니다. "    
    )
    
    main02_03 = StoryNode()
    main02_03 = (
        "이만큼이나 찾았는데 안 나오다니... 이 근처에는  없는 거 같다. \n"
        "   근처 산으로 이동하자"
    )
    
    #선택지3
    main03 = SelectionNode()
    main03.story = ( 
        "3. 루돌프가 코를 가리자 저 멀리서 반짝거리는 무언가가 보이네요!"
        "\n산타 할아버지는 그곳으로 출발하기 시작했어요."
        "\n아니! 사람이 쓰러져 있잖아? "
        "\n이 날씨에 이렇게 밖에서 잔다면 분명히 얼어죽고 말거야!"
    )
    
    main03_01 = StoryNode()
    main03_01 = (
        "저게 저 사람의 운명인가 보군... "
        "\n방치하자기엔 마음이 걸리니 내 여분 옷이라도 주고 가지 뭐!"
    )

    
    main03_02 = StoryNode()
    main03_02 = (
        "그래도 사람 살리는 일이 먼저 아닐까?  "
        "\n따뜻하게 만들어 줘야겠어"
    )
    
    #선택지4
    main04 = SelectionNode()
    main04.story = ( 
        "4. 구해준 사람이 눈을 뜨고 알려준 이야기로"
        "\n산 위에 반짝이는 것은 별똥별이 아니라는 것을 깨달은 산타 할아버지! "
        "\n그가 말해준 별똥별의 방향으로 루돌프와 다시 힘차게 달리기 시작했습니다. "
        "\n이 날씨에 이렇게 밖에서 잔다면 분명히 얼어죽고 말거야!"
    )
    
    # 엔딩 모음
    bad_NoSanta_Ending = EndingNode("BAD ENDING")
    bad_NoSanta_Ending.endingTitle = """산타는 없다"""
    bad_NoSanta_Ending.story = (
        "드디어 12월25일 아침! 어린이들은 두근거리는 마음으로 선물을 확인했는데..."    
        "\n선물이 없잖아?!?! "
    )
    
    storyManager = StoryExcutor(title, main01)
    while not storyManager.isEnd():
        storyManager.execute()