try:
    from tkinter import *
except:
    from Tkinter import *

qd_q={1:'What is the definite integral of x [from 0 to 7]?',
      4:'Solve ΣnCi [0,n] generally.',
      2:'In a parabola y^2 = 4ax , if t is the parameter , what is the slope of the tangent at any general point?',
      3:'In how many ways can the alphabets in the word GOOGLE be arranged so that all the vowels occur together?',
      5:'How many subsets will the power set of the union of two sets(4,5 elements each and none in common) have?',
      6:'What is the derivative of [x] ([i] represents the greates integer function of  i)?',
      9:'What is the last non zero digit of 444! ?',
      8:'How many diagonals are possible in an n sided convex polygon?',
      7:'In x^3=1 what is the relation between the roots (other than 1)?',
      10:'This question is a bit different....... \n A long time ago in a lab far far away,\n a scientist placed 1 bacterium cell in a jar \n which doubled every minute. \nThe jar became full to the brim in 1 hour.\n When was the glass half full/empty\n(depending upon your psychological bend)?\n Answer in minutes after the beacterium was placed'}
qd_a={1:'2',4:'3',7:'1',3:'1',5:'2',6:'4',9:'3',8:'3',2:'3',10:'59'}
qd_o={1:['73','24.5','23.5','7'],4:['2^(n+1)','2^(n-1)','2^(n)','2^(2n)'],
      2:['2/t','t/2','1/t','t'],3:['36','12','3','48'],5:['2^1024','2^512','2^2048','None of these'],
      6:['[x]^2','[x]^-1','sgn(x)','Not possible'],9:['6','7','8','2'],
      8:['nC2-n','n(n-3)/2','Both 1 and 2','None of these'],
      7:['Squares of each other','Cubes of each other','No specific relation','Cannot be determined'],10:['','','','']}


global score,alph_list
score={}
alph_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def final_page():
    global score
    canvas.destroy()
    create_canvas()
    for r in score:
        Label(canvas,text=r+":"+str(score[r])).pack()
    winner=''
    for l in score:
        if score[l]==max(score.values()):
            winner+=l+','
            
    Label(canvas,text=winner+" is/are the winner(s)!!").pack()


def ans_check(i):
    global ans,corr_ans,score,ans_text
    act_ans=ans.get()
    team=act_ans[0]
    act_ans=act_ans[1:]
    corr_ans = qd_a[i]
    if act_ans==corr_ans and i!=10:
        score[team]+=i
        canvas.destroy()
        create_canvas()
        question(i+1)
        ans.delete(0,END)
        ans.insert(0,'')
    elif act_ans==corr_ans and i==10 :
        score[team]+=i
        final_page()


def create_canvas():
    global canvas
    canvas=Canvas(root,width=400,height=400)
    canvas.pack()


def accept_teams():
    global team_count
    team_count=int(teams.get())
    for i in range(1,team_count+1):
        score[alph_list[i-1]]=0
    canvas.destroy()
    create_canvas()
    question(1)


def ask_team():
    global lab,teams,sub
    Label(canvas,text="The questions will be of increasing difficulty \nand if the answer is right the team will be awarded the marks \ncorresponding to the question number.").grid(row=1,column=1)
    lab=Label(canvas,text="How many teams: ").grid(row=2,column=1,columnspan=4)
    teams=Entry(canvas,width=50)
    teams.grid(row=3,column=1)
    sub=Button(canvas,text="SUBMIT",command=lambda: accept_teams()).grid(row=4,column=1)


def question(i):
    global opText1,opText2,opText3,opText4,ans
    q1=Label(canvas,width=100,text=str(i)+". "+qd_q[i],font=(None,20)).grid(row=1,column=1,columnspan=5)
    ans=Entry(canvas,width=50)
    ans.grid(row=6,column=1,columnspan=5)
    if i!=10:
        opText1=(qd_o[i][0])
        opText2=(qd_o[i][1])
        opText3=(qd_o[i][2])
        opText4=(qd_o[i][3])
        op1=Label(canvas,text="1.  "+opText1).grid(row=2,column=3)
        op2=Label(canvas,text="2.  "+opText2).grid(row=3,column=3)
        op3=Label(canvas,text="3.  "+opText3).grid(row=4,column=3)
        op4=Label(canvas,text="4.  "+opText4).grid(row=5,column=3)
    b=Button(canvas,width=10,text="SUBMIT",command=lambda: ans_check(i)).grid(row=7,column=3)


root=Tk()
canvas=Canvas(root,width=400,height=400)
canvas.pack()


ask_team()
root.mainloop()
