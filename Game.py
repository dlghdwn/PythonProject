from Story import * #스토리 클래스를 전부 가져온다

if(__name__ == "__main__"):
    #시작
    title = TitleNode()
    title.title = """우당당탕 크리스마스 소동"""
    title.story = (
        "착한 어린이들이 모두 잠든 12월 24일 밤. \n"
        "산타 할아버지는 어린이들에게 선물을 배달하기 위해 선물 주머니를 확인했어요. \n"
        "이럴 수가! 선물 주머니가 찢어져 선물들이 이리저리 흩어져 버렸지 뭐예요? \n"
        "어린이들이 깨어나기 전까지 이 일을 해결하려면 소원을 들어주는 별똥별을 찾아야 해요. \n"
        "산타 할아버지는 무사히 사건을 해결할 수 있을까요?"
    )
    
    
    #선택지 1
    main01 = SelectionNode()
    main01.story = """1. 어린이들의 선물이 사라져 모두 선물을 못 받게 생겼어! 어떡하지?"""
    
    main01_01 = StoryNode()
    main01_01.story = """아침 전까지 별똥별을 찾아 선물들을 되돌려놔야겠어!"""
    
    main01_02 = StoryNode()
    main01_02.story = """에잇! 이게 내 책임은 아니지 않나? 이렇게 된 김에 휴가나 떠나야지!"""

    #선택지2
    main02 = SelectionNode()
    main02.story = ( 
        "2.  산타 할아버지는 루돌프와 함께 별똥별을 찾기 시작했습니다. \n"    
        "    1시간이나 달렸지만 별똥별은 보이지 않는군요."
    )
    
    main02_01 = StoryNode()
    main02_01.story = """내가 놓친게 분명히 있을거야! 주변을 좀 더 돌아보자"""

    main02_02 = StoryNode()
    main02_02.story = """이 근처에는 없는 거 같다. 무언가 반짝이는 산으로 이동하자"""
    
    #선택지3
    main03 = SelectionNode()
    main03.story = (
        "3.   산타 할아버지는 산을 향해 출발했어요. \n"
        "     반짝이는 무언가를 향해 산을 오르려던 그 때!\n"
        "     산 입구에 쓰러져있는 한 청년을 발견했어요."  
    )
    
    main03_01 = StoryNode()
    main03_01.story = """산 근처 오두막에 청년을 두고 정상을 향해 간다. """
    
    main03_02 = StoryNode()
    main03_02.story = """마을에 청년을 데려다 주고 정상에 오르는 것을 포기한다."""

    #선택지4
    main04 = SelectionNode()
    main04.story = ( 
        "4.  깨어난 청년이 알려준 이야기로 산 위에 반짝이는 것은 \n"
        "    별똥별이 아니라 아주 큰 트리라는 것을 알게되었어요.\n"
        "    산타할아버지는 청년이 별똥별을 보았다고 말해준 마을로 이동했어요.\n"
        "    이런 마을 입구에서 갈림길이 나왔네요... 어디로 가야 할까요?"
    )
    
    main04_01 = StoryNode()
    main04_01.story = (
        "정보를 얻을려면 사람이 많은 곳으로 가야지\n"
        "     마을 광장으로 간다."
    )

    
    main04_02 = StoryNode()
    main04_02.story = (
        "내 정체를 들어내면 안되니 사람이 적은 곳으로 가야지\n"
        "     인적이 드문 마을 근처 호수로 간다."
    )
    
    #선택지5
    main05 = SelectionNode()
    main05.story = ( 
        "5.  마을 근처 호수에 도착하자 물 속에 있는 별똥별을 발견했습니다 \n"
        "    그런데... 이를 어쩌죠? 먼저 별똥별을 가져가는 사람이 있을 줄이야! \n"
        "    별똥별을 주운 사람은 아직 저것이 별똥별인지 모르는 것 같군요"
    )
    
    main05_01 = StoryNode()
    main05_01.story = """별똥별의 정체를 숨기며 달라고 부탁한다.""" 
    
    main05_02 = StoryNode()
    main05_02.story = """별똥별의 정체를 밝히고 달라고 부탁한다."""
    
    #선택지6
    main06 = SelectionNode()
    main06.story = ( 
        "6.  별똥별을 이용해 선물을 돌려놓으려 했지만 아무 일도 일어나지 않았어요.  \n"
        "    당황해하던 그때, 별똥별에서 목소리가 들려오기 시작했어요.\n"
        "    산타 할아버지... 저는 멋진 트리 위의 별이 되고싶어요! 제 소원을 들어주실 수 있나요?"
    )

    main06_01 = StoryNode()
    main06_01.story = """별똥별의 소원을 들어준다."""

    main06_02 = StoryNode()
    main06_02.story = """별똥별의 소원을 들어주지 않는다."""
  
    #선택지7
    main07 = SelectionNode()
    main07.story = ( 
        "7.  소원을 들어주자 별똥별이 힘차게 반짝기 시작했어요. \n"
        "    이제 선물을 원래대로 돌릴 수 있을 것 같아요! \n"
        "    하지만 무언가 다르게 사용할 수도 있을 것 같은데요?"
    )

    main07_01 = StoryNode()
    main07_01.story = """별똥별의 힘을 이용해 선물을 원래대로 되돌린다."""
 

    main07_02 = StoryNode()
    main07_02.story = """별똥별의 힘을 이용해 ??을 확인한다."""
    
    
    # 엔딩 모음
    # BAD ENDING
    bad_NoSanta_Ending = EndingNode("BAD ENDING")
    bad_NoSanta_Ending.endingTitle = """산타는 없다"""
    bad_NoSanta_Ending.story = (
        "드디어 12월25일 아침! \n"
        "어린이들은 두근거리는 마음으로 선물을 확인했는데... \n"    
        "선물이 없잖아?!?! "
    )
    
    bad_Tree_Ending = EndingNode("BAD ENDING")
    bad_Tree_Ending.endingTitle = """반짝이는 트리"""
    bad_Tree_Ending.story = (
        "청년을 오두막에 두고 서둘러 산 정상에 올라간 산타할아버지! \n"
        "하지만 산 정상에 있는 것은 별똥별이 아닌 반짝이는 트리였네요... "
    )
    
    bad_Oops_Ending = EndingNode("BAD ENDING")
    bad_Oops_Ending.endingTitle = """정체를 들킨 산타"""
    bad_Oops_Ending.story = (
        "정보를 얻기 위해 마을 광장으로 간 산타 할아버지 \n"
        "하지만 너무 방심했던 것일까요? 정체를 들켜버렸어요!\n"
        "수많은 인파를 헤쳐나오긴 쉽지 않아 보이네요... "
    )
    
    bad_SadStar_Ending = EndingNode("BAD ENDING")
    bad_SadStar_Ending.endingTitle = """깨져버린 별똥별"""
    bad_SadStar_Ending.story = (
        "소원을 들어주지 않자 별똥별은 아주 슬프게 흐느끼기 시작했어요. \n"
        "그러다 그만 산산조각이 나며 깨져버렸답니다."
    )
    
    #HAPPY ENDING
    happy_Ending = EndingNode("HAPPY ENDING")
    happy_Ending.endingTitle = """되돌린 선물, 어린이들의 미소"""
    happy_Ending.story = (
       "드디어 12월25일 아침! \n"
        "어린이들은 두근거리는 마음으로 선물을 확인했는데... \n" 
        "세상에! 이건 내가 너무 가지고 싶었던 선물이잖아!  \n" 
        "감사합니다 산타 할아버지! "    
    )
    
    #TRUE ENDING
    true_Ending = EndingNode("TRUE ENDING")
    true_Ending.endingTitle = """한 어린이의 꿈"""
    true_Ending.story = (
        "드디어 12월25일 아침! \n"
        "한 어린이가 잠에서 깨 부모님께 달려갑니다. \n" 
        "그리곤 엄청 흥분된 목소리로 말하기 시작해요. \n"
        "있잖아, 나 꿈 속에서 산타였다? "    
    )
    
    #HIDDEN ENDING
    hidden_Ending = EndingNode("HIDDEN ENDING")
    hidden_Ending.endingTitle = """새로운 인연"""
    hidden_Ending.story = (
        "어라? 저기 작은 소녀는 누구지? 성냥팔이 소녀를 발견한 산타할아버지! \n"
        "산타할아버지는 소녀의 사연을 듣곤 자신과 같이 살자고 제안했어요. \n" 
        "성냥팔이 소녀에게는 최고의 크리스마스가 되었답니다. "    
    )
    
    #선택지 연결
    title.addSelection(main01)
    
    main01.addSelection(main01_01)
    main01.addSelection(main01_02)
    
    main01_01.addSelection(main02)
    main01_02.addSelection(bad_NoSanta_Ending)
    
    main02.addSelection(main02_01)
    main02.addSelection(main02_02)
    
    main02_01.addSelection(hidden_Ending)
    main02_02.addSelection(main03)
    
    main03.addSelection(main03_01)
    main03.addSelection(main03_02)
    
    main03_01.addSelection(bad_Tree_Ending)
    main03_02.addSelection(main04)
    
    main04.addSelection(main04_01)
    main04.addSelection(main04_02)
    
    main04_01.addSelection(bad_Oops_Ending)
    main04_02.addSelection(main05)
 
    main05.addSelection(main05_01)
    main05.addSelection(main05_02)
    
    main05_01.addSelection(main06)
    main05_02.addSelection(main06)
    
    main06.addSelection(main06_01)
    main06.addSelection(main06_02)
    
    main06_01.addSelection(main07)
    main06_02.addSelection(bad_SadStar_Ending)
    
    main07.addSelection(main07_01)
    main07.addSelection(main07_02)
    
    main07_01.addSelection(happy_Ending)
    main07_02.addSelection(true_Ending)
 
    storyManager = StoryExcutor(title, main01)
    while not storyManager.isEnd():
        storyManager.execute()