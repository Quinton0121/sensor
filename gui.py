import tkinter
import tkinter.ttk
import datetime
import requests

#class a3g:
#    def __init__(self):        
#        self.tk = tkinter.Tk()
#        self.v = tkinter.StringVar()
#        self.tk.geometry('625x335')
#        self.temp = tkinter.Radiobutton(self.tk, text="Temperature", value="temperature",variable=self.v)
#        self.pres = tkinter.Radiobutton(self.tk, text="Pressure", value="pressure",variable=self.v)
#        self.addBtn = tkinter.Button(self.tk, text = "Add",     width = 15, command = lambda: self.opende(0))
#        self.delBtn = tkinter.Button(self.tk, text = "Delete",  width = 15, command = self.delitem)
#        self.updBtn = tkinter.Button(self.tk, text = "Update",  width = 15, command = lambda: self.opende(1))
#        self.getBtn = tkinter.Button(self.tk, text = "Get",     width = 15, command = lambda: self.opende(2))
#        self.allBtn = tkinter.Button(self.tk, text = "Get All", width = 15, command = self.getall)
#        self.temp.place(x =  10, y = 250)
#        self.pres.place(x =  150, y = 250)
#        self.addBtn.place(x =  10, y = 300)
#        self.delBtn.place(x = 130, y = 300)
#        self.updBtn.place(x = 250, y = 300)
#        self.getBtn.place(x = 370, y = 300)
#        self.allBtn.place(x = 490, y = 300)
#        self.treeview = tkinter.ttk.Treeview(self.tk, columns = ("seq", "mod", "dte", "sta", "lvl", "avl", "hvl"))
#        self.treeview["show"] = "headings"
#        self.treeview.column("seq", width=69, anchor="center")
#        self.treeview.heading("seq", text="Sequence")
#        self.treeview.column("mod", width=89, anchor="center")
#        self.treeview.heading("mod", text="Model")
#        self.treeview.column("dte", width=109, anchor="center")
#        self.treeview.heading("dte", text="Date")
#        self.treeview.column("sta", width=89, anchor="center")
#        self.treeview.heading("sta", text="Status")
#        self.treeview.column("lvl", width=79, anchor="center")
#        self.treeview.heading("lvl", text="Low")
#        self.treeview.column("avl", width=79, anchor="center")
#        self.treeview.heading("avl", text="Average")
#        self.treeview.column("hvl", width=79, anchor="center")
#        self.treeview.heading("hvl", text="High")
#        self.treeview.place(x =  10, y = 10)

#    def callbackFunc(self, type, values):
#        if type == 1:
#            # Update
#            # Index start with 0 not 1, so -= 1
#            values[0] = int(values[0]) - 1


#            # FIXME: connect to database to update
#            requests.put("http://127.0.0.1:5000/"+self.v.get() + "/"+str(values[0]), data={"key1": "value",
#                                              "key2": "value",
#                                              "key3": "value",
#                                              "key4": "value",
#                                              "key5": "value",
#                                              "key6": "value",
#                                              "key7": "value"})

#            self.treeview.delete(self.treeview.get_children("")[values[0]])
#            # 7 items in values: first is sequence
#            self.treeview.insert("", values[0], values = values)
#        elif type == 2:
#            # Get
#            index = int(values[0])
#            self.delall()

#            # FIXME: connect to database to get
#            result = requests.get("http://127.0.0.1:5000/" +self.v.get() + "/"+ values[0]).json()
#            self.treeview.insert("", "end", values = [result["key1"], result["key2"], result["key3"], result["key4"], result["key5"], result["key6"], result["key7"]])

#        else:
#            # Add new item

#            # [x, *values] usage:
#            # a = ["a", "b", "c"]
#            # [1, *a] => [1, "a", "b", "c"]
#            #self.treeview.insert("", "end", values = [len(self.treeview.get_children("")) + 1, *values]) ####need to fixed the hard-coding id

#            # FIXME: connect to database to add
#            print(self.v.get())
#            requests.post("http://127.0.0.1:5000/"+self.v.get() + "/add", data={"sensor_name": values[0],
#                                              "date": values[1],
#                                              "lowest_temp": values[3],
#                                              "avg_temp": values[4],
#                                              "highest_temp": values[5],
#                                              "status": values[2]})


#        self.updateall()
        
#    def opende(self, type):
#        self.dev = de(type, self.callbackFunc)
#        self.updateall()
                    
#    def delitem(self):
#        # FIXME: connect to database to delete
#        # HTTP Delete things here.
#        #print(self.treeview.item(self.treeview.focus())["values"][0])
#        id = self.treeview.item(self.treeview.focus())["values"][0]
#        self.treeview.delete(self.treeview.focus())
#        self.updateall()
#        requests.delete("http://127.0.0.1:5000/"+self.v.get() + "/"+str(id))
                    
#    def delall(self):
#        for i in self.treeview.get_children(""):
#            self.treeview.delete(i)

#    def updateall(self):
#        idx = 1
#        l = self.treeview.get_children("")
#        for i in l:
#            v = self.treeview.item(i)["values"]
#            self.treeview.item(i, values=(idx, v[1], v[2], v[3], v[4], v[5], v[6]))
#            idx += 1
                    
#    def getall(self):
#        # Get all here.
#        # FIXME: connect to database to getAll
#        #self.treeview.insert("", "end", values = [len(self.treeview.get_children("")) + 1, "S", datetime.datetime.now(), "OK", "1", "2", "3"])
#        result = requests.get("http://127.0.0.1:5000/"+self.v.get() + "/").json()
#        for res in result:
#            self.treeview.insert("", "end", values = [res["seq_num"], res["sensor_name"], res["date"], res["status"], res["lowest_temp"], res["avg_temp"], res["highest_temp"]])


#class de:
#    def __init__(self, type, callbackArgs):
#        self.tk = tkinter.Tk() 
#        self.tk.geometry('270x335')
#        self.callback1 = callbackArgs
#        self.cfmBtn = tkinter.Button(self.tk, text = "OK", width = 15, command = self.send)
#        self.cfmBtn.place(x =  10, y = 300)
#        self.clsBtn = tkinter.Button(self.tk, text = "Close", width = 15, command = self.tk.destroy)
#        self.clsBtn.place(x =  150, y = 300)
#        self.type = type
#        if type == 2:
#            self.seqLbl = tkinter.Label(self.tk, text = "Sequence", width = 15)
#            self.seqLbl.place(x =  10, y = 10)
#            self.seqEty = tkinter.Entry(self.tk, width = 23)
#            self.seqEty.place(x = 110, y = 10)
#        else:
#            self.modLbl = tkinter.Label(self.tk, text = "Model", width = 15)
#            self.modLbl.place(x =  10, y =  10)
#            self.modEty = tkinter.Entry(self.tk, width = 23)
#            self.modEty.place(x = 110, y =  10)
#            self.dteLbl = tkinter.Label(self.tk, text = "Date", width = 15)
#            self.dteLbl.place(x =  10, y =  40)
#            self.dteEty = tkinter.Entry(self.tk, width = 23)
#            self.dteEty.place(x = 110, y =  40)
#            self.staLbl = tkinter.Label(self.tk, text = "Status", width = 15)
#            self.staLbl.place(x =  10, y =  70)
#            self.staEty = tkinter.Entry(self.tk, width = 23)
#            self.staEty.place(x = 110, y =  70)
#            self.lvlLbl = tkinter.Label(self.tk, text = "Low Value", width = 15)
#            self.lvlLbl.place(x =  10, y = 100)
#            self.lvlEty = tkinter.Entry(self.tk, width = 23)
#            self.lvlEty.place(x = 110, y = 100)
#            self.avlLbl = tkinter.Label(self.tk, text = "Average Value", width = 15)
#            self.avlLbl.place(x =  10, y = 130)
#            self.avlEty = tkinter.Entry(self.tk, width = 23)
#            self.avlEty.place(x = 110, y = 130)
#            self.hvlLbl = tkinter.Label(self.tk, text = "High Value", width = 15)
#            self.hvlLbl.place(x =  10, y = 160)
#            self.hvlEty = tkinter.Entry(self.tk, width = 23)
#            self.hvlEty.place(x = 110, y = 160)
#        if type == 1:
#            self.seqLbl = tkinter.Label(self.tk, text = "Sequence", width = 15)
#            self.seqLbl.place(x =  10, y = 190)
#            self.seqEty = tkinter.Entry(self.tk, width = 23)
#            self.seqEty.place(x = 110, y = 190)

#    def send(self):
#        # Backend things here
#        if self.type == 2:
#            # Get by sequence
#            self.callback1(self.type, [self.seqEty.get()])
#            pass
#        elif self.type == 1:
#            # Update
#            self.callback1(self.type, [self.seqEty.get(), self.modEty.get(), self.dteEty.get(), self.staEty.get(), self.lvlEty.get(), self.avlEty.get(), self.hvlEty.get()])
#            pass
#        else:
#            # Add
#            self.callback1(self.type, [self.modEty.get(), self.dteEty.get(), self.staEty.get(), self.lvlEty.get(), self.avlEty.get(), self.hvlEty.get()])
#            pass
#        self.tk.destroy()

#gui = a3g()
#gui.tk.mainloop()

#class a3g:
#    def __init__(self):        
#            self.tk = tkinter.Tk()
#            self.v = tkinter.StringVar()
#            self.tk.geometry('625x335')
#            self.temp = tkinter.Radiobutton(self.tk, text="Temperature", value="temperature",variable=self.v)
#            self.pres = tkinter.Radiobutton(self.tk, text="Pressure", value="pressure",variable=self.v)
#            self.addBtn = tkinter.Button(self.tk, text = "Add",     width = 15, command = self.opende())
            
#            self.temp.place(x =  10, y = 250)
#            self.pres.place(x =  150, y = 250)
#            self.addBtn.place(x =  10, y = 300)
            
#            self.treeview = tkinter.ttk.Treeview(self.tk, columns = ("seq", "mod", "dte", "sta", "lvl", "avl", "hvl"))
#            self.treeview["show"] = "headings"
#            self.treeview.column("seq", width=69, anchor="center")
#            self.treeview.heading("seq", text="Sequence")
#            self.treeview.column("mod", width=89, anchor="center")
#            self.treeview.heading("mod", text="Model")
#            self.treeview.column("dte", width=109, anchor="center")
#            self.treeview.heading("dte", text="Date")
#            self.treeview.column("sta", width=89, anchor="center")
#            self.treeview.heading("sta", text="Status")
#            self.treeview.column("lvl", width=79, anchor="center")
#            self.treeview.heading("lvl", text="Low")
#            self.treeview.column("avl", width=79, anchor="center")
#            self.treeview.heading("avl", text="Average")
#            self.treeview.column("hvl", width=79, anchor="center")
#            self.treeview.heading("hvl", text="High")
#            self.treeview.place(x =  10, y = 10)

#    def callbackFunc(self,values):
#        a=self.v.get()
#        print("http://127.0.0.1:5000/"+ a+ "/add")
#        requests.post("http://127.0.0.1:5000/temperature/add", data={"sensor_name": values[0],
#                                              "date": values[1],
#                                              "lowest_temp": values[3],
#                                              "avg_temp": values[4],
#                                              "highest_temp": values[5],
#                                              "status": values[2]})
    
#    def opende(self):
#            De(self.callbackFunc)
    
class De:
    def __init__(self):
        self.tk = tkinter.Tk() 
        self.tk.geometry('270x335')
#        self.callback1 = callbackArgs
        self.cfmBtn = tkinter.Button(self.tk, text = "OK", width = 15, command = self.send)
        self.cfmBtn.place(x =  10, y = 300)
        self.clsBtn = tkinter.Button(self.tk, text = "Close", width = 15, command = self.tk.destroy)
        self.clsBtn.place(x =  150, y = 300)
        self.type = type


        self.modLbl = tkinter.Label(self.tk, text = "Model", width = 15)
        self.modLbl.place(x =  10, y =  10)
        self.modEty = tkinter.Entry(self.tk, width = 23)
        self.modEty.place(x = 110, y =  10)
        self.dteLbl = tkinter.Label(self.tk, text = "Date", width = 15)
        self.dteLbl.place(x =  10, y =  40)
        self.dteEty = tkinter.Entry(self.tk, width = 23)
        self.dteEty.place(x = 110, y =  40)
        self.staLbl = tkinter.Label(self.tk, text = "Status", width = 15)
        self.staLbl.place(x =  10, y =  70)
        self.staEty = tkinter.Entry(self.tk, width = 23)
        self.staEty.place(x = 110, y =  70)
        self.lvlLbl = tkinter.Label(self.tk, text = "Low Value", width = 15)
        self.lvlLbl.place(x =  10, y = 100)
        self.lvlEty = tkinter.Entry(self.tk, width = 23)
        self.lvlEty.place(x = 110, y = 100)
        self.avlLbl = tkinter.Label(self.tk, text = "Average Value", width = 15)
        self.avlLbl.place(x =  10, y = 130)
        self.avlEty = tkinter.Entry(self.tk, width = 23)
        self.avlEty.place(x = 110, y = 130)
        self.hvlLbl = tkinter.Label(self.tk, text = "High Value", width = 15)
        self.hvlLbl.place(x =  10, y = 160)
        self.hvlEty = tkinter.Entry(self.tk, width = 23)
        self.hvlEty.place(x = 110, y = 160)

    def send(self):
            bs={"date":"2018-09-23 19:59:01.873","sensor_name":"af","lowest_temp":1,"avg_temp":2,"highest_temp":3,"status":"GOOD"}
            a=(requests.get("http://127.0.0.1:5000/temperature/6").json())
            print(a)
gui = De()
gui.tk.mainloop()