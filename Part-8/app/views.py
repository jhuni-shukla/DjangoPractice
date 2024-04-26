from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def movies_view(request):
    head_msg = 'Movie Information'
    sub_msg1 = 'RRR ready to relase'
    sub_msg2 = 'Background support reuirred to get chance'
    sub_msg3 = 'Indian cine industry struggling like anything with covid'
    sub_msg4 = 'Biggest benefit of covid for industry:OTT'
    sub_msg5 = 'avi is hero of the movies and'
    type='movies'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'type':type}
    return render(request,'index2.html',my_dict)


def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Athletic Achievements'
    sub_msg2 = 'Team Dynamics'
    sub_msg3 = 'Impact on Society'
    sub_msg4 = 'Global Sporting Events'
    sub_msg5 = 'Health and Wellness'
    type='sports'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'type':type}

    return render(request,'index2.html',my_dict)

def politics_view(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'Policy Debates'
    sub_msg2 = 'Elections and Campaigns'
    sub_msg3 = 'International Relations'
    sub_msg4 = 'Political Movements'
    sub_msg5 = 'Media and Political Communication'
    type='politics'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'type':type}

    return render(request,'index2.html',my_dict)
