

if __name__ == '__main__':

    GA_box=[0,1,2,3,4,5,6]
    loss_list=[1,2,3,0,5,5,1]

    ans = list()
    for i in loss_list:
        ans.append(i)
    ANS_Y = min(ans)
    ANS_X = GA_box[ans.index(ANS_Y)]
    print(ANS_X,ANS_Y)

