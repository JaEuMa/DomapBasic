import json
import sys
import os.path
import time as ti
import pandas

def checkFile():
    #if there is no dile abaliable create a file and write the basic json stuff in it
    if not os.path.isfile('domapBasicData.txt'):
        print ("File does not exist -> gets created")
        f = open("domapBasicData.txt", "w")
        f.write('{"tasks": []}')
        f.close()

def getFileJson():
        
    #open the file again and throw in the Json data
    file = open('domapBasicData.txt', 'r')
    stringcontent = file.read()
    file.close()

    #load json
    jsoncontent = json.loads(stringcontent)

    return jsoncontent

    topics = {'tudublin', 'shopping', 'general'}

def createtask():

    tags = {'tudublin', 'shopping', 'general'}

    jsoncontent = getFileJson()

    data = {'task': {}}

    data['id'] = 0

    data['complete'] = 0

    data['createtime'] = str(ti.ctime())

    data['timearr'] = []

    title = input("geben sie einen titel ein \n")
    if title == '':
        title = 'empty'
    data['title'] = title

    prio = input("geben sie eine prio ein [0-9]\n")
    if prio == '':
        prio = 0
    data['priority'] = prio

    time = input("geben sie eine zeit ein [min]\n")
    if time == '':
        time = 'empty'
    data['time'] = time

    dead = input("geben sie eine deadline ein [days]\n")
    if dead == '':
        dead = 'empty'
    data['deadline'] = dead

    soft = input("geben sie eine softlne ein [days]\n")
    if soft == '':
        soft = 'empty'
    data['softline'] = soft

    note = input("geben sie eine notiz ein\n")
    if note == '':
        note = 'empty'
    data['note'] = note

    print("Geben sie tags ein. Zur verfuegung stehen", tags)
    tag = input('')
    if tag == '':
        tags = []
    if tag in tags:
        data['note'] = tags.append(tag)
    else:
        print('not in tags list')
        tag = []

    jsoncontent['tasks'].append(data)
    #open the file again and throw in the Json data
    file = open('domapBasicData.txt', 'w')
    json.dump(jsoncontent, file, indent=4)
    file.close()

def showtasks():
    jsoncontent = getFileJson()

    for content in jsoncontent['tasks']:
        print(content['title'])

def deletetask():
    jsoncontent = getFileJson()
    i = 0
    for content in jsoncontent['tasks']:
        print(i, content['title'])
        i =+ 1

    popindex = input("which task should be deleted?")
    jsoncontent['tasks'].pop(int(popindex))

    #open the file again and throw in the Json data
    file = open('domapBasicData.txt', 'w')
    json.dump(jsoncontent, file, indent=4)
    file.close()

#start console program
print("-----------------------------------------------------------------------------------------------------\n")
print("                                          Welcome to DomapBasic                                        ")
print("                                          ...type help for help                                      \n")
print("-----------------------------------------------------------------------------------------------------\n")

#first check if there is a json text file
checkFile()

while True:
    inp = input(">>>  ")
    if inp == 'create':
        createtask()
    if inp == 'show':
        showtasks()
    if inp == 'update':
        print("Not Yet avaliable")
    if inp == 'delete':
        deletetask()
    if inp == 'daily':
        print("Not Yet avaliable")
    if inp == 'help':
        print("-----------------------------------------------------------------------------------------------------\n")
        print("                                          DomapBasic Help                                              ")
        print("create       create a new task")
        print("show         show all tasks")
        print("*not yet avalable        update       update properties of a task")
        print("delete       delete a task")
        print("*not yet avaliable       daily        show a daily brief with close deadlines and current softlines")
        print("-----------------------------------------------------------------------------------------------------\n")
    if inp == 'end':
        print("------------------------------------thank you for using Domap-----------------------------------------\n")
        sys.exit() 
    