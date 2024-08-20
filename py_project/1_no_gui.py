import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
DFGI=pd.read_csv('GroceryItems.csv',sep=',')
R=1
while R==1:
    print('============================')
    print('Grocery Items Data Management:')
    print('Menu:')
    print('1.Display all the grocery items details:')
    print('2.Display a perticular column of the dataframe:')
    print('3.Add a new item in the store:')
    print('4.Remove an item from the store:')
    print('5.Graphs:')
    print('6.Exit:')
    print('============================')
    ch=int(input('Choose your sub-option:'))


    #1
    if ch==1:
        print('============================')
        print('Grocery Items:')
        print(DFGI)


    #2   
    elif ch==2:
        print('============================')
        R=3
        while R==3:
            print('Columns present:')
            print('1.Item Name:')
            print('2.Quantity:')
            print('3.Price:')
            print('4.Go back to the Sub-Menu:')
            ch2=int(input('Choose a column:'))
            if ch2==1:
                print('============================')
                print('ItemName:')
                print(DFGI['Item Name:'])
                print('============================')
            elif ch2==2:
                print('============================')
                print('Quantity:')
                print(DFGI['Quantity:'])
                print('============================')
            elif ch2==3:
                print('============================')
                print('Price in Rs:')
                print(DFGI['Price (Rs):'])
                print('============================')
            elif ch2==4:
                R=1
            else:
                print('============================')
                print('Error!')
                print('============================')


    #3
    elif ch==3:
        print('============================')
        print('Items:')
        print(DFGI['Item Name:'])
        print('============================')

        Ad=str(input('Enter an item you want to add:'))
        if Ad in (DFGI['Item Name:']).values:
            print('============================')
            print('Item Already Present!')
        else:
            Q=int(input('Enter quantity:'))
            P=int(input('Enter Price:'))
            l1=list()
            l1.append(Ad)
            l1.append(Q)
            l1.append(P)
            DFGI.loc[Ad]=l1
            DFGI.reset_index(inplace=True)
            DFGI.drop(columns=['index'],inplace=True)
            print('============================')
            print('The item named',Ad,'has been added.')
            print('============================')
            print(DFGI)
                    

    #4
    elif ch==4:
        print('============================')
        print('Items:')
        print(DFGI['Item Name:'])
        print('============================')

        Dl=str(input('Choose an item you want to delete:'))
        if Dl in (DFGI['Item Name:']).values:
            DFGI=DFGI.drop(DFGI[DFGI['Item Name:']==Dl].index)
            print('============================')
            print('The item named',Dl,'has been removed.')
            print('============================')
            print(DFGI)
        else:
            print('============================')
            print('Item Not Present!')


    #5
    elif ch==5:
        R=3
        while R==3:
            print('============================')
            print('Select the graph you want to display:')
            print('1.Vertical bar graph of item quantity:')
            print('2.Horizontal bar graph of item quantity:')
            print('3.Line graph of item price:')
            print('4.Histogram of items in the same price range:')
            print('5.Go back to the Menu:')
            print('============================')
            ch2=int(input('Enter your choice:'))
            if ch2==1:
                DFGI[['Quantity:','Item Name:']].plot(kind='bar',x='Item Name:', title='Quantity of items present in the store:',color='red')
                plt.xlabel('Items:')
                plt.ylabel('Quantity:')
                plt.show()
            elif ch2==2:
                DFGI[['Quantity:','Item Name:']].plot(kind='barh',x='Item Name:', title='Quantity of items present in the store:',color='red')
                plt.ylabel('Items:')
                plt.xlabel('Quantity:')
                plt.show()
            elif ch2==3:
                DFGI[['Item Name:','Price (Rs):']].plot(kind='line',x='Item Name:', title='Price of items present in the store:',color='red',marker='H',markersize=10,linewidth=2)
                plt.ylabel('Items:')
                plt.xlabel('Price (Rs):')
                plt.show()
            elif ch2==4:
                DFGI[['Item Name:','Price (Rs):']].plot(kind='hist', title='Items in the same price range:',color='orange',edgecolor='lime',linewidth=2,linestyle=':')
                plt.xlabel('Price (Rs):')
                plt.show()
            elif ch2==5:
                R=1
            else:
                print('============================')
                print('Error!')

            
    #6    
    elif ch==6:
        print('Do you want to save and exit?')
        print('1.Save and exit:')
        print('2.Only exit:')
        print('3.Cancel:')
        ch2=int(input())
        if ch2==1:
            DFGI.to_csv('GroceryItems.csv',sep=',',index=False)
            exit()
        elif ch2==2:
            exit()
        elif ch2==3:
            print('============================')
            R=1
        else:
            print('============================')
            print('Error!')
            print('============================')
            R=1


    else:
        print('============================')
        print('Error!')
        print('============================')





