from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    #시작
    title = TitleNode()
    title.title = """우당당탕 크리스마스 소동"""
    title.story = (
        "착한 어린이들이 모두 잠든 12월 24일 밤. \n "
        "   산타 할아버지는 어린이들에게 선물을 배달하기 위해 선물주머니를 확인했어요. \n"
        "   이럴 수가! 선물 주머니가 찢어져 선물들이 이리저리 흩어져 버렸지 뭐예요? \n"
        "   어린이들이 깨어나기 전까지 이 일을 해결하려면 소원을 들어주는 별똥별을 찾아야 해요. \n"
        "   산타 할아버지는 무사히 사건을 해결할 수 있을까요?"
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
        "   그렇나 1시간이나 달렸지만 별똥별은 보이지 않는군요."
    )
    
    main02_01 = StoryNode()
    main02_01 = (
        "이만큼이나 찾았는데 안 나오다니... 이 근처에는 없는 거 같다. \n"
        "   사람이 많은 마을로 이동하자"
    )
    
    main02_02 = StoryNode()
    main02_02 = (
        "내가 놓친게 분명히 있을거야! \n"
        "   주변을 좀 더 돌아보자"
    )
    
    main02_03 = StoryNode()
    main02_03 = (
        "이만큼이나 찾았는데 안 나오다니... 이 근처에는 없는 거 같다. \n"
        "   무언가 반짝이는 산으로 이동하자"
    )
    
    #선택지3
    main03 = SelectionNode()
    main03.story = (
        "3. 산타 할아버지는 산을 향해 출발했어요. \n"
        "   반짝이는 무언가를 향해 산을 오르려던 그 때!\n"
        "   산 입구에 쓰러져있는 사람을 발견했어요."  
    )
    
    main03_01 = StoryNode()
    main03_01 = (
        "저 사람을 도와주면 시간아 촉박할거야... \n"
        "   사람을 무시하고 정상을 향해 간다."
    )

    
    main03_02 = StoryNode()
    main03_02 = (
        "이 날씨에 사람을 두고 갈 순 없어 \n"
        "   쓰러진 사람을 도와준다."
    )
    
    #선택지4
    main04 = SelectionNode()
    main04.story = ( 
        "4. 구해준 사람이 알려준 이야기로 \n"
        "   산 위에 반짝이는 것은 별똥별이 아니라는 것을 깨달은 산타 할아버지! \n "
        "   그가 말해준 마을로 루돌프와 다시 힘차게 달리기 시작했습니다. \n "
        "   이런 갈림길이 나왔네요... 어디로 가야 할까요?"
    )
    
    main04_01 = StoryNode()
    main04_01 = (
        "정보를 얻을려면 사람이 많은 곳으로 가야지\n"
        "   마을 광장으로 간다."
    )

    
    main04_02 = StoryNode()
    main04_02 = (
        "내 정체를 들어내면 안되니 사람이 적은 곳으로 가야지\n"
        "   인적이 드문 마을 근처 호수로 간다."
    )
    
    #선택지5
    main05 = SelectionNode()
    main05.story = ( 
        "5. 마을 근처 호수에 도착하자 물 속에 있는 별똥별을 발견했습니다 \n"
        "   그런데... 이를 어쩌죠? 먼저 별똥별을 가져가는 사람이 있을 줄이야! \n "
        "   별똥별을 주운 사람은 아직 저것이 별똥별인지 모르는 것 같군요   "
    )
    
    main05_01 = StoryNode()
    main05_01 = """별똥별의 정체를 숨기며 달라 부탁한다."""
    
    main05_02 = StoryNode()
    main05_02 = """별똥별의 정체를 밝히고 달라고 부탁한다."""
    
    #선택지6
    main06 = SelectionNode()
    main06.story = ( 
        "6. 별똥별에 대해 사실대로 이야기하자 아픈 자식을 위해 쓰고 싶다는 사람! \n"
        "   그러나 모든 아이들의 행복을 위해 돌려주겠다는데... \n "
        "   이대로 가면 모두 행복해야할 크리스마스에 슬픈사람이 생길 것 같다. "

    )
    
    main06_01 = StoryNode()
    main06_01 = (
        "정보를 얻을려면 사람이 많은 곳으로 가야지\n"
        "   마을 광장으로 간다."
    )

    
    main06_02 = StoryNode()
    main06_02 = (
        "내 정체를 들어내면 안되니 사람이 적은 곳으로 가야지\n"
        "   인적이 드문 마을 근처 호수로 간다."
    )
    
    # 엔딩 모음
    bad_NoSanta_Ending = EndingNode("BAD ENDING")
    bad_NoSanta_Ending.endingTitle = """산타는 없다"""
    bad_NoSanta_Ending.story = (
        "드디어 12월25일 아침! 어린이들은 두근거리는 마음으로 선물을 확인했는데..."    
        "\n선물이 없잖아?!?! "
    )
    
    hidden_Ending = EndingNode("HIDDEN ENDING")
    hidden_Ending.endingTitle = """새로운 인연"""
    hidden_Ending.story = (
        "어라? 저기 작은 소녀는 누구지? 성냥팔이 소녀를 발견한 산타할아버지! \n "
        "   산타할아버지는 소녀의 사연을 듣곤 자신의 집에서 같이 살자고 제안했어요. \n" 
        "   성냥팔이 소녀에게는 최고의 크리스마스가 되었답니다. "    
    )
    
    storyManager = StoryExcutor(title, main01)
    while not storyManager.isEnd():
        storyManager.execute()