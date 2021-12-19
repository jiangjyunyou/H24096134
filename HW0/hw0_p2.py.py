#!/usr/bin/env python
# coding: utf-8

# In[57]:


fp=open('D:/IMDB-Movie-Data.csv','r')#資料開啟與處理。
data=(fp.readlines())
fp.close()
lines = []

#promble 1
#Top-3 movies with the highest ratings in 2016?
for y in range(len(data)):
    lines.append(data[y].split(','))#以'，' 分格資料。
#print(lines)
y2016=[]
r2016=[]
t2016=[]
for i in range(len(lines)):
    if lines[i][5] == '2016':#若year中存在2016,將資料添加進空的list。
        y2016.append(lines[i])
        r2016.append(lines[i][7])
        t2016.append(lines[i][1])
r2016=sorted(r2016,reverse=True)#將資料由大到小排序。
#print(r2016[0],r2016[1],r2016[2])
answer1=[]
answer1.append(t2016[0:3]) 
print(answer1)#列出答案。


# In[56]:


#problem2
#The actor generating the highest average revenue?
actor,actors,r=[],[],[]
new_lines = lines[1:]#刪去第一行之資料(本行為資料之標題)。
#print(new_lines)
for i in range(len(new_lines)):
    a=new_lines[i][4].split('|')#以'|'分隔資料。
    actor.extend(a)#在actor末尾追加a中多個值。
for i in range(len(actor)):
    actor[i] = actor[i].strip()#除去資料中的空格。
actors=list(set(actor))#去除重複之資料。
#print(actors)
na1,na2 = [],[]
for i in range(len(actors)):
    na1.append(actors[i])#在空白list中加入整理好的資料。
#print(na1)
for i in range(len(na1)):
    if na1[i].split('|') not in na2:
        na2.append(na1[i].split('|'))#na1的資料加入na1,並以'|'分隔資料。
#print(na2)
#for x in range(len(new_lines)):
    #if new_lines[x][9] == "":
        #print(new_lines[x])
ny = []
for i in range(len(new_lines)):
    if new_lines[i][9] != "":#將不存在空格之資料匯入空白list。
        ny.append(new_lines[i])
#print(ny)
ra = []
ra = []
dicta = {}
for k in range(len(na1)):
    ar,ra=[],[]
    ra.append(na1[i])#整理後資料匯入新的list。   
    for j in range(len(ny)):
        for i in range(len(ny[j][4])):
            if na1[k] in ny[j][4][i]:
                ar.append(eval(ny[j][9]))
    dicta[ra[k]] = (sum(ar)/len(ar))#將平均值匯入空白之dicta。        
    #print(ar)
    #print(len(ar))
    ra.append(sum(ar)/len(ar))
key = list({y:i for y, i in sorted(dict1.items(),key=lambda item: item[1])})#將資料做排序。
print('The actor generating the highest average revenue is:',key[0],key[1])#列出答案。


# In[55]:


#problem3
#The average rating of Emma Watson’s movies?
a=[]
for i in range(len(lines)):
    if 'Emma Watson' in lines[i][4]:#若Emma Watson存在於actor中,空白list中加入相對應的資料。
        a.append(eval(lines[i][7]))
#print(a)
n=len(a)#list的長度。
average=(sum(a)/n)#list中值的總和除以list的長度。
print(average)#列出平均，即為本題答案。


# In[175]:


#problem4
#Top-3 directors who collaborate with the most actors? 
d,ds=[],[] #lines[idx][3]
a4,a4s=[],[] #lines[idx][4]
dd={}
new_lines = lines[1:]#刪去第一行之資料(本行為資料之標題)
for i in range(len(new_lines)):
    d.append(new_lines[i][3])#將資料中的director加入空白的list
for i in range(len(d)):
    d[i] = d[i].strip()#刪去list中之空格
    ds=list(set(d))#刪去list中重複之資料
#print(ds)
for i in range(len(ds)):
    for j in range(len(new_lines)):
        if ds[0] in new_lines[j][3]:
            a4.append(lines[j][4].split('|'))#以'|'來分格資料
#for i in range(len(new_lines)):
    #print(new_lines[i][4])
for key in d:
    dd[key]=dd.get(key,0)+1
#print(dd)
#print(sorted(dd.items(), key=lambda x:x[1]))
dds=(sorted(dd.items(), key=lambda x:x[1],reverse=True))#Step1.將dict中的value由大到小排序
#Step2.找出David Yates14,M. Night Shyamalan24,Michael Bay16,Paul W.S. Anderson21,Ridley Scott30執導過最多部作品(6,6,6,8)
#優先找出執導過較多作品的導演->較多作品=較可能與更多演員合作
#print(dds)
d0,d1,d2=[],[],[]
for i in range(len(lines)):
    if 'Ridley Scott' in lines[i][3]:
        d0.append(lines[i][4].split('|'))
#print(len(d0))確認需合併的list個數
ds0='Ridley Scott'
x0=d0[0]+d0[1]+d0[2]+d0[3]+d0[4]+d0[5]+d0[6]+d0[7]
x0=list(set(x0))#去除重複之資料
#print(len(x0))
for i in range(len(lines)):
    if 'Paul W.S. Anderson' in lines[i][3]:
        d1.append(lines[i][4].split('|'))
#print(len(d1))確認需合併的list個數
ds1='Paul W.S. Anderson'
x1=d1[0]+d1[1]+d1[2]+d1[3]+d1[4]+d1[5]
x1=list(set(x1))#去除重複之資料
#print(len(x1))
for i in range(len(lines)):
    if 'M. Night Shyamala' in lines[i][3]:
        d2.append(lines[i][4].split('|'))
#print(len(d2))確認需合併的list個數
ds2='M. Night Shyamalan'
x2=d2[0]+d2[1]+d2[2]+d2[3]+d2[4]+d2[5]
x2=list(set(x2))#去除重複之資料
#print(len(x2))
print('Top-3 directors collaborate with the most actors:')
print('1st',ds0,'Number of actors:',len(x0))
print('2nd',ds2,'Number of actors:',len(x2))
print('3rd',ds1,'Number of actors:',len(x1))


# In[53]:


#problem5
#Top-2 actors playing in the most genres of movies?
a5,a5s,a5ss=[],[],[]#lines[idx][4]
g5=[]#lines[idx][2]
aa={}
for i in range(len(new_lines)):
    a5.append(new_lines[i][4].split('|'))#演員資料匯入空白list。
#print(a5)
for j in range(len(a5)):
    a5s+=a5[j]#整理過的資料匯入新的list。
for i in a5s:
    if i == ' ':
        a5s.remove(' ')#移除list中的空格。
#print(a5s)
for key in a5s:
    aa[key]=aa.get(key,0)+1
#print(aa)
aas=(sorted(aa.items(), key=lambda x:x[1],reverse=True))#找出出演次數較多的演員 。
#print(aas)#(14)Denzel Washington 9#(14)Chloe Grace Moretz 11#(14)Michael Fassbender 12。
aa,aa1,aa2=[],[],[]
#for i in range(len(new_lines)):
    #print(new_lines[i][2])
for i in range(len(new_lines)):
    if 'Denzel Washington' in new_lines[i][4]:
        aa.append(lines[i][2].split('|'))
#print(aa)
#print(len(aa))#確認需合併的list個數
genre=aa[0]+aa[1]+aa[2]+aa[3]+aa[4]+aa[5]+aa[6]+aa[7]+aa[8]
genre=list(set(genre))#刪去重複的電影類別。
ac0='Denzel Washington'
#print(genre)
#print(len(genre))#演員出演過的電影類別數量。
for i in range(len(new_lines)):
    if 'Chloe Grace Moretz' in new_lines[i][4]:
        aa1.append(lines[i][2].split('|'))
#print(aa1)
#print(len(aa1))#確認需合併的list個數。
genre1=aa1[0]+aa1[1]+aa1[2]+aa1[3]+aa1[4]+aa1[5]+aa1[6]+aa1[7]+aa1[8]+aa1[9]+aa1[10]
genre1=list(set(genre1))#刪去重複的電影類別。
ac1='Chloe Grace Moretz'
#print(genre1)
#print(len(genre1))#演員出演過的電影類別數量。
for i in range(len(new_lines)):
    if 'Michael Fassbender' in new_lines[i][4]:
        aa2.append(lines[i][2].split('|'))
#print(aa2)
#print(len(aa2))#確認需合併的list個數
genre2=aa2[0]+aa2[1]+aa2[2]+aa2[3]+aa2[4]+aa2[5]+aa2[6]+aa2[7]+aa2[8]+aa2[9]+aa2[10]
genre2=list(set(genre1))#刪去重複的電影類別。
ac2='Michael Fassbender'
#print(len(genre2))#演員出演過的電影類別數量。
ggg=[]
ggg1=[]
for i in range(len(new_lines)):
    ggg.append(new_lines[i][2].split('|'))
#print(ggg)
for i in range(len(ggg)):
    ggg1 += ggg[i]#合併資料
#print(ggg1)
ggg1=list(set(ggg1))
#print(len(ggg1))#共20種電影類別。
print('Top-2 actors playing in the most genres of movies:')#列出答案。
print(ac0,'and',ac1,'and',ac2,'their numbers of genres are:',len(genre2))#列出答案。


# In[52]:


#problem6
#Actors whose movies lead to the largest maximum gap of years
a6,aa6,aaa6=[],[],[]#new_lines[i][4]
yg,y=[],[]#new_lines[i][5]
ans={}
answer=[]
for i in range(len(new_lines)):
    a_6=new_lines[i][4].split('|')#演員資料匯入list。
    a6.extend(a_6)#
#print(a6)
a6=list(set(a6))#去除重複的資料
#print(a6)
for i in a6:
    aa6.append(i.strip(' '))#去除資料中的空格
aa6=list(set(aa6))#去除重複的資料
#print(len(aa6))
for i in range(len(aa6)):
    xx6=[]
    for j in range(len(new_lines)):
        if aa6[i] in new_lines[j][4]:
            xx6.append(eval(new_lines[j][5]))#將演員出演的電影年份匯入空白的list
        aaa6.append(xx6)
#print(aaa6)
for k in aaa6:
    year_gap=max(k)-min(k)#計算年份的最大差距
    yg.append(year_gap)
#print(year_gap)
#print(max(yg))#確認yeargap的最大值=10
ans=dict(zip(aa6,yp))#將兩個list指定為空白dict(ans)中的key and value。
anss=dict(sorted(ans.items(), key=lambda x:x[1],reverse=True))#將dict中的value由大到小排序。
for i in anss.values():
    if i == '10':#若dict中的value值=10,
        answer.append(anss.keys())#則將對應的actor匯入空白的list。
print('Actors whose movies lead to the largest maximum gap of years are:',answer)


# In[174]:


#problem7
#Find all actors who collaborate with Johnny Depp in direct and indirect ways
d7,dd7,ddd7=[],[],[]
a7,aa7,aaaa7,a5_7=[],[],[],[]
a7,xx7=[],[]
for i in range(len(new_lines)):
    d7.append(new_lines[i][4].split('|'))#演員資料匯入list。
for i in range(len(d7)):
    dd7 += d7[i]
dd7=list(set(dd7))#去除重複的資料
for i in dd7:
    ddd7.append(i.strip(' '))#去除演員名字前的空格
ddd7=list(set(ddd7))#去除重複的資料
#print(ddd7)
#print(d7)
for i in range(len(d7)):
    if ' Johnny Depp' in d7[i]:#將資料中包含 Johnny Depp的所有演員匯入空白list
        a7.append(d7[i])
#print(a7)  
for i in range(len(d7)):
    if 'Johnny Depp' in d7[i]:#將資料中包含Johnny Depp的所有演員匯入空白list
        aa7.append(d7[i])
#print(aa7)
aaa7=a7+aa7
#print(aaa7)
for i in range(len(aaa7)):
    aaaa7+=aaa7[i]
#print(aaaa7)
aaaa7=list(set(aaaa7))#去除重複的資料。
#print(aaaa7)#曾與Johnny Depp一起演出的演員。
for i in aaaa7:
    a5_7.append(i.strip(' '))#去除演員前的空格。
a5_7=list(set(a5_7))#去除重複的資料。
#print(a5_7)#與Johnny Depp共同演出過的演員。
#print(d7)
for i in a5_7:
    x7=[]
    for j in range(len(d7)):
        if i in d7[j]:
            x7.append(d7[j])
    xx7.append(x7)     
#print(xx7)#與Johnny Depp共同演出過的演員共同演出的演員。#(direct and indirect)
xx7_1,xx7_2,xx7_3,xx7_4=[],[],[],[]
for i in range(len(xx7)):
    xx7_1 += xx7[i] #合併list中的[i]匯入新的list。
#print(xx7_1)
for i in range(len(xx7_1)):
    xx7_2 += xx7_1[i]
#print(xx7_2)
for i in xx7_2:
    xx7_3.append(i.strip(' '))#去除演員名字前的空格。
xx7_3=list(set(xx7_3))#去除重複的資料。
##print(len(xx7_3))
for i in xx7_3:#重複以上步驟，確認沒有少算到indirect的部分。
    x7_1=[]
    for j in range(len(d7)):
        if i in d7[j]:
            x7_1.append(d7[j])
    xx7_4.append(x7_1)
xx7_5,xx7_6,xx7_7,xx7_8=[],[],[],[]
#print(xx7_4)
for i in range(len(xx7_4)):
    xx7_5 += xx7_4[i] #合併list中的[i]匯入新的list。
#print(xx7_5)
for i in range(len(xx7_5)):
    xx7_6 += xx7_5[i]
#print(xx7_6)
for i in xx7_6:
    xx7_7.append(i.strip(' '))#去除演員名字前的空格。
xx7_7=list(set(xx7_7))#去除重複的資料。
#print(len(xx7_7))#包含direct與indirect的演員
answer7=[]
answer=a5_7+xx7_7
answer=list(set(answer))#去除重複的演員
#print(answer)
print('Find all actors who collaborate with Johnny Depp in direct and indirect ways:')
print('The actors are:',answer)


# In[ ]:





# In[ ]:




