print ('starting')
while True:
    print()
    print()
    print('---------------------------------------------------------------')
    print("|                    WELCOME                                  |")
    print('|           CHOOSE AN OPTION TO PROCEED                       |')
    print("|   1.Create and Print Marksheet                              |")
    print("|   2.Print a Multiword name and print it in abrivivated form |")
    print("|   3.Show any 5 list operations and their working.           |")    
    print("|   4.Show any 5 methods and function based on dictionary     |")
    print("|   5. EXIT                                                   |")
    print('---------------------------------------------------------------')
    choice=int(input("Enter your choice:"))
    if choice==1:
        student = str(input('Enter the Student Name:'))
        Class = str(input('Enter the student class:'))
        sec = str(input('Enter the Section of student:'))
        roll = int(input('Enter the Student Roll Number:'))
        english = int(input('Enter English Marks of student:'))
        maths = int(input('Enter Maths Marks of student:'))
        science = int(input('Enter Science marks of Student:'))
        socialscience = int(input('Enter Social Science Marks of Student:'))
        hindi = int(input('Enter hindi marks of students:'))
        comp = int(input('Enter Computer Science Marks of student:'))
        Total = english+maths+science+socialscience+hindi+comp
        if Total > 600:
            print('Wrong Marks input again', 'ERROR: Marks more than total of 600')
            break
        average = Total/6.0
        print()
        print()
        print('----------------------------------------------------------------')
        print('|                 MONT FORT INTER COLLEGE                      |')
        print('|--------------------------------------------------------------|')
        print('|                 Annual Exam Marksheet                        |')
        print('|--------------------------------------------------------------|')
        print('| Student Name:',student,'Class:',Class, 'Roll Number:', roll,'|')
        print('|           Subject |  Marks Obtained | Out of                 |')      
        print('|        English    | ', english,    '| 100                    |')
        print('|        Hindi      | ',  hindi,     '| 100                    |')
        print('|        Maths      | ',  maths,     '| 100                    |')
        print('|  Computer Science | ',  comp ,     '| 100                    |')
        print('|       Science     | ',  science,   '| 100                    |')
        print('|   Social Science  |',socialscience,'| 100                    |')
        print('---------------------------------------------------------------|')
        print('|     TOTAL:        |', Total, '      | Out of 600             |')
        print('|     Average:      |', average,'%                             |')
        print('---------------------------------------------------------------|')
        if (english<35) or (maths<35) or (science<35) or (comp<35) or (hindi<35) or (socialscience<35):
              print('|      RESULT:      FAIL                                 |')
        else:
              print('|      RESULT:      PASS                                 |')
    elif choice==2:
        str=input("Enter a Student full name:")
        list1=str.split(" ")
        print('The Abriverated form of Name:',list1[0][0],'.',list1[1][0],list1[2])  
    elif choice==3:
        print('1. Printing a LIST')
        list1 = list(input('Enter a Sentence:'))
        print(list1)
        print()
        print('2. Traversing a List:')
        list7 = list(input('Enter a Sentence:'))
        print()
        for i in list7:
            print(i)
        print()
        print('3. Concatenation of LIST:')
        print()
        list1 = list(input('enter some values'))
        list2 = list(input('enter some values'))
        list3 = list1 + list2
        print(list3)
        print()
        print('4. Replicatiopn of LIST')
        print()
        list1 = list(input('Enter some values'))
        multi = int(input('Enter how many times to repeat:'))
        list2 = list1 * multi
        print(list2)
        print()
        print('5. Membership Testing:')
        print()
        sentence = input('Enter a sentence:')
        test = input('word/letter to check:')
        if test in sentence:
            print(test, 'Is present')
        else:
            print(test, 'Is not present')
        print()
    elif choice==4:
        print()
        print('1. clear function:')
        D = {1:'one', 2:'two',3:'three',4:'four'}
        print('before clearing:',D)
        D.clear()
        print('After Clearing:',D)
        print()
        print('2.Get() function:')
        D1 = {'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'wednesday','thu':'thursday'}
        D1.get('wed')
        print(D1.get('fri','Not present'))
        print()
        print('3. items() functions:')
        D = {'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'wednesday','thu':'thursday'}
        D.items()
        print()
        print('4. Keys() function:')
        D = {'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'wednesday','thu':'thursday'}
        D.keys()
        print()
        print('5. values() function:')
        D = {'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'wednesday','thu':'thursday'}
        D.values()
        print()
    elif choice==5:
        break
    else:
        print("Wrong Choice")
