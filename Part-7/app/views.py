from django.shortcuts import render

def News_Page(request):
    return render(request,'index.html')

def movies_view(request):
    head_msg = 'Movie Information'
    sub_msg1 = 'RRR ready to relase'
    sub_msg2 = 'Background support reuirred to get chance'
    sub_msg3 = 'Indian cine industry struggling like anything with covid'
    sub_msg4 = 'Biggest benefit of covid for industry:OTT'
    sub_msg5 = 'avi is hero of the movies and'

    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5}

    return render(request,'msp.html',my_dict)


def sports_view(request):
    head_msg = 'sports Information'
    sub_msg1 = 'Athletic Achievements: Highlighting outstanding performances by athletes, such as breaking records, winning championships, or achieving personal bests, can captivate audiences and showcase the pinnacle of human physical prowess'
    sub_msg2 = 'Team Dynamics: Exploring the intricate relationships and dynamics within sports teams offers insights into leadership, cooperation, and the power of collective effort'
    sub_msg3 = 'Impact on Society: Sports often transcend the realm of entertainment, influencing societal norms, values, and even politics'
    sub_msg4 = 'Global Sporting Events: Major international tournaments, such as the Olympics or the FIFA World Cup, bring together nations from around the world, fostering unity, pride, and friendly competition.'
    sub_msg5 = 'Health and Wellness: Participation in sports and physical activities promotes physical fitness, mental well-being, and overall healthand'

    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5}

    return render(request,'msp.html',my_dict)

def politics_view(request):
    head_msg = 'politics Information'
    sub_msg1 = 'Policy Debates: Examining political debates and discussions surrounding key policy issues, such as healthcare, education, immigration, and climate change, provides insight into the priorities and ideologies of different political parties and leaders'
    sub_msg2 = 'Elections and Campaigns: Tracking electoral campaigns, from local elections to presidential races, sheds light on the strategies, messaging, and tactics employed by candidates and political parties to garner support and sway voters.'
    sub_msg3 = 'International Relations: Analyzing diplomatic relations between nations, geopolitical tensions, and global events, such as conflicts, treaties, and summits, offers a glimpse into the complex web of international politics and the pursuit of peace, security, and cooperation on the world stage.'
    sub_msg4 = 'Political Movements: From grassroots activism to social justice movements, political engagement takes various forms and shapes public discourse. Exploring the motivations, strategies, and impacts of political movements provides insights into societal change and the quest for equality, justice, and human rights.'
    sub_msg5 = 'Media and Political Communication: Critically examining the role of media in shaping political narratives, disseminating information, and influencing public opinion helps understand the dynamics of modern politics and the challenges of navigating a rapidly evolving media landscape.'

    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5}

    return render(request,'msp.html',my_dict)
