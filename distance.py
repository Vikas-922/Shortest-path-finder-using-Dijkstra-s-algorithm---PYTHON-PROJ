
from tkinter import *
import math
import time

sleep_time = 0

def update_sleep_time(value):
    global sleep_time
    sleep_time = int(value) / 100  # Convert milliseconds to seconds

class point:
   # sleep_time = sleep_time
    def __init__(self,x,y,name,):
       # self.sleep_time = sleep_time
        self.x=x
        self.y=y
        self.name=name
        self.arrow=None
        self.chd=None
        self.r=12
        self.backtrace=None
        self.wieght=999999
        self.weightDraw=None
        self.neighbour=[]
        self.element= self.draw()

    def setNeighbour(self,nbr):
        self.neighbour=nbr

    def draw(self):
        c=w.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,
                         width=2,fill="green",)
        w.itemconfig(c,outline="green")
        w.create_text(self.x,self.y,text=self.name,fill="white",font=("TkDefaultFont", 12))
        return c

    def chWieghtD(self):
        kk=20
        if self.weightDraw is not None:
            w.delete(self.weightDraw)
        self.weightDraw=w.create_text(self.x,self.y-kk,text=str(self.wieght),fill="#a4ff5f",font=("TkDefaultFont", 14)) #tags="wg"

    def node(self,colr):
        w.itemconfig(self.element,fill=colr)

    def aselect(self,coloor="red"):
        timee=sleep_time
        tclr = w.itemcget(self.element,"fill")
        w.itemconfig(self.element,fill=coloor)
        w.update()
        time.sleep(timee)
        w.itemconfig(self.element,fill=tclr)

    def draw_arrow(self,x2,y2):
        if self.arrow is not None:
            w.delete(self.arrow)

        # Calculate the angle between the center and mouse pointer
        angle = math.atan2(y2 - self.y, x2 - self.x)

        # Calculate the coordinates of the arrow head
        arrow_length = 30
        arrow_x = self.x + arrow_length * math.cos(angle)
        arrow_y = self.y + arrow_length * math.sin(angle)

        # Draw the arrow
        self.arrow = w.create_line(self.x, self.y, arrow_x, arrow_y, fill="red",tags=self.name, arrow=LAST,arrowshape=(10, 15, 7))
        w.tag_raise(self.arrow) # w.tag_lower(self.arrow)
        w.update()
        

def calculate_distance(p1,p2):
    distance =math.floor(math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))
   # print('   Distance ',p1.name,'-',p2.name,': ', distance)
    return distance

def findDistance(a,b):
    #it takes ineger as input
    global points
    distanc =math.floor(math.sqrt((points[a-1].x - points[b-1].x)**2 + (points[a-1].y - points[b-1].y)**2))
    print(a,'-',b,'||',distanc)
    return distanc

def Distance():
    # Get text from the text box and split it by comma
    values = text_box3.get()
    # Convert the split values to integers
    my_array = [int(x.strip()) for x in values.split(",")]
    res=0
    if len(my_array)>1:
        for i in range(len(my_array)-1):
            res+=findDistance(my_array[i],my_array[i+1])
        result_label.config(text="Distance:  " + str(res))
    

def setNeibr(p,arr):
    global points
    for n in arr:
        points[p-1].neighbour.append(points[n-1])

#global sleep_time
#sleep_time=0
root = Tk()
root.title( " PATH FINDERR ")
root.geometry("1300x800")

l1 = Label(root,text="PATH")
l1.pack()
w = Canvas(root, width = 970, height = 700,bg="grey") 
w.place(x=10,y=6)


text_box1_label = Label(root, text="Start Point :")
text_box1_label.place(x=1010,y=50)
text_box1 = Entry(root)
text_box1.place(x=1090,y=50)

text_box2_label = Label(root, text="End Point :")
text_box2_label.place(x=1010,y=80)
text_box2 = Entry(root)
text_box2.place(x=1090,y=80)

slider = Scale(root, from_=1, to=300, orient=HORIZONTAL, label="Delay(100=1sec)",
                  command=update_sleep_time)
#slider.set(10)  # Initial position of the slider
slider.place(x=1100,y=170)

def initaiateDraw():
    w.delete("all")

    global points
    points=[]

    axx=[50, 231, 418, 692, 864, 213, 641, 184, 421, 682, 434, 314, 536, 351, 800, 95, 461, 602, 553, 384, 505, 295, 253, 272, 577, 780, 53, 89, 333, 610, 833]
    ayy=[50, 177, 330, 524, 655, 537, 163, 354, 115, 341, 559, 448, 259, 210, 74, 634, 194, 285, 376, 494, 470, 306, 393, 50, 57, 208, 263, 490, 624, 629, 408]

    current_char="1"
    for i in range(len(axx)):
        new_point = point(axx[i], ayy[i], current_char)
        points.append(new_point)
        current_char = str(int(current_char) + 1)

    setNeibr(1,[2])
    setNeibr(2,[1,8,22,3,14,9,24])
    setNeibr(3,[2,22,12,21,4,19,13,14])
    setNeibr(4,[3,21,5,10,30,19,11])
    setNeibr(5,[4])
    setNeibr(6,[16,8,28,12,11])
    setNeibr(7,[9,15,26,13,10])
    setNeibr(8,[27,6,23,2])
    setNeibr(9,[25,2,7,17])
    setNeibr(10,[31,4,7,18])
    setNeibr(11,[29,4,6,20])
    setNeibr(12,[3,6,20,23])
    setNeibr(13,[3,7,17,18])
    setNeibr(14,[2,3,17])
    setNeibr(15,[7])
    setNeibr(16,[6])
    setNeibr(17,[13,9,14])
    setNeibr(18,[19,10,13])
    setNeibr(19,[3,4,18])
    setNeibr(20,[12,11,21])
    setNeibr(21,[3,20,4])
    setNeibr(22,[3,2,23])
    setNeibr(23,[8,12,22])
    setNeibr(24,[2])
    setNeibr(25,[9])
    setNeibr(26,[7])
    setNeibr(27,[8])
    setNeibr(28,[6])
    setNeibr(29,[11])
    setNeibr(30,[4])
    setNeibr(31,[10])

    
    railp1=[1,2,3,4]
    railp2=[2,3,4,5]
    busp1=[2,8,6,11,11,4,7,7,9,9,2,6,3,3,7]
    busp2=[8,6,16,6,4,10,10,15,7,2,8,12,12,13,13]
    autoop1=[12,20,21,4,20,11,6,3,12,23,8,23,3,2,3,14,14,2,9,17,9,7,13,18,10,18,3,19]
    autoop2=[20,21,4,30,11,29,28,21,23,8,27,22,22,22,14,2,17,24,17,13,25,26,18,10,31,19,19,4]

    for i in range(len(railp1)):    #rail
            linn = w.create_line(points[railp1[i]-1].x,points[railp1[i]-1].y,points[railp2[i]-1].x,points[railp2[i]-1].y,width=4,fill="#303030",dash=(20, 16))
            w.tag_lower(linn)
            
    for i in range(len(busp1)):    #rai
            linn = w.create_line(points[busp1[i]-1].x,points[busp1[i]-1].y,points[busp2[i]-1].x,points[busp2[i]-1].y,width=3,fill="#ff9933",smooth=True)
            w.tag_lower(linn)
    
    for i in range(len(autoop1)):    #rai
            linn = w.create_line(points[autoop1[i]-1].x,points[autoop1[i]-1].y,points[autoop2[i]-1].x,points[autoop2[i]-1].y,width=3,fill="pink",smooth=True)
            w.tag_lower(linn)

points=[]

def update():    

    initaiateDraw()
    
    global startPoint, endPoint,points
   
    startPoint,endPoint=points[0],points[5]
    t1 = str(text_box1.get())
    t2 = str(text_box2.get())
    t1=t1.upper()
    t2=t2.upper()
    for ty in points:
        if t1==ty.name:
            startPoint=ty
        if t2==ty.name:
            endPoint=ty

    tempArr=[]

    startPoint.wieght=0
    startPoint.backtrace=startPoint

    prevNode=startPoint
    oldNode=None
    wieghtTill=0
    visited=[]
    arrForLastMin=[]
    history=[]
    break_outer=False
    err=False

    startPoint.node("#0000ff")
    while (True):
        
        tempArr.clear()
        arrForLastMin.clear()
        if prevNode.name not in visited:
            visited.append(prevNode.name)
        if len(visited)==len(points):
            print('all visited')
            prevNode=endPoint

        for i in range(len(prevNode.neighbour) ):
            #print('visit ',prevNode.name)
            curNode=prevNode.neighbour[i]
            curNode.aselect()
            
            # for changing backtrace of last endPoint
            # checks n times and see is there min weight neighbout around
            if (endPoint.name==prevNode.name):
                disttt = curNode.wieght + calculate_distance(prevNode,curNode)
                arrForLastMin.append(disttt)
            #prevNode.backtrace

            dist = prevNode.wieght + calculate_distance(prevNode,curNode)
            # tempArr.append(dist)

            if dist<curNode.wieght:         #change weight
                curNode.backtrace=prevNode
                curNode.draw_arrow(prevNode.x,prevNode.y)
                curNode.wieght=dist
                tempArr.append(curNode.wieght)  #
                curNode.chWieghtD()
                w.update()
                #time.sleep(0.2)
            else:   #
                tempArr.append(curNode.wieght)  #

        
        #min wieght neighbor is assigned to backtrace of endNode
        if len(visited)==31:
            if prevNode.name != endPoint.name:
                prevNode=endPoint
                continue
            if (endPoint.name==prevNode.name):
                qq = min(arrForLastMin)
                ii = arrForLastMin.index(qq)
                prevNode.backtrace=prevNode.neighbour[ii]
                prevNode.wieght=prevNode.backtrace.wieght+calculate_distance(prevNode.backtrace,prevNode)
                prevNode.draw_arrow(prevNode.backtrace.x,prevNode.backtrace.y)
                prevNode.chWieghtD()
                w.update()
                break

        
        #selecting (PrevNode) smallest wieght node
        #selects node which is not visited
        errrr=0
        while (True):
            zzz=0
            nn=0
            
            ####  LOCKED  SITUATION WHERE SURROUNGIN NODES ARE VISITED
            for k in range(len(prevNode.neighbour)):
                if nn == len(prevNode.neighbour):
                    break
                if (prevNode.neighbour[nn].name in visited):
                    zzz=zzz+1
                    nn=nn+1

            
            if(zzz==len(prevNode.neighbour)):
                zzz=0
            # visited.append(prevNode.name)
                print('locked ',prevNode.name)
                # if prevNode.name=="16":
                #     err=True
                historyList=[]
                for lkm in history:
                    historyList.append(lkm.name)
                print(historyList)
            
                prevNode.node("#800080") 
                prevNode=history.pop()
                prevNode.node("#0000ff")

                break
            #+++++++++++++++++++++++++++++++++++++++++++++

            mn = min(tempArr)
            min_index = tempArr.index(mn)

            #if deadlock occurs for node, below condition is false

                    # ||not be previose node from where we came||                       || not be visited ||
            if (prevNode.neighbour[min_index].name != prevNode.backtrace.name) and (prevNode.neighbour[min_index].name not in visited):
            # oldNode=prevNode
                history.append(prevNode)
                prevNode.node("#800080")   
                prevNode=prevNode.neighbour[min_index]
                prevNode.node("#0000ff")
                
                wieghtTill=mn
                break
            else:
                tempArr[min_index]=999999
        
        if break_outer:
            break

    print(tempArr)
    stack=[]    #to recorrect weightd at end path
    for m in range(len(stack)):
        stack[m+1].wieght=stack[m].weight+calculate_distance(stack[m],stack[m+1])
        stack[m+1].chWieghtD()
        if stack[m+1].name==endPoint.name:
            break

    ####   PATH highlight  DARAWING  @@@@@@@@@
    cNode=endPoint
    while(True):
        ppp = w.create_line(cNode.x,cNode.y,cNode.backtrace.x,cNode.backtrace.y,fill="blue", width=10)
        #w.tag_lower(ppp, prevNode.element)
        w.tag_lower(ppp)
        stack.insert(0,cNode)
        if cNode.backtrace.name==startPoint.name:
            stack.insert(0,startPoint)
            break
        cNode=cNode.backtrace


    #findDistance(2,8)


update_button = Button(root, text="Find Path",command=update, bg="red").place(x=1070,y=110)

text_box3_label = Label(root, text="Calculate Distance between Two Points:",font=("Arial", 10))
text_box3_label.place(x=1010,y=260)
text_box3 = Entry(root)
text_box3.place(x=1010,y=290)
distane_button = Button(root, text="Find Distance",command=Distance, bg="red").place(x=1160,y=285)
result_label = Label(root, text="RESULT AREA",font=("Arial", 12), fg="blue")
result_label.place(x=1070,y=320)

update()
mainloop()